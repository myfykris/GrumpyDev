# postgresql behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which PostgreSQL versions, table sizes, write rates, replication topology,
  and application-version overlap apply?
- What locks, rewrites, backfill, isolation, retry, and restore behavior
  applies to each changed invariant?

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

- Domain boundary: product and version,
  extensions, managed or self-hosted topology, replicas, pooling, storage,
  vacuum, migration, backup, restore, failover, and lag coverage.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/schema-migrations-and-locking.md`

Positive trigger: the plan changes DDL, constraints, indexes, defaults, generated values, types, partitions, extensions, table or index rewrites, lock acquisition, validation scans, timeouts, WAL volume, schema migration, backfills, coexistence, expand and contract sequencing, or irreversible data conversion.

Expected behavior:

- Standard or deep mode loads `references/schema-migrations-and-locking.md`.
- The review applies the focused checks in `references/schema-migrations-and-locking.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/schema-migrations-and-locking.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/transactions-and-concurrency.md`

Positive trigger: the plan changes transaction boundaries, isolation, read-modify-write invariants, constraints, row or advisory locks, leases, leader election, deadlock or serialization retries, multiple writers, outboxes, or non-transactional side effects.

Expected behavior:

- Standard or deep mode loads `references/transactions-and-concurrency.md`.
- The review applies the focused checks in `references/transactions-and-concurrency.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/transactions-and-concurrency.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/queries-and-indexes.md`

Positive trigger: the plan changes SQL queries, predicates, joins, ordering, pagination, indexes, selectivity, statistics, parameter-sensitive plans, collation, N+1 behavior, write amplification, or performance and capacity claims.

Expected behavior:

- Standard or deep mode loads `references/queries-and-indexes.md`.
- The review applies the focused checks in `references/queries-and-indexes.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/queries-and-indexes.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/operations-replication-and-recovery.md`

Positive trigger: the plan changes connection pools, pool modes, maintenance, vacuum, bloat, WAL, roles, row-level security, replicas, lag, read routing, failover, backup, retention, point-in-time recovery, restore, recovery objectives, or operator ownership.

Expected behavior:

- Standard or deep mode loads `references/operations-replication-and-recovery.md`.
- The review applies the focused checks in `references/operations-replication-and-recovery.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/operations-replication-and-recovery.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
