# distributed-systems behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which partition, latency, consistency, and failure assumptions define the
  system's contract?
- Who owns retries, deduplication, reconciliation, leadership, and recovery
  after partial success?

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

- Domain boundary: Nodes, regions, failure
  domains, network assumptions, clocks, membership, quorum, consistency,
  partitions, reconciliation, rollout, and disaster recovery.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/partial-failure-retries-and-overload.md`

Positive trigger: the plan changes remote calls, timeouts, retries, hedging, backoff, circuit breaking, overload behavior, admission control, cancellation, uncertain outcomes, or dependency failure.

Expected behavior:

- Standard or deep mode loads `references/partial-failure-retries-and-overload.md`.
- The review applies the focused checks in `references/partial-failure-retries-and-overload.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/partial-failure-retries-and-overload.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/consistency-replication-and-caches.md`

Positive trigger: the plan changes replicated state, read or write consistency, quorum behavior, lag, failover, cache ownership, invalidation, leases, fencing, or stale data tolerance.

Expected behavior:

- Standard or deep mode loads `references/consistency-replication-and-caches.md`.
- The review applies the focused checks in `references/consistency-replication-and-caches.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/consistency-replication-and-caches.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/messaging-ordering-and-reconciliation.md`

Positive trigger: the plan changes events, queues, delivery guarantees, ordering, deduplication, idempotency, outboxes, sagas, compensation, reconciliation, replay, or poison work.

Expected behavior:

- Standard or deep mode loads `references/messaging-ordering-and-reconciliation.md`.
- The review applies the focused checks in `references/messaging-ordering-and-reconciliation.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/messaging-ordering-and-reconciliation.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/coordination-clocks-and-leadership.md`

Positive trigger: the plan changes locks, leader election, consensus, coordination services, logical or wall clocks, time-based correctness, split-brain prevention, or ownership transfer.

Expected behavior:

- Standard or deep mode loads `references/coordination-clocks-and-leadership.md`.
- The review applies the focused checks in `references/coordination-clocks-and-leadership.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/coordination-clocks-and-leadership.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/evolution-operations-and-recovery.md`

Positive trigger: the plan changes protocols, schemas, rolling versions, topology, region or zone placement, data migration, observability, incident response, rollback, disaster recovery, or restoration.

Expected behavior:

- Standard or deep mode loads `references/evolution-operations-and-recovery.md`.
- The review applies the focused checks in `references/evolution-operations-and-recovery.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/evolution-operations-and-recovery.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
