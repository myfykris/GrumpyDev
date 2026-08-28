# Survey routing behavior

Expected behavior:

- `Grump this architecture plan` invokes the review skill, not the survey.
- Explicit setup, onboarding, re-survey, or doctrine-refresh requests invoke
  the survey.
- An initial survey asks the doctrine format preference as `Q001`, after the
  evidence pass and before every other presented question.
- A re-survey preserves an existing unambiguous format answer unless the user
  asks to revisit it.
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
- The survey attempts to determine the main project's purpose and goals from
  evidence and agent context before asking the user.
- When purpose and goals cannot be determined, the survey asks one numbered,
  explicitly optional question that permits a brief answer or a decline.
- Declining the purpose question leaves purpose and success conditions
  unresolved and does not block setup.
- The survey does not treat later plan-scoped `RQ###` answers as survey output.
