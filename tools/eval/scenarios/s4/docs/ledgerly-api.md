# Ledgerly API (the parts we use)

Source: Ledgerly developer docs, API v2, copied 2026-08-14.

## POST /v2/invoices

Body: `{ "external_id": string, "amount": string, "currency": string }`.
`amount` is a decimal string in major units.

Headers: `Authorization: Bearer <token>`, `Idempotency-Key`.

- 201 Created: returns `{ "id": "<ledgerly invoice id>", ... }`.
- 200 OK: same key and body seen before; returns the original invoice,
  including `id`.
- 429: rate limited; honor `Retry-After`.

## GET /v2/invoices?external_id=<external_id>

Returns `{ "id": "<ledgerly invoice id>", "status": ... }`, or 404 if no
invoice has that external_id.

## Limits

5 requests per second per token, shared across all endpoints.
