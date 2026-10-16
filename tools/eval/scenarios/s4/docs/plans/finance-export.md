# Plan: Nightly Finance export

Finance wants a CSV each morning that lists the previous New York day's
invoices together with each invoice's Ledgerly id, so they can find every row
in Ledgerly directly.

## Design

- Add an export step to the existing worker. The worker is a single replica
  (DEC-001), so no lock or leader election is needed.
- At 01:00 New York time, the worker selects the previous New York day's
  invoices: `created_at >= start_of_day AND created_at < start_of_next_day`,
  with both bounds computed in SQL using `AT TIME ZONE 'America/New_York'`.
- For each invoice, call `GET /v2/invoices?external_id=<partner_invoice_id>`
  to get its Ledgerly id, then write the CSV row: partner_invoice_id,
  ledgerly_id, customer_id, amount, currency, created_at (New York time).
- Upload the file directly to `s3://finance-exports/invoices/YYYY-MM-DD.csv`
  (overwritten on rerun), using the worker's existing IAM role plus a new
  policy that allows PutObject on that prefix only.
- Record completion in a new table
  `export_runs (day date PRIMARY KEY, rows int, finished_at timestamptz)`, and
  skip the run if that day's row already exists.
- Logging: JSON lines. Add a Loki alert that fires if no `export finished`
  line appears by 06:00 New York time (DEC-003).

## Volume

About 3,000 invoices per business day, with peaks around 9,000
(docs/product.md).

## Testing

- Unit test the day-window computation across both DST changes.
- Integration test with a fake Ledgerly.
