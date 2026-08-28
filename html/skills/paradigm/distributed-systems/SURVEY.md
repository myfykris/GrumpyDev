# Distributed systems survey contribution

## Applicability

Apply this contribution when correctness or availability crosses independently failing
processes, services, machines, regions, or external authorities. A small application
with a database, queue, cache, or remote API can qualify. Combine it with protocol,
messaging, storage, security, observability, and platform contributions. Deduplicate the
concrete technology questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect architecture and data-flow documents, service and schema definitions,
API or event contracts, deployment topology, timeout and retry configuration,
incident runbooks, service objectives, and relevant code. Identify observed
behavior separately from aspirational diagrams. Do not trigger failures or
access production systems merely to complete setup.

## Durable project facts

Collect stable distributed-system doctrine that should guide many reviews:

- Service, team, and data ownership boundaries, including the system of record
  for important entities and decisions.
- Required business invariants and standard consistency or staleness promises
  for user-visible reads, writes, and asynchronous work.
- Supported regions and failure domains, partition and degraded-mode policy, and
  availability versus consistency priorities for critical operations.
- Standard timeout-budget, retry, backoff, jitter, circuit, admission-control,
  and backpressure conventions plus ownership of retries at each layer.
- Idempotency identity, retention, and duplicate-handling conventions for APIs,
  jobs, messages, and external effects.
- Message delivery and ordering assumptions, outbox/inbox patterns, poison-work
  policy, replay authority, and schema-evolution rules.
- Reconciliation expectations, owners, evidence of completion, and escalation
  when automatic repair cannot restore an invariant.
- Coordination conventions for leases, leadership, distributed locks, quorum,
  fencing, and clock use.
- Observability correlation, service objectives, fault-injection practice,
  disaster-recovery ownership, and authority to enter and exit degraded modes.
- Deployment-profile guidance: Nodes, regions, failure domains, network
  assumptions, clocks, membership, quorum, consistency, partitions,
  reconciliation, rollout, and disaster recovery.

## Ask only when materially unresolved

Ask only when a missing project-wide fact will repeatedly affect evaluations.
Useful gaps include authoritative ownership, permitted staleness, partition
policy, standard retry owner, idempotency convention, delivery assumptions,
reconciliation ownership, fencing requirements, or recovery authority. Let the
combined survey assign sequential question numbers after deduplication.

Keep operation-specific failure traces, exact timeout values, message keys,
compensations, and rollout questions in the live evaluation unless they express
a durable cross-project convention.
- Align existing domain questions with this deployment guidance when it is
  material: Nodes, regions, failure domains, network assumptions, clocks,
  membership, quorum, consistency, partitions, reconciliation, rollout, and
  disaster recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record confirmed doctrine under architecture, data, runtime, deployment,
verification, and operational conventions. Preserve important distinctions, such
as "at least once with idempotent consumers" instead of flattening them to
"reliable messaging." Attribute decisions to evidence or the user where useful.
Record material unknowns explicitly and mark the contribution current only after
relevant durable questions are resolved or deliberately deferred.

Map existing Distributed systems survey answers to the affected `DEP-###`
profile. Reference a shared `INF-###` component rather than copying its common
contract. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Do not record credentials, private endpoints, sensitive topology details,
production payloads, live incident data, transient replica identities, or a raw
Q&A transcript. Do not invent guarantees from product marketing or framework
defaults. Do not ask the same ownership, retry, or recovery question already
answered by a companion contribution.

## Re-survey triggers

Re-survey after material service or data-ownership changes, new regions or
failure domains, consistency-contract changes, introduction or replacement of
queues/caches/replication, retry or idempotency policy changes, coordination or
leader-election changes, new degraded modes, observability redesign, or major
disaster-recovery changes.
