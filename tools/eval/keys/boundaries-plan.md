# Answer key: plan review (docs/plans/credit-notes.md)

Score each item 1 (found, with the right consequence), 0.5 (found but the
consequence is missing or wrong, or only hinted), 0 (absent).

- P1 Step 1 restates the minor-unit rule inline (`e.currency === 'JPY' ? 0 : 2`)
  instead of using `src/money.ts` (`toMinor`, `MINOR_UNITS`), which docs/decisions.md
  D3 names as the source of minor units. Credit is for naming money.ts/toMinor
  as the owner that is bypassed or duplicated. Agrees today, so MEDIUM is right;
  HIGH is acceptable only with a stated reason.
- P2 Step 1 puts more work (a second event type and raw SQL persistence) into
  the webhook handler, which already blends several jobs (known debt in
  `.grump` for reviewers that have it). Credit for flagging that the plan grows
  this handler or puts persistence in the route instead of a repository.
- P3 Step 3 has CreditApplier reach into InvoiceBatch's private `rows` and edit
  `amount_minor`. Credit 1 requires a concrete consequence, any of:
  - the database amount never changes (`InvoiceBatch.commit` writes only
    status), so the CSV and dashboard show the gross amount while Ledgerly has
    the net amount, breaking reconciliation; it also contradicts D1 (amounts are
    never changed after receipt);
  - the credit notes are marked `applied` before the push succeeds, so a failed
    or retried push loses the credit, or a retry sends a different body under
    the same idempotency key.
- P4 Step 4 sets `invoices.status = 'credited'`, which the CHECK constraint in
  migrations/001_init.sql rejects, so the update fails. 0.5 if it only says the
  status lifecycle is spread out without naming the constraint.
- P5 Step 5 calls Ledgerly with a raw `fetch`, bypassing `src/ledgerly/client.ts`
  (README: the only code that talks to Ledgerly; D2). Credit 1 requires a
  consequence: it loses the client's timeouts or 409 handling, or the two worker
  replicas both run the loop and post the same credit notes (409 responses
  then go unhandled).
- P6 Step 7 formats credit amounts with `/ 100`, copying the exporter's existing
  rule, which is wrong for JPY (0 minor units): JPY credits come out 100x too
  small. Credit 1 requires noting the JPY error (or the existing exporter bug).
- P7 The plan never names an owner for the new concept (credit-note money
  rules, persistence, Ledgerly calls, batch changes). Credit 1 for a finding
  that says where credit-note logic should live (for example a credits module
  that uses money.ts, a repository, and a new client function), 0.5 if implied
  only through individual fixes.

Bonus (not in the sum, report separately):
- PB The existing exporter already prints JPY invoice amounts 100x too small
  (`src/export/nightlyCsv.ts`), independent of the plan.

Penalties (count instances, with quotes):
- X1 Flags a well-designed part as a defect: step 6 placing types in
  `src/ledgerly/types.ts` (that is where D2 says they go), the Ledgerly
  client, or the InvoiceBatch API itself (the problem is the bypass).
- X2 A factual claim about the code that is false.
- X3 Proposes restructuring outside the plan's scope as a requirement (for
  example rewriting the whole webhook handler or worker before credit notes can
  ship). Suggesting it as optional is not a penalty.

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID.
