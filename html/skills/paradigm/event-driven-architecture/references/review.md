# Event-driven architecture standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when message roles are explicit and publication, handling, replay,
  and reconciliation are proven.
