# invoice-sync

Receives invoice events from Partner (webhooks), stores them in PostgreSQL, and
a worker pushes each invoice to the Ledgerly accounting API.

- `src/server.ts` - HTTP server (webhooks)
- `src/worker.ts` - polls `invoices` with status `pending` and posts to Ledgerly
- `migrations/` - node-pg-migrate SQL migrations, run as a pre-deploy job
- `deploy/` - Kubernetes manifests (rolling updates)

Logging is plain `console.log` JSON lines; the platform ships stdout to Loki.
