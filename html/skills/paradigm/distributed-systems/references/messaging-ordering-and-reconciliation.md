# Distributed messaging, ordering, and reconciliation

Read this reference when the reviewed work directly or indirectly changes events,
queues, delivery guarantees, ordering,
deduplication, idempotency, outboxes, sagas, compensation, reconciliation, replay, or
poison work.

## Ordering, messages, and reconciliation

- Define the smallest ordering scope the invariant needs. Global ordering is
  expensive and often unnecessary, while partition ordering may not survive key
  changes, retries, or producer concurrency.
- Assume at-least-once processing unless stronger end-to-end evidence exists.
  Broker deduplication alone does not make database or external side effects
  exactly once.
- Coordinate state and message publication with an outbox, log, change stream,
  or other proven boundary. Analyze the inverse inbox/deduplication problem at
  consumers.
- Make consumers restartable and idempotent. Define poison-message quarantine,
  schema compatibility, replay limits, and what happens when an old message
  arrives after newer state.
- Require reconciliation for any state that can diverge. Define comparison
  source, scan or event trigger, safe repair, rate limit, observability,
  ownership, and completion evidence.
