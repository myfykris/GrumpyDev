# Answer key: clean plan in units with pre-existing boundary problems
(docs/plans/issued-at.md)

The plan itself is meant to be sound. It touches src/routes/webhooks.ts,
src/invoices/repository.ts, src/export/nightlyCsv.ts, a new migration, and
tests/e2e/webhook.test.ts. Those units already have problems. The project
notes (.grump) record no known debt. Score how each review handles them.

Scope (per Kris, 2026-10-15): a plan review reports pre-existing problems only
in units the plan touches or uses (edits, calls into, reads or depends on):
src/routes/webhooks.ts, src/routes/verifySignature.ts, src/invoices/repository.ts,
src/context.ts and src/routes/partnerContext.ts, src/money.ts,
src/export/nightlyCsv.ts, src/locks.ts, migrations/, tests/e2e/webhook.test.ts.
Out of scope: src/worker/*, src/invoices/batch.ts, src/routes/admin.ts,
src/ledgerly/*, src/reports/*.

Pre-existing problems in touched units (1 = reported with location and a
concrete consequence; 0.5 = mentioned without consequence or only in passing;
0 = absent):
- T1 The webhook handler is BLENDED (signature check, validation, money
  parsing, credit-limit SQL, Slack alert, insert in one function), and the plan
  adds another validation job to it.
- T2 webhooks.ts restates the minor-unit rule inline (`e.currency === 'JPY' ? 0 : 2`
  with float math) instead of `toMinor` in src/money.ts, which D3 names as
  the owner.
- T3 repository.ts imports `SUPPORTED` from routes/webhooks.ts (INVERTED); the
  worker therefore loads the route module and needs the webhook secret.
- T4 repository.ts reads the module-global `currentPartner` (hidden argument),
  which concurrent requests overwrite once Acme is live (2026-11-01). Credit 1
  also if it notes the plan already changes `NewInvoice`/`insertInvoice`, so
  passing the partner explicitly fits this change.
- T5 nightlyCsv.ts formats every amount with `/ 100`, so JPY amounts are 100x
  too small (JPY starts 2026-11-01). The plan edits this function.
- T6 nightlyCsv.ts shares advisory lock 42 with the worker tick, so the export
  can fail when a tick holds it.
- T7 The test the plan extends relies on the `NODE_ENV === 'test'` signature
  bypass in verifySignature.ts, a test hook on the production path.

Framing (score 0, 0.5 or 1):
- V 1 if the review says the plan's own changes are sound (or raises no
  invalid defect against them) and presents the pre-existing problems
  separately, with a recommendation per problem (fix first, fix in this change,
  or record as known debt). 0.5 if it reports pre-existing problems but mixes
  them with plan defects, or blocks the plan without saying the plan itself is
  sound. 0 if it reports none of T1-T7, or calls the plan defective on invalid
  grounds.

Penalties (count instances, with quotes):
- X1 A defect attributed to the plan that is not real.
- X2 A false factual claim about the code or history.
- X3 Requires restructuring of units the plan does not touch (worker/*,
  invoices/batch.ts, routes/admin.ts, ledgerly/*) before the plan can ship.
  Mentioning them, or suggesting it as optional, is not a penalty.

- X4 A pre-existing problem reported in an out-of-scope unit (noise). Count
  each one, with a quote.

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID; and give a
signal-to-noise rating 1-5.
