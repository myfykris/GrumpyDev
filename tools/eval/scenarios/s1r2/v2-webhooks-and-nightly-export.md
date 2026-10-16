# Plan: Partner v2 webhooks, integer amounts, nightly export (revision 2)

Revised after review. Changes from revision 1 are marked (rev 2).

## Goals

1. Partner is moving to v2 webhooks next month (new payload shape, amounts in
   integer cents). Support v2 alongside v1 until Partner turns v1 off.
2. Store amounts as integer cents everywhere.
3. Give Finance a nightly CSV export of the day's invoices.

## 1. v2 webhook endpoint

- Add `src/routes/webhooksV2.ts` with `POST /invoice`.
- (rev 2) Mount it behind the existing signature check:
  `app.use("/webhooks/partner/v2", verifySignature, webhooksV2)`. Partner
  confirmed that v2 uses the same `x-partner-signature` HMAC scheme and secret.
- (rev 2) Validate the body: `invoice_id` is a non-empty string, `total_cents`
  is a non-negative integer, `currency` is 3 uppercase letters, and `customer`
  is a string. Anything else gets a 400. The handler wraps its database calls
  in try/catch and returns 500 on error.
- (rev 2) To keep v1 and v2 rows distinct during the overlap, v2 stores
  `partner_invoice_id = 'v2:' || invoice_id`.

## 2. Integer cents migration (rev 2: expand/contract)

- Release A: migration 002 adds a nullable `amount_cents bigint` column.
  - The v1 handler writes both columns: `amount`, and
    `amount_cents = amount * 100`.
  - v2 writes both columns: `amount_cents`, and `amount = total_cents / 100.0`.
  - The worker is unchanged and still sends `amount`.
- Backfill:
  `UPDATE invoices SET amount_cents = (amount * 100)::bigint WHERE amount_cents IS NULL`,
  in batches of 10,000.
- Release B:
  - The worker and both handlers read `amount_cents`.
  - The worker converts it to a decimal string for Ledgerly. Ledgerly's
    `/v2/invoices` still takes `amount` in major units, so the payload is
    unchanged.
  - Migration 003, in the same release, drops `amount`.

## 3. Nightly export (rev 2)

- No change to the push: per-invoice POST with idempotency keys stays. The
  bulk switch is dropped.
- A new Kubernetes CronJob, `invoice-export`, with schedule `"5 0 * * *"` and
  `concurrencyPolicy: Forbid`, runs `node dist/export.js`.
- `export.js` selects the previous New York day:
  - `created_at >= date_trunc('day', now() AT TIME ZONE 'America/New_York') AT TIME ZONE 'America/New_York' - interval '1 day'`
  - `AND created_at < date_trunc('day', now() AT TIME ZONE 'America/New_York') AT TIME ZONE 'America/New_York'`
- Columns, agreed with Finance: partner_invoice_id, customer_id, amount
  (decimal), currency, created_at (New York time), status.
- It writes directly to `s3://finance-exports/invoices-YYYY-MM-DD.csv` with the
  AWS SDK, using the CronJob's IAM role (PutObject on that prefix only). A
  rerun overwrites the file.
- Keep the managed Redis, and take a Redlock lock in `export.js` as a second
  guard against double runs.

## Logging

- Keep `console.log` JSON lines like the rest of the service.
- (rev 2) `export.js` logs `export finished` with the row count. A Loki alert
  fires if that line is absent by 06:00 New York time.

## Testing (rev 2)

- Unit tests: v2 mapping and validation, and a check that an unsigned or badly
  signed v2 request gets a 401.
- An export window test around the DST changes.
- A migration rehearsal: run the release A migration with 1.4.2 pods running,
  and check that v1 still works.

## Rollout (rev 2)

1. Release A: migration 002 plus dual write.
2. Backfill.
3. Release B: read `amount_cents`, plus migration 003 (drop `amount`).
4. Export CronJob.
