# Plan: Reliable Ledgerly pushes

## Problem

The worker (`src/worker.ts`) has three reliability gaps:

1. A row that fails once is marked `failed` and never retried. On-call re-sends
   these by hand (docs/operations.md).
2. If a request throws (timeout, connection reset), the error escapes the loop.
   That row and every remaining row in the claimed batch stay in `sending`
   forever.
3. `setInterval` starts a new tick every 5 s even if the previous tick is still
   running, so slow Ledgerly responses stack up concurrent ticks.

Goal: every invoice reaches Ledgerly exactly once without manual re-sends, and
invoices that cannot be delivered are surfaced to on-call.

Out of scope: v2 webhooks, the nightly export, and webhook handler error
handling. Each has its own plan.

## Schema: migration 002_push_retries.sql

```sql
SET lock_timeout = '3s';
ALTER TABLE invoices
  ADD COLUMN attempts        integer     NOT NULL DEFAULT 0,
  ADD COLUMN next_attempt_at timestamptz,
  ADD COLUMN claimed_at      timestamptz,
  ADD COLUMN last_error      text;
```

- PostgreSQL 15 adds columns with a constant default or no default as a
  catalog-only change, so there is no table rewrite. The statement needs a
  brief ACCESS EXCLUSIVE lock; if it cannot get it within 3 s it fails and
  on-call reruns the Job.
- No new index. The claim query filters on `status`, which
  `invoices_status_idx` already covers, and the pending, failed and sending
  rows are a small set (docs/operations.md).
- New status values: `dead` (gave up after retries) and `rejected` (Ledgerly
  returned a non-retryable error). `status` is `text`, so no type change.

## Claim query

```sql
UPDATE invoices
   SET status = 'sending', claimed_at = now(), attempts = attempts + 1
 WHERE id IN (
   SELECT id FROM invoices
    WHERE (status IN ('pending', 'failed')
           AND (next_attempt_at IS NULL OR next_attempt_at <= now()))
       OR (status = 'sending'
           AND (claimed_at IS NULL OR claimed_at < now() - interval '15 minutes'))
    ORDER BY id
    LIMIT 50
    FOR UPDATE SKIP LOCKED)
RETURNING *;
```

- A row stuck in `sending` is reclaimed after 15 minutes. `claimed_at IS NULL`
  covers rows stranded by the current code, which never sets `claimed_at`.
- A request takes at most 20 s (`headersTimeout` 10 s and `bodyTimeout` 10 s,
  both set explicitly), so a reclaimed row is never still in flight.
- Reclaiming is safe anyway: every attempt reuses the same Idempotency-Key,
  `inv-<partner_invoice_id>` (docs/ledgerly-api.md).

## Handling each response

Each row is pushed inside its own try/catch, and its outcome is written
immediately after its request, so one bad row cannot strand the rest of the
batch.

| Outcome | New status | Notes |
| --- | --- | --- |
| 201 or 200 | `sent` | |
| 409 `duplicate_external_id` | `sent` | The invoice already exists in Ledgerly. |
| 409 `idempotency_in_progress`, 429, 5xx, timeout, network error | `failed` | `next_attempt_at` = now + backoff. For 429, use `Retry-After` when it is larger. |
| 422 or any other 4xx | `rejected` | Log `invoice rejected` with the response body. |

- Backoff is full jitter: a random delay between 0 and
  `min(3600, 30 * 2^attempts)` seconds.
- After 12 attempts the row becomes `dead` and the worker logs `invoice dead`.
  The longest possible path to `dead` is about 6 hours, well inside the 30-day
  key retention, so Ledgerly deduplicates every retry.
- `last_error` stores the error or response body, truncated to 1,000
  characters.

## Scheduling and shutdown

- Replace `setInterval` with a loop that waits 5 s after each tick finishes, so
  ticks never overlap.
- On SIGTERM: stop starting new requests, let the in-flight request finish
  (at most 20 s), write its outcome, close the pool, and exit. The default
  `terminationGracePeriodSeconds` (30 s) covers this.

## Deployment

- Change the worker Deployment strategy from RollingUpdate to Recreate
  (`deploy/worker.yaml`). With one replica, this guarantees the old and new
  workers never run at the same time. Pushes pause for a few seconds during a
  deploy, which is fine: Finance needs invoices in Ledgerly by the next
  morning (docs/product.md).
- Order: run migration 002, then apply the new worker. The old 1.4.2 worker
  ignores the new columns, so the migration is safe while it is still running.

## Rollback

- Redeploy 1.4.2. The new columns stay and are ignored.
- Rows in `dead` or `rejected` stay as they are, because the old worker never
  selects them. Rows in `failed` behave as they do today.
- Migration 002 has a down migration that drops the four columns. A code
  rollback does not need it.

## Monitoring and runbook

- Every outcome is logged as one JSON line with the invoice id, attempt,
  status, and HTTP status.
- On-call adds two Grafana alert rules on Loki in the platform repo:
  - Any `invoice dead` or `invoice rejected` line pages on-call.
  - More than 200 rows claimed in 5 minutes with zero `sent` raises a warning
    (likely a Ledgerly outage).
- README gets a runbook entry: after fixing the cause, on-call re-queues a dead
  or rejected row with
  `UPDATE invoices SET status = 'pending', attempts = 0, next_attempt_at = NULL WHERE id = ...`.

## Testing

- Unit tests (vitest) for the response table above and the backoff bounds.
- Integration test against a local PostgreSQL 15 (Docker) and a fake Ledgerly
  that returns 500, then times out, then 201. Assert that:
  - the fake received the same Idempotency-Key every time;
  - the row ends `sent` after 3 attempts;
  - a row left in `sending` with `claimed_at` NULL is reclaimed.
- Kill test: send SIGTERM mid-request and check that the row ends `sent` or
  `failed`, and is never left in `sending` past the lease.

## Rollout

1. Merge. Run migration 002 in staging and deploy the worker to staging with
   `LEDGERLY_URL` pointed at the Ledgerly sandbox. Push a test invoice through
   a forced 500 and confirm one invoice in the sandbox.
2. Production: migration 002, then the worker.
3. Watch the logs for one day, then on-call stops manual re-sends. The existing
   `failed` rows are retried automatically on the first ticks. Rows that
   on-call already re-sent by hand get 409 `duplicate_external_id` and are
   marked `sent`.
