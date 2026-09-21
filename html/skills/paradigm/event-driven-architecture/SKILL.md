---
name: gd-event-driven-architecture
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review event-driven architecture engineering work for event contracts, delivery semantics, ordering, idempotency, replay, coupling, and operational recovery."
---

# Event-driven architecture GrumpyDev review

## Quick checks

- Read event schemas, producers, consumers, brokers, delivery settings, retry
  and dead-letter policy, replay tooling, and ownership.

- Trace creation, publication, duplication, reordering, consumption, failure,
  redrive, and retirement of each event type.

Watch especially for exactly-once claims built on at-least-once components,
database and event dual writes, out-of-order or duplicate delivery, poison
events, consumers with non-idempotent side effects, schema changes that strand
old consumers, and replay that recontacts external systems.

- Assess ambiguous command ownership, lost committed events, or duplicate
  irreversible effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Event-driven
architecture specialist.

## Verdict context

State event ownership, delivery and ordering guarantees, publication atomicity,
replay policy, and recovery evidence.
