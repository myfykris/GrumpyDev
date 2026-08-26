# Message queues survey contribution

## Applicability

Apply this contribution when work or data crosses a broker, queue, stream, or
pub-sub system. Skip it when Message queues does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Message queues, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Broker and version, topology, delivery and
  ordering guarantees, retention, retry and dead-letter policy, client
  libraries, capacity, and disaster recovery.
- Review doctrine for: Delivery, ordering, acknowledgement, visibility, retries,
  deduplication, transactions, backpressure, partitions, dead letters,
  retention, replay, and failover.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Product and version, topology, partitions,
  ordering, acknowledgement, visibility, retention, dead letters, security,
  producer and consumer regions, scaling, and failover.

## Ask only when materially unresolved

- Which broker and delivery, ordering, acknowledgement, retention, and redrive
  guarantees actually apply?
- What makes duplicate, delayed, reordered, poison, or permanently failed
  messages safe and recoverable?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Product and version, topology,
  partitions, ordering, acknowledgement, visibility, retention, dead letters,
  security, producer and consumer regions, scaling, and failover? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Message queues answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Message queues deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Message
queues doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Message queues when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
