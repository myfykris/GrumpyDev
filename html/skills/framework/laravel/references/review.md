# Laravel standard review

Apply this guidance alongside the core GrumpyDev review and the `php` skill. Add
the applicable storage, queue, cache, web-server, and deployment specialists for
the concrete drivers and runtime.

## Inspect evidence

- Read the Laravel and PHP constraints, Composer lockfile, bootstrap files,
  service providers, bindings, facades, configuration, environment mapping,
  routes, middleware, controllers, requests, policies, gates, models,
  migrations, factories, jobs, listeners, commands, scheduler, and tests.
- Establish whether the application uses conventional request workers, Octane or
  another long-running server, queue workers, Horizon, scheduled commands,
  broadcasting, events, notifications, filesystem disks, caches, sessions, and
  multiple database connections.
- Trace one affected request and asynchronous job through route binding,
  middleware, validation, authorization, container resolution, transactions,
  Eloquent, events, serialization, queueing, retries, response transformation,
  and error handling.
- Inspect generated and cached configuration, routes, events, views, services,
  packages, and deployment commands. Read the actual runtime configuration
  rather than treating `.env.example` as production evidence.
- Read migration and backfill code together with old and new application code,
  queue payloads, worker restart behavior, rollback procedure, and operational
  dashboards.

## Establish the operating model

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

## Challenge the reviewed work

### Recurring traps

Watch especially for mass assignment confused with authorization, N+1 query
regressions, queued models reconstructed with stale state, jobs dispatched
before commit, migration operations that lock large tables, and
configuration-cache behavior that differs from local execution.

## Verify the claims

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

## Ask when evidence is missing

- If a new binding or resident runtime is involved, ask what owns its lifetime,
  what state it retains, and how it resets between requests or jobs.
- If models, observers, events, jobs, or external effects interact, ask where
  the transaction commits and which work is synchronous, after commit, retried,
  unique, or idempotent.
- If a schema or data change is planned, ask how old and new code coexist, how
  the backfill resumes, which locks or scans occur, and what recovery remains
  possible after data changes.
## Calibrate findings

- Treat authorization bypass, cross-tenant leakage, unsafe mass assignment,
  injection, destructive migration loss, or irreversible duplicate external
  effects as critical.
- Treat hidden container lifetime, transaction, queue, cache, or mixed-version
  assumptions as required revisions when they can break a supported path.
- Do not condemn Eloquent, events, queues, facades, or caches categorically.
  Report the specific lifecycle or invariant failure and its evidence.
- Downgrade or omit findings when policies, constraints, transactions, query
  behavior, job idempotency, persistent-state reset, migration coexistence, and
  recovery are demonstrated by representative tests and operational evidence.

## Add to the verdict

State the Laravel and runtime targets, container and process lifetimes,
authorization boundary, Eloquent and transaction behavior, migration and
backfill safety, queue guarantees, cache and generated-artifact behavior,
deployment overlap, worker restart, rollback limits, and supporting evidence.
