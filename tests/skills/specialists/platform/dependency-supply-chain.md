# dependency-supply-chain behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- What canonical source, publisher, exact resolved version, and lockfile
  identify each new dependency?
- Which install scripts, build plugins, generated artifacts, licenses, and
  transitive updates enter the build boundary, inventory, and vulnerability
  response process?

Expected behavior:

- Ask only the unresolved questions that can change the verdict, severity, or
  required action.
- Apply the skill's domain-specific critical and lower-severity conditions.

## Resolved-evidence case

Review the same plan after repository evidence or explicit plan content
resolves the material decisions.

Expected behavior:

- Ask zero questions that the evidence already answers.
- Downgrade or omit findings that the supplied evidence invalidates.

## Deployed-inventory case

Review a plan that points to a lockfile as complete supply-chain proof but does
not identify bundled, generated, native, image, build-tool, or deployed
transitive components and has no owner for an end-of-life dependency.

Expected behavior:

- Reject the lockfile as provenance or deployed inventory by itself.
- Require an artifact-linked software bill of materials, source and publisher
  identity, patch ownership, exploitation and reachability triage, exception
  expiry, and an exit path for the unsupported component.
- Require verified provenance or signatures only where the ecosystem supports
  them and where they change the actual artifact trust decision.

## Evidence-resolved survey case

Run initial setup or an explicit re-survey after `.grump`, repository evidence,
and project documentation already establish every applicable durable fact for
this specialist.

Expected behavior:

- Load this specialist's `SURVEY.md` because this is a survey operation.
- Ask zero questions whose decisions are already supported by current evidence.
- Preserve concise doctrine with useful evidence references and mark the
  specialist survey contribution current.

## Material survey-gap case

Run initial setup or an explicit re-survey when inspection leaves one durable
project fact unresolved and that fact will materially change future reviews in
this domain.

Expected behavior:

- Ask only the unresolved durable question after pooling and deduplicating all
  applicable specialist contributions.
- Let the survey orchestrator assign its sequential question identifier; do not
  obtain a fixed identifier from `SURVEY.md`.
- Record the confirmed answer as project doctrine or record a deliberate
  deferral as unresolved without inventing a default.

## Ordinary-review loading case

Run an ordinary Grump review after setup has saved the project's durable domain
context in `.grump`.

Expected behavior:

- Load this specialist's `SKILL.md` and the saved `.grump` doctrine.
- Do not load this specialist's `SURVEY.md` during the ordinary review.
- Ask a plan-scoped question only if a material decision remains unresolved
  after inspecting the plan, repository, documentation, and agent context.

## Companion-overlap case

Run setup with this specialist and a companion specialist whose survey proposes
the same underlying version, runtime, ownership, deployment, or recovery
decision using different wording.

Expected behavior:

- Pool both contributions before numbering questions.
- Ask one combined question for the shared decision rather than one question
  per file, while retaining any genuinely distinct domain choices.
- Record one coherent project fact in `.grump` and mark both contributions
  appropriately.

## Infrastructure-profile case

Run initial setup or an explicit re-survey with an applicable execution profile
and this domain boundary:

- Domain boundary: Build hosts, package sources,
  network access, install scripts, native toolchains, artifact promotion,
  dependency caches, signing authority if applicable, and emergency rebuild.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.
