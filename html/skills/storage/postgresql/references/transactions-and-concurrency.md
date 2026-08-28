# PostgreSQL transactions and concurrency

Read this reference when the reviewed work directly or indirectly changes transaction
boundaries, isolation, read-modify-write invariants, constraints, row or advisory
locks, leases, leader election,
deadlock or serialization retries, multiple writers, outboxes, or non-transactional side
effects.

## Transactions and concurrency

- Prove that transaction boundaries cover the invariant. Framework helpers can
  accidentally perform work outside the transaction or hold transactions open
  across remote calls.
- Analyze isolation behavior, predicate races, lost updates, write skew,
  deadlocks, serialization failures, uniqueness conflicts, and retry safety. A
  transaction alone does not serialize a read-modify-write sequence.
- Prefer database constraints for invariants that must survive concurrency and
  multiple writers. If application code owns an invariant, identify every writer
  and explain why database enforcement is impractical.
- When using row locks, advisory locks, leases, queues, or leader election,
  specify lock identity, acquisition order, timeout, disconnect behavior, and
  fencing against a stale owner.
- Retried transactions must repeat the complete decision from fresh reads and
  must not duplicate non-transactional side effects such as messages, files, or
  external calls. Require an outbox or equivalent boundary when needed.
