# Operations

- PostgreSQL 15, managed. `max_connections = 100`.
- `invoices` holds about 600,000 rows (October 2026).
- `invoice-sync-server` sits behind the cluster's NGINX ingress, which
  terminates TLS and forwards requests to the Service. Partner calls
  `https://hooks.example.com/webhooks/partner/v1/invoice`.
- Partner retries a webhook that gets a non-2xx response or a connection error
  up to 3 times over 1 hour, then drops it and emails us a daily list.
- Migrations: the migration Job runs each migration file inside a transaction
  (BEGIN ... COMMIT), then on-call runs `kubectl apply -f deploy/`.
- Daily reconciliation report: on-call runs `scripts/report.ts` by hand at
  09:00 New York time. It opens one REPEATABLE READ transaction over the
  previous day's invoices and takes about 5 minutes.
