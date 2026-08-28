# Message queues standard review

## Establish the operating model

Establish the project target: Broker and version, topology, delivery and
ordering guarantees, retention, retry and dead-letter policy, client libraries,
capacity, and disaster recovery. The changed boundary must define: Delivery,
ordering, acknowledgement, visibility, retries, deduplication, transactions,
backpressure, partitions, dead letters, retention, replay, and failover.

Identify the producer commit boundary, broker authority, partition or ordering
key, acknowledgement and lease rule, retry and deduplication owner, consumer
effect boundary, dead-letter policy, retention, replay authority, and operator
repair path. Prove duplicate, delayed, reordered and poison messages plus
partition loss, consumer termination and backlog growth preserve the required
business invariants.

## Challenge the reviewed work

### Recurring traps

- State delivery and ordering scope in broker-specific terms; marketing labels
  do not define end-to-end effects.
- Acknowledge only after required effects are durable, and make repeats safe at
  the actual side-effect boundary.
- Bound payload size, retention, partition skew, consumer concurrency, in-flight
  work, and backlog age.
- Separate transient retries from permanent failure, prevent retry storms, and
  make dead-letter ownership and redrive explicit.
- Prove producer backpressure, broker failover, consumer rebalancing, schema
  evolution, and replay without corrupting downstream state.

## Verify the claims

- Fail producers before and after business-state commit and consumers before
  and after each effect. Verify acknowledgement, retry and deduplication preserve
  the required outcome under ambiguous completion.
- Inject duplicate, reordered, delayed, oversized and poison messages; expire
  leases; remove partitions or brokers; grow backlog beyond normal retention;
  and exercise dead-letter and replay procedures.
- Run old and new producers and consumers together, then drain and roll back
  with messages in flight while verifying schema, ordering and idempotency.

## Ask when evidence is missing

- Which broker and delivery, ordering, acknowledgement, retention, and redrive
  guarantees actually apply?
- What makes duplicate, delayed, reordered, poison, or permanently failed
  messages safe and recoverable?

## Calibrate findings

- Downgrade when the workload tolerates the broker's real semantics and redrive
  plus reconciliation are proven.
