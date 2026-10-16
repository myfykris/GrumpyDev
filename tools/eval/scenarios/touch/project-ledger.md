# Ledger: project

| ID | Severity | Status | Issue | Closes when | First seen | Last checked |
|----|----------|--------|-------|-------------|------------|--------------|
| GD-001 | HIGH | NEW | Ledgerly 409 path leaves the invoice in 'sending' forever (retry.ts bypasses InvoiceBatch.commit) | a test with one markSent and one 409 row issues an UPDATE to 'sent' for both; rows stuck in 'sending' > 10 min: 0 | 2026-10-15 | 2026-10-15 |
| GD-002 | HIGH | NEW | Transient push errors are terminal ('failed'); claimed 'sending' rows have no reaper; worker SIGTERM strands a batch | a 5xx/timeout returns the row to 'pending' with backoff and it is sent within 5 min; stale 'sending' rows are re-pended automatically | 2026-10-15 | 2026-10-15 |
| GD-003 | HIGH | NEW | Module-level currentPartner shared across concurrent requests and set before authentication | module-level mutable request state in src: 1 -> 0; interleaved-request test keeps each partner | 2026-10-15 | 2026-10-15 |
| GD-004 | HIGH | NEW | Nightly CSV divides every amount by 100: JPY rows 100x too low from the first JPY export | CSV formats via money.ts; JPY export test passes; '/ 100' outside money.ts in src: 1 -> 0 | 2026-10-15 | 2026-10-15 |
| GD-005 | HIGH | NEW | Unauthenticated request crashes the process: non-JSON content type + signature header makes hmac.update({}) throw in an unguarded async Express 4 handler | such a request returns 4xx; async handlers without error handling: 3 -> 0 | 2026-10-15 | 2026-10-15 |
| GD-006 | HIGH | NEW | Slack alert runs before the insert, no try/catch, no timeout: Slack failure drops or stalls ingest (inside known-debt function) | insert precedes alert; alert is best-effort with a timeout; Slack-failure test still returns 202 | 2026-10-15 | 2026-10-15 |
| GD-007 | HIGH | NEW | Invoice identity is not partner-scoped (global UNIQUE, ON CONFLICT DO NOTHING, key inv-<id>): an Acme id equal to a Partner id is silently dropped | unique (partner_id, partner_invoice_id); two partners with the same id produce two rows and two Ledgerly pushes | 2026-10-15 | 2026-10-15 |
| GD-008 | MEDIUM | NEW | One webhook secret for all callers; x-partner-id is unsigned and unbound to a secret; Acme has no signing secret defined | per-partner secrets keyed by partner id; unknown partner id -> 401 | 2026-10-15 | 2026-10-15 |
| GD-009 | HIGH | NEW | Dockerfile sets NODE_ENV=production before npm install, so devDependencies (tsc) are omitted and the build step fails; no lockfile | image builds from the Dockerfile in CI; lockfile committed and used (npm ci) | 2026-10-15 | 2026-10-15 |
| GD-010 | MEDIUM | NEW | UTC-day boundary depends on the DB session TimeZone (CSV window, dashboard view), which nothing sets | CSV window and view use explicit UTC; copies of the UTC-day rule: 2 -> 1 | 2026-10-15 | 2026-10-15 |
| GD-011 | MEDIUM | NEW | CSV fields are not quoted; ids come unvalidated from the webhook | CSV writer quotes fields; ingest validates id format | 2026-10-15 | 2026-10-15 |
| GD-012 | HIGH | NEW | DUPLICATED/BYPASSED: minor-unit and supported-currency rule; money.ts has 0 production callers | copies outside money.ts: TS 3 -> 0, SQL 1 -> 1 guarded by a parity test; production callers of money.ts: 0 -> 3 | 2026-10-15 | 2026-10-15 |
| GD-013 | MEDIUM | NEW | INVERTED: invoices/repository.ts imports SUPPORTED from routes/webhooks.ts; worker loads the route and needs the webhook secret | imports of routes/ from outside routes/: 1 -> 0; PARTNER_WEBHOOK_SECRET in worker.yaml: 1 -> 0 | 2026-10-15 | 2026-10-15 |
| GD-014 | HIGH | NEW | BYPASSED/LEAKY: worker/retry.ts mutates InvoiceBatch private rows via 'as any' | 'as any' in src: 1 -> 0; retry.ts deleted | 2026-10-15 | 2026-10-15 |
| GD-015 | HIGH | NEW | INVERTED: repository reads request-scoped global state (context.ts) as a hidden argument | repository takes partnerId as an argument; context.ts and partnerContext middleware deleted | 2026-10-15 | 2026-10-15 |
| GD-016 | MEDIUM | NEW | BLENDED: JOB_LOCK 42 serves worker-vs-export, worker-vs-worker and export-vs-export, and is held across network I/O | purposes per lock: 3 -> 1; export no longer fails because a tick is running | 2026-10-15 | 2026-10-15 |
| GD-017 | MEDIUM | NEW | BLENDED: NODE_ENV==='test' returns true in verifySignature; no test exercises the real check | NODE_ENV reads in src: 1 -> 0; a test sends a correctly signed and a wrongly signed body | 2026-10-15 | 2026-10-15 |
| GD-018 | MEDIUM | NEW | SCATTERED: Ledgerly idempotency-key and 409 rules live in worker/, not src/ledgerly (README and D2 say only src/ledgerly knows Ledgerly) | key/409 rule sites outside src/ledgerly: 2 -> 0 | 2026-10-15 | 2026-10-15 |
| GD-019 | MEDIUM | NEW | SCATTERED: invoice status transitions in 4 files; admin requeue bypasses the repository and can reset an in-flight 'sending' row | writers of invoices.status outside src/invoices/: 1 -> 0 | 2026-10-15 | 2026-10-15 |

## 2026-10-15 - first review (whole project)

Verdict: AT RISK. 19 issues, all NEW. Not checked: vitest suite not run (no install), pre-deploy migration job and image build pipeline (not in repo), real Ledgerly and Express behavior.
