# Plan execution guard behavior

Expected behavior:

- Deliver the completed review and verdict before offering the execution guard.
- Ask the execution-guard question with the next evaluation-scoped `RQ###`
  identifier after both interactive and non-interactive reviews.
- Make the question state that `yes` will add the rules directly to the reviewed
  plan.
- Treat `yes` as narrow permission to append one self-contained execution-rules
  section to that local plan, not as authorization to begin implementation.
- Put the rules inside the GrumpyDev addendum, preserve the plan's format and
  encoding, and do not create a duplicate section.
- Make the written rules tell future implementing agents to report unrelated
  leads, continue through immaterial details, and stop before material
  deviations until the user decides whether to amend and Grump the plan.
- Never promote the plan-specific choice to `.grump` doctrine.
- Leave the guard disabled after `no`, an ambiguous answer, a deferral, or a
  decline.
- Never treat a GrumpyDev verdict or enabled guard as permission to implement.
