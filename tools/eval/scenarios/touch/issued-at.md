# Plan: store Partner's invoice issue date

## Why

From 2026-11-01 Partner adds `issued_at` (an ISO 8601 date, for example
`2026-11-03`) to every invoice webhook. Finance wants it in the nightly CSV so
they can match Partner's monthly statements. Finance has agreed that invoices
received before this change, and any received by old server pods during the
rollout, have an empty issue date.

## Steps

1. Migration `005_issued_at.sql`: `ALTER TABLE invoices ADD COLUMN issued_at date;`
   Nullable, no default, no backfill.
2. `src/routes/webhooks.ts`: add `issued_at?: string` to `PartnerInvoiceEvent`.
   If it is present and does not match `/^\d{4}-\d{2}-\d{2}$/`, or is not a
   real calendar date, return 422 before any other work.
3. `src/invoices/repository.ts`: add `issuedAt: string | null` to `NewInvoice`
   and write it to `issued_at` in `insertInvoice`. The handler passes
   `e.issued_at ?? null`.
4. `src/export/nightlyCsv.ts`: select `issued_at` and append an `issued_at`
   column at the end of each line (empty when NULL, otherwise `YYYY-MM-DD`).
   Finance confirmed that appending a column does not break their import.
5. Tests: extend `tests/e2e/webhook.test.ts` with an invoice carrying a valid
   `issued_at` (202) and one with `issued_at: "2026-02-30"` (422).

## Rollout

Migration 005 runs in the usual pre-deploy job. Then the server, then the
export CronJob image. The column is nullable and unused by old code, so old and
new pods can run together, and rolling back the image is safe.
