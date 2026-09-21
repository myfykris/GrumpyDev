# Event-driven architecture full-review guidance

## Operating conditions

Establish the project target: Brokers, delivery and ordering guarantees, event
ownership, schema governance, retention and replay, consumer topology, and
failure handling. The changed boundary must define: Event ownership,
notification versus fact semantics, ordering, delivery, schemas, idempotency,
consumers, dead letters, replay, observability, and evolution.

## Failure patterns

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

## Verification to run or specify in the plan

- Interrupt publication between database commit and broker acknowledgement,
  then replay the resulting messages. Verify state and events reconcile and
  duplicate delivery cannot repeat an irreversible effect.
- Run old and new producers and consumers with reordered messages and poison
  records. Check schema compatibility, dead-letter recovery, and replay from
  retained history without bypassing authorization.
