# Survey routing behavior

Expected behavior:

- `Grump this architecture plan` invokes the review skill, not the survey.
- Explicit setup, onboarding, re-survey, or doctrine-refresh requests invoke
  the survey.
- The survey records the plan interaction preference in `.grump`.
- An initial survey always asks for the plan-readiness and research-execution
  policies and records both answers in `.grump`.
- A re-survey retains existing unambiguous policy answers unless the user asks
  to revisit them.
- Initial setup and explicit re-survey load applicable installed specialist
  `SURVEY.md` files after repository evidence is inspected.
- An ordinary plan review never loads a specialist `SURVEY.md`.
- Specialist candidates are deduplicated before receiving survey `Q###`
  identifiers, and evidence-resolved candidates are never asked.
- The survey does not treat later plan-scoped `RQ###` answers as survey output.
