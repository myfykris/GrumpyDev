# Plan: Multi-currency invoices

## Why

Partner starts sending EUR and JPY invoices on 2026-12-01 (Partner email,
2026-10-02). Today every invoice is USD. Finance reconciles in USD.

## Steps

1. Schema. Add `currency_minor_units smallint` and `amount_minor bigint` to
   `invoices` and backfill `amount_minor = amount * 100` for every existing row.
   Determine which column type stores amounts today before writing the
   migration.

2. Exchange rates. Add an
   `fx_rates (day date, currency char(3), rate_to_usd numeric(18,8), rate_source_id int)`
   table and a nightly job that loads rates at 00:30 New York time. Research
   which rate source to use (ECB reference rates, Ledgerly's rates, or Partner's
   invoice-day rate).

3. Ledgerly push. Determine whether Ledgerly accepts non-USD invoices. Update
   the worker to send `amount_minor` and `currency` on every push and keep the
   existing retry behavior. Research whether the worker already sends an
   idempotency key.

4. Bulk push spike. Time-boxed spike (2 days, before step 5): send 500 sandbox
   invoices through Ledgerly's bulk endpoint and measure p95 latency. If p95 is
   above 5 s, keep per-invoice pushes. Record the decision in
   `docs/decisions.md` before step 5 starts.

5. Finance export. Add a USD column to the nightly CSV, using the rate for the
   invoice's New York day.

6. Historical restatement. TBD: confirm with Finance whether invoices before
   2026-12-01 must be restated in USD. The backfill job for this ships in the
   same release as steps 1-3.

7. Rounding. Investigate rounding rules for currencies that do not use 2
   decimal places.

## Rollout

Figure out how the worker is deployed and scale it if needed. Ship steps 1, 2,
3, 5 and 6 together in one release on 2026-11-15.
