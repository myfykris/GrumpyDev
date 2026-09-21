---
name: gd-message-queues
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review message-queue engineering work for delivery semantics, ordering, acknowledgement, idempotency, retries, dead letters, backpressure, and recovery."
---

# Message queues GrumpyDev review

## Quick checks

- Read topic and queue topology, keys, payload schemas, acknowledgements,
  visibility or leases, retries, retention, dead letters, quotas, and
  dashboards.

- Trace publish failure, duplicate and out-of-order delivery, consumer crash,
  poison data, backlog growth, redrive, and broker outage.

Watch especially for acknowledgements before durable effects, visibility or
lease expiry during long work, redelivery treated as exceptional, poison
messages blocking a partition, global ordering assumed from partitioned systems,
reconnect storms, and producers outrunning consumer backpressure.

- Assess data loss, duplicate irreversible side effects, or an unbounded
  poison-message failure loop under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Message queues
specialist.

## Verdict context

State delivery and ordering guarantees, acknowledgement and idempotency
boundaries, backlog limits, retry policy, and recovery evidence.
