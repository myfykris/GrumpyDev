---
name: event-driven-architecture
description: Review event-driven architecture plans for event contracts, delivery semantics, ordering, idempotency, replay, coupling, and operational recovery. Use when services communicate or trigger work through events or messages.
---

# Event-driven architecture plan review

Apply this guidance alongside the core GrumpyDev review and the `message-queues`
and `schema-evolution` skills.

## Inspect evidence

- Read event schemas, producers, consumers, brokers, delivery settings, retry
  and dead-letter policy, replay tooling, and ownership.
- Trace creation, publication, duplication, reordering, consumption, failure,
  redrive, and retirement of each event type.

## Establish the operating model

Establish the project target: Brokers, delivery and ordering guarantees, event
ownership, schema governance, retention and replay, consumer topology, and
failure handling. The changed boundary must define: Event ownership,
notification versus fact semantics, ordering, delivery, schemas, idempotency,
consumers, dead letters, replay, observability, and evolution.

Name the invariants, authorities, owners, and enforcement for Event ownership,
notification versus fact semantics, ordering, delivery, schemas, idempotency.
Prove consumers, dead letters, replay, observability, evolution under
concurrency, partial failure, incompatible versions, operational response,
rollback, and repair, and justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for exactly-once claims built on at-least-once components,
database and event dual writes, out-of-order or duplicate delivery, poison
events, consumers with non-idempotent side effects, schema changes that strand
old consumers, and replay that recontacts external systems.

- Classify every message as an event, command, or data stream. Require events to
  describe completed facts with stable identity and ownership.
- Allow intentional commands only with one logical owner, targeted routing,
  explicit acknowledgement, duplicate handling, and failure semantics. Reject
  command-shaped broadcasts with ambiguous ownership.
- Define delivery and ordering scope precisely, then require consumers to
  tolerate everything the broker can actually do.
- Check transactional publication or outbox behavior so state cannot commit
  without its event, or vice versa.
- Require backward-compatible evolution and mixed-version evidence for
  producers, consumers, and replayed history.
- Expose hidden temporal coupling, fan-out cost, poison messages, and recovery
  ownership before approving asynchronous indirection.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Event ownership, notification versus fact semantics, ordering,
  delivery, schemas, idempotency. Use dependency, architecture, contract,
  schema, or ownership tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: consumers, dead letters, replay,
  observability, evolution. Exercise the material invariant under concurrency,
  delay, duplication, partial failure, incompatible versions, rollback, and
  repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Is each message an event, command, or data stream, and who owns its meaning
  and handling?
- What delivery, ordering, acknowledgement, duplication, evolution, replay, and
  recovery semantics apply?

## Calibrate findings

- Treat ambiguous command ownership, lost committed events, or duplicate
  irreversible effects as critical.
- Downgrade when message roles are explicit and publication, handling, replay,
  and reconciliation are proven.

## Add to the verdict

State event ownership, delivery and ordering guarantees, publication atomicity,
replay policy, and recovery evidence.
