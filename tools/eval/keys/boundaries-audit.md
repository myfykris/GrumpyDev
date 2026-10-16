# Answer key: codebase audit of the invoicer repository

Score each item 1 (found, located, with the right consequence), 0.5 (found but
the consequence or location is missing or wrong), 0 (absent).

Defects (live or latent):
- D1 The nightly CSV (`src/export/nightlyCsv.ts`) formats every amount with
  `/ 100` and two decimals. JPY has 0 minor units, so JPY amounts come out 100x
  too small once JPY starts (2026-11-01, docs/product.md).
- D2 `src/worker/retry.ts` `handleConflict` edits InvoiceBatch's private rows
  (`(batch as any).rows`) instead of calling `markSent`. The row is not in the
  `sent` map and its in-memory status is no longer `sending`, so `commit()`
  neither marks it sent nor returns it to pending: every 409'd invoice stays in
  `sending` forever and its Ledgerly id is lost.
- D3 `src/context.ts` `currentPartner` is module-level state set by middleware
  and read in `insertInvoice` after an `await` in the handler (the credit-limit
  query). Concurrent requests overwrite it, so invoices can get another
  request's partner_id once Acme goes live (2026-11-01).
- D4 Advisory lock 42 (`src/locks.ts` JOB_LOCK) serves several purposes: the
  export's single-run guard and the worker's per-tick guard. Credit 1 requires
  at least two consequences of: the export fails when a tick holds the lock
  (the 2026-07-02 commit only retries it); pushes stop while the export runs,
  against the 5-minute target; only one of the two worker replicas can tick at
  a time.

Boundary findings:
- F1 The minor-unit rule exists in several places: `src/money.ts` MINOR_UNITS
  (owner), the inline `e.currency === 'JPY' ? 0 : 2` in `src/routes/webhooks.ts`,
  the SQL CASE in `migrations/003_report_minor_units.sql` (a hand-kept mirror
  across the TS/SQL boundary), and `/ 100` in the exporter. Credit 1 for at
  least 3 of the 4 copies cited; 0.5 for 2.
- F2 `toMinor`/`formatMinor` exist and are tested but are bypassed (webhook
  parsing, exporter formatting).
- F3 The supported-currency list is kept twice: `SUPPORTED` in webhooks.ts and
  the keys of MINOR_UNITS (`isSupportedCurrency` is unused).
- F4 INVERTED: `src/invoices/repository.ts` imports `SUPPORTED` from
  `src/routes/webhooks.ts`. Credit 1 requires a consequence: the worker now
  loads the route module and verifySignature, which throws without
  PARTNER_WEBHOOK_SECRET, so the worker was given the webhook secret (the
  2026-07-22 fix), or the circular import between repository and webhooks.
- F5 The invoice status lifecycle has no owner: transitions are written in
  repository (claim), batch (commit), retry.ts (in memory), the admin requeue
  route, and the CHECK constraint. Credit 1 requires a concrete consequence,
  for example the admin requeue also resets rows that are `sending`, so an
  in-flight invoice can be claimed and pushed again (409, then stuck via D2).
- F6 Test hook on a production path: `verifySignature` returns true when
  `NODE_ENV === 'test'`. The Dockerfile sets NODE_ENV=production, so it is not
  live as deployed. Credit 1 for flagging it with the correct exposure; 0.5 if
  it is flagged as live in production (also count that as X2).
- F7 The webhook handler blends signature check, validation, money parsing,
  credit-limit query, Slack alert and insert. It is recorded as known debt in
  `.grump` for reviewers that have that file. For those, credit 1 for listing
  it as known debt (or omitting it); for others, credit 1 for reporting it.

Cost from history (score 0, 0.5 or 1):
- H Classifies fix commits by root cause and links them to findings. Credit 1
  for at least 3 correct links of: 2026-04-07 (0.29 stored as 28: bypassed
  toMinor), 2026-09-04 (JPY dashboard: duplicated minor-unit rule),
  2026-07-22 (worker needs webhook secret: inverted import), 2026-07-02 (export
  lock busy: shared lock). 0.5 for 1-2 links. The 2026-03-18 CSV column order
  fix is unrelated to boundaries.

Preserve (score 0, 0.5 or 1):
- K Names well-designed boundaries to keep: `src/ledgerly/` as the only code
  that talks to Ledgerly, with types and mapping kept apart (D2); `src/money.ts`
  as a tested owner; InvoiceBatch's markSent/markFailed/commit API. 1 for at
  least two, 0.5 for one.

Penalties (count instances, with quotes):
- X1 Flags a well-designed boundary as a defect (for example "duplicate types
  in ledgerly/types.ts and InvoiceRow", or InvoiceBatch's API as the problem).
- X2 A factual claim about the code or history that is false.

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID; and give a
signal-to-noise rating 1-5 (5 = every line useful to the owner).
