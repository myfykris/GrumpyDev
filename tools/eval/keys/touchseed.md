# Answer key: sound plan in files with pre-existing problems, project ledger seeded
(docs/plans/issued-at.md; .grumpydev/reviews/project.md holds 19 issues from an earlier audit)

The plan edits src/routes/webhooks.ts, src/invoices/repository.ts and
src/export/nightlyCsv.ts, adds a migration and extends tests/e2e/webhook.test.ts.
It uses verifySignature.ts, context.ts and partnerContext.ts, money.ts and locks.ts.

Seeded project issues located in units the plan touches or uses (in scope):
project:GD-003 (partner global), GD-004 (CSV /100), GD-005 (unauthenticated crash
in the webhook), GD-006 (Slack before insert), GD-007 (identity not partner-scoped
in the insert), GD-008 (one secret, unsigned partner header), GD-010 (CSV day
boundary), GD-011 (CSV quoting), GD-012 (money rule copies), GD-013 (repository
imports the route), GD-015 (repository reads the global), GD-016 (lock 42 in the
export), GD-017 (test bypass in verifySignature). That is 13 issues.
Out of scope (units the plan neither touches nor uses): GD-001, GD-002, GD-009,
GD-014, GD-018, GD-019.

Score:
- C1 Count of in-scope seeded issues the review cites by their project ID
  (for example "project:GD-004"), out of 13. Report the list.
- C2 Count of in-scope seeded issues the review reports again as a new issue
  (its own new ID) without citing the project ID. Quote each.
- C3 Count of out-of-scope seeded issues the review reports or cites as findings.
  Quote each.
- R For each cited issue, does the review say how the plan relates to it and give
  fix first, fix in this change, or keep as known debt? 1 if all cited issues
  have that, 0.5 if most, 0 if few.
- V 1 if the review says whether the plan's own changes are sound and keeps
  pre-existing issues apart from plan defects, 0.5 if mixed, 0 otherwise.
Also count the plan's own findings: VALID-MATERIAL, VALID-MINOR, INVALID; and give
signal-to-noise 1-5.
