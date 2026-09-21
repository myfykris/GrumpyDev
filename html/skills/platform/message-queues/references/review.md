# Message queues full-review guidance

## Operating conditions

Establish the project target: Broker and version, topology, delivery and
ordering guarantees, retention, retry and dead-letter policy, client libraries,
capacity, and disaster recovery. The changed boundary must define: Delivery,
ordering, acknowledgement, visibility, retries, deduplication, transactions,
backpressure, partitions, dead letters, retention, replay, and failover.

## Failure patterns

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

## Verification to run or specify in the plan

- Fail producers before and after business-state commit and consumers before
  and after each effect. Verify acknowledgement, retry and deduplication preserve
  the required outcome under ambiguous completion.
- Inject duplicate, reordered, delayed, oversized and poison messages; expire
  leases; remove partitions or brokers; grow backlog beyond normal retention;
  and exercise dead-letter and replay procedures.
- Run old and new producers and consumers together, then drain and roll back
  with messages in flight while verifying schema, ordering and idempotency.
