# Plan: Partner v2 webhooks, integer amounts, nightly export

## Goals

1. Partner is moving to v2 webhooks next month (new payload shape, amounts in
   integer cents). Support v2 alongside v1 until Partner turns v1 off.
2. Store amounts as integer cents everywhere.
3. Give Finance a nightly CSV export of the day's invoices.

## 1. v2 webhook endpoint

- Add `src/routes/webhooksV2.ts` with `POST /invoice`.
- Mount it in `server.ts` with `app.use("/webhooks/partner/v2", webhooksV2)`,
  reusing the existing router setup.
- v2 payload: `{ invoice_id, customer, total_cents, currency }`. Map to the
  same `invoices` columns.

## 2. Integer cents migration

- New migration `002_amount_cents.sql`:

  ```sql
  ALTER TABLE invoices RENAME COLUMN amount TO amount_cents;
  ALTER TABLE invoices ALTER COLUMN amount_cents TYPE bigint
    USING (amount_cents * 100)::bigint;
  ```

- Update `webhooksV1.ts`, `worker.ts`, and the new v2 route to use
  `amount_cents`. v1 handler multiplies `amount` by 100.
- Ledgerly's bulk endpoint accepts amounts in integer cents too, so the worker
  sends `amount_cents` directly.
- Ship as one release: the migration runs as the usual pre-deploy job, then the
  rolling update rolls out the new code.

## 3. Nightly export

- Add a Redis instance (managed, small) and use a Redis lock (Redlock) so only
  one worker runs the export.
- In `worker.ts`, add a `setInterval` that checks every minute whether it is
  past midnight and the export has not run yet today.
- Query: `SELECT * FROM invoices WHERE created_at >= $1` where `$1` is
  `new Date().setHours(0,0,0,0)` (midnight today).
- Write the CSV to `/tmp/exports/invoices-YYYY-MM-DD.csv`. A separate CronJob
  uploads the contents of `/tmp/exports` to the Finance S3 bucket at 06:00.
- Switch the worker to Ledgerly's bulk endpoint (`POST /v2/invoices/bulk`,
  up to 10,000 invoices per request) so the nightly export and the push use the
  same batch, and drop per-invoice idempotency keys since the bulk call is a
  single request.

## Logging

- Keep using `console.log` JSON lines like the rest of the service.

## Testing

- Unit test the v2 payload mapping.
- Run the migration against a local database.

## Rollout

- Deploy to staging, check a v2 test webhook, deploy to production.
