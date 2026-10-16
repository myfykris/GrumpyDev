# Plan: Scale invoice-sync for Partner Plus

## Why

Partner Plus goes live on 2026-11-02. Partner expects volume to grow about
10x: roughly 30,000 invoices per business day, with month-end bursts of a few
hundred webhooks per minute (Partner's estimate, email of 2026-09-30).

## 1. Connection pooling

Add PgBouncer (a Deployment with 2 replicas) in front of PostgreSQL with
`pool_mode = transaction` and `default_pool_size = 40`. Point `DATABASE_URL`
for the server and the worker at PgBouncer. This keeps us under
`max_connections = 100` as we add replicas.

## 2. More workers, bigger batches

- Worker replicas: 1 -> 3. The claim query already uses
  `FOR UPDATE SKIP LOCKED`, so two workers never claim the same row.
- Batch size: 50 -> 500. Tick interval: 5 s -> 1 s.

## 3. Automate the daily reconciliation report

Move `scripts/report.ts` into the worker and run it every day at 09:00 New
York time. Exactly one worker must run it, so the workers elect a leader with
a PostgreSQL advisory lock:

```ts
// worker startup; does not block the push loop
pool.query("SELECT pg_advisory_lock(42)").then(() => startReportScheduler());
```

Non-leaders wait on the lock. If the leader dies, PostgreSQL releases its
session lock and another worker takes over automatically.

## 4. Customers table

Finance wants customer names in the report. Migration `002_customers.sql`:

```sql
CREATE TABLE customers (
  id   text PRIMARY KEY,
  name text
);
INSERT INTO customers (id) SELECT DISTINCT customer_id FROM invoices;
ALTER TABLE invoices
  ADD CONSTRAINT invoices_customer_fk
  FOREIGN KEY (customer_id) REFERENCES customers (id);
CREATE INDEX CONCURRENTLY invoices_customer_id_idx ON invoices (customer_id);
```

A nightly job fills `customers.name` from Partner's customer API.

## 5. Source tracking

Migration `003_source.sql`:

```sql
ALTER TABLE invoices ADD COLUMN source text;
```

Adding a nullable column with no default is instant in PostgreSQL 15, so this
can run at any time, including business hours.

## 6. Probes and shutdown

Server Deployment:

```yaml
livenessProbe:
  httpGet: { path: /healthz, port: 8080 }
  periodSeconds: 5
  failureThreshold: 1
```

`/healthz` changes to run `SELECT 1`, so a pod that has lost its database
connection gets restarted.

Server SIGTERM handling: `process.on("SIGTERM", () => server.close(() => process.exit(0)))`.
Keep the default `terminationGracePeriodSeconds` of 30 s.

## 7. Rate limiting

Protect the database from abusive callers:

```ts
import rateLimit from "express-rate-limit";
app.use("/webhooks", rateLimit({ windowMs: 60_000, limit: 300 })); // per client IP
```

300 requests per minute per IP is above Partner's month-end bursts.

## Rollout

One release: migrations 002 and 003, then PgBouncer, then the server and
workers.

## Testing

Load test in staging: 1,000 webhooks per minute for 10 minutes.
