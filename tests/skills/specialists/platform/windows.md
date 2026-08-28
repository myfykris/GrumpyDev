# windows behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not establish the
relevant Processes, services, identity, ACLs, registry, filesystems, COM and
WinRT, application identity, packaging, activation, architecture, updates,
logging, crash handling, and recovery.

Expected behavior:

- Inspect `.grump`, the plan, repository, documentation, configuration, and
  agent context before asking anything.
- Ask only unresolved questions that can change the verdict, severity, or
  required action; do not impose a question count.
- Apply the specialist's domain-specific failure and severity conditions.

## Resolved-evidence case

Review the same plan after evidence establishes the target Windows versions and
editions, architectures, app model, packaging and identity, installer or store
channel, service use, privilege requirements, signing, and update policy, plus
the plan-specific lifecycle, compatibility, deployment, and recovery behavior.

Expected behavior:

- Ask zero questions that the supplied evidence already answers.
- Downgrade or omit findings invalidated by target-specific evidence.
- Retain only findings tied to a demonstrated requirement, invariant, failure
  mode, or unsupported claim.

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

- Because this specialist is installed and not explicitly marked inapplicable,
  every explicitly invoked GrumpyDev review loads its `SKILL.md`, even when the
  reviewed work does not name or modify this domain.
- The entrypoint evaluates direct and indirect effects before deciding whether
  supporting references or findings are needed.
- When no material effect exists, the specialist produces no finding.
- Lean mode loads this specialist's `SKILL.md` and saved doctrine without
  loading `references/review.md` unless an entrypoint escalation trigger
  applies.
- Standard mode loads `SKILL.md` and loads `references/review.md` only when
  the entrypoint identifies a plausible direct or indirect material effect.
- Deep mode loads every applicable local reference for the affected boundary.
- No ordinary review loads this specialist's `SURVEY.md`.
- Ask a review-scoped question only if a material decision remains unresolved
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

- Domain boundary: versions and
  editions, architecture, app model, service or desktop session, identity,
  ACLs, filesystem, registry, packaging, signing, updates, logging, and
  recovery.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/services-com-and-process-identity.md`

Positive trigger: the plan changes Windows services, service accounts, tokens, impersonation, privileges, sessions, job objects, child processes, UAC, COM, WinRT, apartment models, marshaling, registration, process boundaries, service recovery, or shutdown.

Expected behavior:

- Standard or deep mode loads `references/services-com-and-process-identity.md`.
- The review applies the focused checks in `references/services-com-and-process-identity.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/services-com-and-process-identity.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/packaging-signing-updates-and-recovery.md`

Positive trigger: the plan changes package identity, packaged or unpackaged execution, Store, installer, portable or managed distribution, architecture, runtime dependencies, activation, signing, repair, uninstall, per-user or per-machine scope, updates, locked files, migration, rollback, event logs, dumps, or offline recovery.

Expected behavior:

- Standard or deep mode loads `references/packaging-signing-updates-and-recovery.md`.
- The review applies the focused checks in `references/packaging-signing-updates-and-recovery.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/packaging-signing-updates-and-recovery.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
