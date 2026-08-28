# Review target behavior

Expected behavior:

- `Grump this plan` evaluates proposal readiness, sequencing, dependencies,
  rollback, and execution boundaries. Plan-context warnings, authorized plan
  addenda, and the post-review execution-rules offer may apply.
- `Grump this architecture` evaluates responsibilities, interfaces, invariants,
  tradeoffs, failure domains, deployment, and operational consequences without
  requiring an implementation-plan structure.
- `Grump this project` evaluates the user-selected existing-system scope against
  repository behavior, project doctrine, documentation, operations, and
  accumulated risk without inventing a proposed plan.
- `Grump this diff` inspects the complete change and enough surrounding context
  to evaluate intent, regressions, compatibility, security, tests, deployment,
  and indirect effects.
- Another explicitly identified engineering artifact is evaluated against its
  stated purpose, claims, affected decisions, and available project evidence.
- Every active installed specialist participates for every target type and
  evaluates direct and indirect effects.
- Architecture, project, diff, and other non-plan reviews always return results
  in chat, do not use the plan-context warning, do not append a plan addendum,
  and do not offer plan execution rules.
- A non-plan target is never criticized merely for lacking plan formatting,
  sequencing, or plan-only metadata.
