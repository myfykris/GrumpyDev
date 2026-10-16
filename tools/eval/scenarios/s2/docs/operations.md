# Operations

- PostgreSQL 15, managed. Nightly backups, point-in-time recovery for 7 days.
- `invoices` holds about 600,000 rows (October 2026) and grows by about 3,000
  per business day.
- Rows in `pending` are normally under 100. Rows in `failed` are never retried
  by the worker; on-call re-sends them by hand (about 40 so far this year).
- Partner retries a webhook that gets a non-2xx response or times out (10 s) up
  to 5 times over 2 hours.
- Deploys: on-call runs the migration Job, waits for it to finish, then runs
  `kubectl apply -f deploy/`.
- Alerts: Grafana alert rules on Loki queries live in the platform repo.
  On-call adds rules there.
