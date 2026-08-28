# php behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which PHP version, SAPI, web server, extensions, error settings, and
  dependency versions apply?
- How do types, request state, sessions, serialization, resources, errors, and
  untrusted input cross the boundary?

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

- Domain boundary: PHP version, SAPI, mod_php, FastCGI, PHP-FPM, worker, INI,
  proxy, session, cache,
  OPcache, rollout, and rollback coverage. Map the answers into named profiles.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/types-and-boundary-data.md`

Positive trigger: the plan changes weak or strict scalar coercion, union or nullable types, array shapes, numeric strings, truthiness, JSON conversion, reflection, magic access, encoding, locale, or data entering from requests, storage, queues, or environment.

Expected behavior:

- Standard or deep mode loads `references/types-and-boundary-data.md`.
- The review applies the focused checks in `references/types-and-boundary-data.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/types-and-boundary-data.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/request-and-process-lifecycle.md`

Positive trigger: the plan depends on a SAPI, PHP-FPM, mod_php, CGI or FastCGI, request metadata, server variables, proxy mapping, long-running workers, resident application servers, persistent connections, output buffering, streaming, signals, shutdown, cancellation, or process recycling.

Expected behavior:

- Standard or deep mode loads `references/request-and-process-lifecycle.md`.
- The review applies the focused checks in `references/request-and-process-lifecycle.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/request-and-process-lifecycle.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/security-and-external-input.md`

Positive trigger: the plan handles uploads, paths, stream wrappers, sessions, cookies, untrusted serialization, HTML or other output contexts, SQL or shell boundaries, temporary files, client-visible errors, or security-sensitive logging.

Expected behavior:

- Standard or deep mode loads `references/security-and-external-input.md`.
- The review applies the focused checks in `references/security-and-external-input.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/security-and-external-input.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/dependencies-and-deployment.md`

Positive trigger: the plan changes PHP or extension versions, Composer resolution, plugins or scripts, classmaps, OPcache, preloading, generated framework artifacts, rolling releases, migrations, cache or queue payload compatibility, worker draining, restart, rollback, or recovery.

Expected behavior:

- Standard or deep mode loads `references/dependencies-and-deployment.md`.
- The review applies the focused checks in `references/dependencies-and-deployment.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/dependencies-and-deployment.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
