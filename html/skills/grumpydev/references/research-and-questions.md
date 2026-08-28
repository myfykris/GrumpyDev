# Research and review questions

## Resolve decision-affecting research

Treat research as decision-affecting when its result could materially change
architecture, scope, safety, a data model or migration, an external contract,
implementation sequencing, rollback, operating cost, or the review verdict.
Do not apply this label to ordinary verification of a selected design when the
plan defines both the success criteria and the response to failure without
leaving a material design choice open.

Read `Decision-affecting research` from `.grump` when present:

- `resolve first` means an implementation plan cannot receive `APPROVE` or
  `APPROVE WITH CONCERNS` while such research remains unresolved. Complete the
  research, select the resulting implementation decision, and review the
  resulting plan.
- `gated discovery` means GrumpyDev may approve a plan whose complete scope is a
  bounded discovery phase with explicit research questions, evidence methods,
  decision criteria, stopping conditions, and named downstream decisions. It
  must not approve the downstream implementation until the research is
  resolved, the implementation plan is updated, and that plan is Grumped again.
- absent or `unresolved` defaults to `gated discovery`.

A mixed plan that includes both unresolved discovery and dependent downstream
implementation is not ready as one implementation plan. Require it to resolve
the research first or split out the bounded discovery plan. Use `REVISE` when a
responsible corrected path is clear and `INSUFFICIENT EVIDENCE` when the missing
research prevents one.
## Perform needed research

Read `Research execution` from `.grump` when present:

- `automatic` means perform safe, read-only research during the evidence pass
  when the needed access and tools are available.
- `ask first` means ask one deduplicated `RQ###` permission question before
  starting that research, even when review questions are otherwise
  non-interactive.
- `report only` means do not perform the research; identify the exact research,
  why it matters, and the decision it blocks under `Evidence gaps`.
- absent or `unresolved` defaults to `ask first`.

Use project evidence and relevant project documentation before external
research. For current technical or vendor facts, prefer authoritative primary
sources and record enough source detail, version or date scope, findings, and
confidence for another reviewer to verify the conclusion. Do not treat research
permission as permission to modify the project, write to an external system,
access production or secrets, spend money, install software, execute downloaded
code, or perform a state-changing experiment. Ask for any separately required
permission at the point of action.

Research cannot substitute for a product, ownership, risk-acceptance, or other
project decision that only the user can make. After research, return to the
same evaluation. If the evidence resolves the issue and the resulting path is
sufficiently specified, evaluate that path. For implementation plans, otherwise
apply the plan-readiness policy above and preserve the remaining gap. For other
targets, report how the unresolved research limits the verdict.
## Choose the review interaction mode

Read `Review questions` from `.grump` when present:

- `interactive` means pause after the initial evidence pass for material review
  questions.
- `non-interactive` means complete the review without pausing and report
  unanswered material questions under `Evidence gaps`.
- absent or `unresolved` defaults to `interactive`.

A current explicit user instruction overrides the stored mode for the current
evaluation without rewriting `.grump`. This mode controls substantive review
questions only. It does not suppress required safety confirmations, host
approvals, clarification needed to identify the review target, or the
post-review plan-rules offer when the target is an implementation plan.
## Deduplicate and ask review questions

Collect potential questions from the core review and every active installed
specialist before asking the user. Deduplicate them by the underlying decision, missing
evidence, or requirement they address, not merely by wording. Merge overlapping
questions into one question that names every affected area.

Do not ask for information already answered by the review target, agent context,
`.grump`, repository evidence, or an earlier user answer. Do not repeat a
question the user deferred or declined unless new evidence materially changes
why the answer is needed. Never require or manufacture a question.

In interactive mode, finish the initial evidence pass before asking anything.
Assign every question an `RQ###` identifier, beginning with `RQ001` for each
evaluation, including when asking only one question. Ask the smallest useful
batch and wait for the answer. If an answer exposes a new material uncertainty,
ask a follow-up only when it can change the verdict, severity, or required
action. If the user defers, declines, or says to proceed, do not repeat the
question; finish non-interactively and state the evidence limit.

In non-interactive mode, do not pause. List each material unanswered question
under `Evidence gaps` and state which conclusion it could change. A complete
A complete review can finish with zero questions in either mode.

Survey questions use a separate continuous `Q###` sequence. Review `RQ###`
identifiers are scoped to one evaluation. Use the evaluation's ISO 8601 UTC time
when preserving them in an authorized plan addendum.
## Offer durable doctrine promotion

Live review questions and answers are scoped to the current evaluation.
Do not write them to `.grump` merely because the user answered them.

When an answer appears to establish a durable project-wide constraint, accepted
tradeoff, decision, invariant, or resolution of a project unknown, and saving it
could materially improve future reviews, ask a separate numbered question if
the user has not already stated its scope:

```text
RQ###. Your answer appears to establish this project-wide knowledge:
<concise statement>. Should GrumpyDev treat it as durable project doctrine for
future reviews, or keep it scoped to this evaluation? Reply with
`project-wide` or `this review only`.
```

Do not ask this for temporary details, target-specific choices, or facts already
recorded as doctrine. `Project-wide` explicitly confirms scope but does not by
itself authorize a file write. Apply the `Confirmed doctrine updates` policy
below. `This review only`, deferred, or declined keeps the answer scoped to the
evaluation and any authorized plan addendum. Do not ask again without new
evidence that materially changes the apparent scope.
