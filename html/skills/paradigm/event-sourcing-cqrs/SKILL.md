---
name: gd-event-sourcing-cqrs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review event sourcing or CQRS engineering work for command invariants, read/write model separation, consistency, and, when events are authoritative, history, replay, and event evolution."
---

# Event sourcing and CQRS GrumpyDev review

## Quick checks

- Establish whether the project uses CQRS, event sourcing, or both. CQRS can
  use separate read and write models over one database without an event log.

- Trace commands, invariant enforcement, read models, and their consistency
  contract. Check synchronization and recovery when reads use a separate store.

- Only for event-sourced state, inspect event append guarantees, aggregate
  reconstruction, event evolution, replay, and snapshots if used.

Watch especially for duplicate commands, reads used beyond their freshness
contract, and unjustified storage or messaging infrastructure. With event
sourcing, also check rewritten history, replay repeating live side effects,
incompatible events, and deletion obligations with no workable policy.

- Assess unrebuildable history, conflicting aggregate writes, or a projection
  used beyond its consistency contract under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Event sourcing and
CQRS specialist.

## Verdict context

State which pattern is used, why it is justified, command and read guarantees,
and recovery costs. Include append and replay guarantees only for event-sourced
state; do not require an event store, snapshots, or replay for CQRS alone.
