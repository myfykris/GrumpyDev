# Answer key: research-deferral test (plan: docs/plans/multi-currency.md)

The plan defers several decisions. Grade how each review handles them.

Hidden decision-affecting research (score 1 if the review flags the item as an
unresolved decision AND says what later work depends on it; 0.5 if it only lists
it as an open question or mentions it without the dependency; 0 if absent):
- H1 Rate source (step 2) is undecided, yet the fx_rates schema (rate_source_id),
  the 00:30 New York load time, and the step 5 export rule already depend on it
  (sources publish at different times and with different semantics).
- H2 Whether Ledgerly accepts non-USD invoices (step 3) is undecided, yet step 3
  already changes the worker to send amount_minor and currency on every push.
- H3 Historical restatement is TBD with Finance (step 6), yet its backfill job is
  scheduled to ship in the same release.
- H4 Rounding/minor units (step 7) is uninvestigated, yet step 1 already backfills
  amount_minor = amount * 100 for all rows and adds currency_minor_units; JPY has
  0 minor units (and some currencies 3), so step 1 bakes in the answer.

Answerable from the repository (score 1 if the review answers it correctly from
the repo, 0.5 if it says the repo can answer it without answering, 0 if it leaves
it open, treats it as a blocker, or ignores it):
- A1 Amount column type today: numeric(12,2) (migrations/001_init.sql).
- A2 The worker already sends an idempotency key: `idempotency-key: inv-<partner_invoice_id>` (src/worker.ts).
- A3 Worker deployment: Kubernetes Deployment, 1 replica, RollingUpdate (deploy/worker.yaml).

Verdict and structure:
- V Score 1 if the verdict blocks implementation (NEEDS INFO / REVISE / not
  ready) AND recommends resolving the decisions first (a discovery step, splitting
  the plan, or sequencing research before dependent work); 0.5 if it blocks
  without that; 0 if it approves.

Penalties (count instances, with quotes):
- X1 Treats the bounded bulk-push spike (step 4) as a defect or blocker.
  (Noting it is fine, or a minor suggestion about it, is not a penalty.)
- X2 Invents an answer to H1-H4 without evidence (for example asserting Ledgerly
  supports EUR, or that a rate source publishes at a given time, as fact).

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID.
