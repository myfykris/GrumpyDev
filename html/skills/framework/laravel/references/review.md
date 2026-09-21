# Laravel full-review guidance

## Operating conditions

- State Laravel, PHP, Composer package, database, cache, queue, session,
  filesystem, and web-server versions or drivers that affect the plan.
- Identify container lifetimes for every new binding. Distinguish transient,
  singleton, scoped, request, job, and application-server lifetimes. In a
  long-running server, a singleton can retain request or tenant data.
- Define the transaction boundary and database connection for each invariant.
  Model callbacks, observers, events, queued listeners, notifications, and jobs
  can run before commit, after commit, synchronously, or asynchronously
  depending on code and configuration.
- State the Eloquent loading, serialization, casting, timestamp, soft-delete,
  global-scope, mass-assignment, and relationship assumptions on the affected
  models.
- Identify queue delivery, retry, timeout, uniqueness, concurrency, failed-job,
  dead-letter, and ordering semantics for each affected job path.
- Define which caches and generated artifacts are shared, per-process,
  environment-specific, tagged, versioned, or safe to invalidate.

## Failure patterns

Watch especially for mass assignment confused with authorization, N+1 query
regressions, queued models reconstructed with stale state, jobs dispatched
before commit, migration operations that lock large tables, and
configuration-cache behavior that differs from local execution.

## Verification to run or specify in the plan

- Test unauthorized objects, alternate guards, tenant crossover, malformed
  input, concurrent writes, transaction rollback, observer failure, and bulk
  operations that bypass models.
- Run queue jobs repeatedly, concurrently, after timeout, after worker death,
  before and after deployment, and with the referenced model changed or deleted.
  Verify the external side effect as well as job status.
- Measure representative Eloquent queries and query plans. Assert query count or
  loading behavior where N+1 regressions are costly.
- Rehearse migrations and backfills on representative scale while old and new
  code and workers remain active. Verify restart, drain, cache generation,
  health, rollback, and recovery.
- In resident runtimes, send distinct tenant and identity requests through the
  same process and verify state, locale, services, transactions, and logs reset.
