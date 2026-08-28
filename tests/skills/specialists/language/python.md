# python behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which Python version and implementation, target platforms, dependency
  resolver, and packaging mode apply?
- How do async and sync work, cancellation, typing boundaries, serialization,
  resources, and process concurrency interact?

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

- Domain boundary: Interpreter and version, WSGI
  or ASGI or worker runtime, process and thread model, event loop, native
  wheels, OS and architecture, packaging, environment management, and shutdown.

Expected behavior:

- Include the unresolved domain facts in the same initial batch as the core
  profile confirmation.
- Record confirmed facts on the applicable `DEP-###` profile and reference a
  shared `INF-###` component when several profiles use it.
- Ask nothing from this contribution when repository evidence and the core
  profile already resolve every material fact.

## Focused-reference routing cases

### `references/async-processes-and-shutdown.md`

Positive trigger: the plan changes an event loop, async framework, threads, processes, executors, workers, GIL assumptions, task ownership, cancellation, signals, fork behavior, cleanup, retries, or graceful shutdown.

Expected behavior:

- Standard or deep mode loads `references/async-processes-and-shutdown.md`.
- The review applies the focused checks in `references/async-processes-and-shutdown.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/async-processes-and-shutdown.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/serialization-execution-and-filesystem-security.md`

Positive trigger: the plan handles untrusted pickle, marshal, shelve, YAML, dynamic import, eval, exec, templates, subprocesses, paths, symlinks, archives, decompression, XML, images, regexes, or other attacker-controlled parsing.

Expected behavior:

- Standard or deep mode loads `references/serialization-execution-and-filesystem-security.md`.
- The review applies the focused checks in `references/serialization-execution-and-filesystem-security.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/serialization-execution-and-filesystem-security.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/packaging-native-and-deployment.md`

Positive trigger: the plan changes interpreter implementation or version, packaging, lock or resolver tooling, imports, optional dependencies, virtual environments, generated files, native extensions, OS or architecture targets, build artifacts, or deployment environment behavior.

Expected behavior:

- Standard or deep mode loads `references/packaging-native-and-deployment.md`.
- The review applies the focused checks in `references/packaging-native-and-deployment.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/packaging-native-and-deployment.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
