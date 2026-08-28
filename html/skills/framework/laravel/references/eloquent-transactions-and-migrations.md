# Laravel Eloquent, transactions, and migrations

Read this reference when the reviewed work directly or indirectly changes Eloquent
models, relationships, scopes, casts,
observers, bulk updates, constraints, transactions, locking, database connections,
schema, indexes, backfills, or mixed-version data behavior.

## Eloquent, transactions, and migrations

- Trace mass assignment, casts, accessors, mutators, observers, boot hooks,
  global scopes, soft deletes, touch behavior, lazy loading, N+1 queries, and
  model serialization. Bulk query updates can bypass model events and casts.
- Require database constraints for invariants that must survive concurrency,
  alternate writers, imports, jobs, or future code paths. An application check
  before insert does not prevent a race.
- Check transaction nesting, multiple connections, external side effects,
  deadlock retries, pessimistic or optimistic locking, and what an observer or
  event can see before commit.
- Require expand, migrate, and contract sequencing when old and new code can
  overlap. Analyze lock, rewrite, scan, backfill, default, nullability, index,
  foreign-key, and rollback behavior using the selected database specialist.
- Make backfills bounded, observable, restartable, idempotent, and compatible
  with concurrent writes. A migration process is a poor unbounded job runner.

## Ask when evidence is missing

- If framework behavior or package compatibility is version-sensitive, ask which
  Laravel, PHP, database, queue, cache, session, and runtime versions or drivers
  execute the affected paths.
