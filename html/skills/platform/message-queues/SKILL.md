---
name: message-queues
description: Review message-queue plans for delivery semantics, ordering, acknowledgement, idempotency, retries, dead letters, backpressure, and recovery. Use when work or data crosses a broker, queue, stream, or pub-sub system.
---

# Message queues plan review

Apply this guidance alongside the core GrumpyDev review and the
`event-driven-architecture` or `background-jobs` skill.

## Inspect evidence

- Read topic and queue topology, keys, payload schemas, acknowledgements,
  visibility or leases, retries, retention, dead letters, quotas, and
  dashboards.
- Trace publish failure, duplicate and out-of-order delivery, consumer crash,
  poison data, backlog growth, redrive, and broker outage.

## Establish the operating model

Establish the project target: Broker and version, topology, delivery and
ordering guarantees, retention, retry and dead-letter policy, client libraries,
capacity, and disaster recovery. The changed boundary must define: Delivery,
ordering, acknowledgement, visibility, retries, deduplication, transactions,
backpressure, partitions, dead letters, retention, replay, and failover.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Delivery, ordering, acknowledgement, visibility,
retries, deduplication, transactions. Prove backpressure, partitions, dead
letters, retention, replay, failover through rotation, overload, partial
rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for acknowledgements before durable effects, visibility or
lease expiry during long work, redelivery treated as exceptional, poison
messages blocking a partition, global ordering assumed from partitioned systems,
reconnect storms, and producers outrunning consumer backpressure.

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

- Verify these behaviors through the effective Message queues configuration and
  runtime topology: Delivery, ordering, acknowledgement, visibility, retries,
  deduplication, transactions. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: backpressure, partitions, dead
  letters, retention, replay, failover. Exercise startup, readiness, normal
  load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which broker and delivery, ordering, acknowledgement, retention, and redrive
  guarantees actually apply?
- What makes duplicate, delayed, reordered, poison, or permanently failed
  messages safe and recoverable?

## Calibrate findings

- Treat data loss, duplicate irreversible side effects, or an unbounded
  poison-message failure loop as critical.
- Downgrade when the workload tolerates the broker's real semantics and redrive
  plus reconciliation are proven.

## Add to the verdict

State delivery and ordering guarantees, acknowledgement and idempotency
boundaries, backlog limits, retry policy, and recovery evidence.
