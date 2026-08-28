# laravel behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which PHP, Laravel, database, queue, cache, and runtime versions or drivers
  apply?
- How do validation, authorization, model events, transactions, jobs, retries,
  and migrations interact?

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

- Domain boundary: PHP
  SAPI, server, FPM or Octane, queues, scheduler, sessions, cache, files,
  database, proxy, config cache, rollout, and worker restart coverage.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/http-validation-and-authorization.md`

Positive trigger: the plan changes routes, middleware, request validation, route model binding, guards, providers, policies, gates, CSRF, signed URLs, rate limits, trusted proxies, API resources, JSON output, pagination, or HTTP error behavior.

Expected behavior:

- Standard or deep mode loads `references/http-validation-and-authorization.md`.
- The review applies the focused checks in `references/http-validation-and-authorization.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/http-validation-and-authorization.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/eloquent-transactions-and-migrations.md`

Positive trigger: the plan changes Eloquent models, relationships, scopes, casts, observers, bulk updates, constraints, transactions, locking, database connections, schema, indexes, backfills, or mixed-version data behavior.

Expected behavior:

- Standard or deep mode loads `references/eloquent-transactions-and-migrations.md`.
- The review applies the focused checks in `references/eloquent-transactions-and-migrations.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/eloquent-transactions-and-migrations.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/queues-events-and-workers.md`

Positive trigger: the plan changes queued jobs, events, listeners, notifications, Horizon, scheduler behavior, retry, uniqueness, ordering, idempotency, worker termination, Octane, or another resident process.

Expected behavior:

- Standard or deep mode loads `references/queues-events-and-workers.md`.
- The review applies the focused checks in `references/queues-events-and-workers.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/queues-events-and-workers.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/caching-configuration-and-deployment.md`

Positive trigger: the plan changes cache keys, invalidation, sessions, generated configuration, route or view caches, maintenance mode, release artifacts, storage links, OPcache, worker restarts, health checks, rollback, or deployment sequencing.

Expected behavior:

- Standard or deep mode loads `references/caching-configuration-and-deployment.md`.
- The review applies the focused checks in `references/caching-configuration-and-deployment.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/caching-configuration-and-deployment.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
