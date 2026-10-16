# Ledgerly API (the parts we use)

Source: Ledgerly developer docs, API v2, copied 2026-08-14.

## POST /v2/invoices

Body: `{ "external_id": string, "amount": string, "currency": string }`

- `amount` is a decimal string in major units, for example `"19.99"`.
- `currency` is an ISO 4217 code.

Headers: `Authorization: Bearer <token>`, `Idempotency-Key: <string, max 255>`.

Responses:

- 201 Created: the invoice was created.
- 200 OK: a request with the same Idempotency-Key and an identical body was
  already processed; the original invoice is returned.
- 409 Conflict, code `duplicate_external_id`: an invoice with this external_id
  already exists (created under a different key). The body includes the
  existing invoice id.
- 409 Conflict, code `idempotency_in_progress`: a request with the same key is
  still being processed. Retry later.
- 422 Unprocessable Entity: validation error. Not retryable.
- 429 Too Many Requests: rate limited. Honor `Retry-After` (seconds).
- 5xx: transient. Retry.

Idempotency keys are retained for 30 days.

Rate limit: 20 requests per second per token.
