---
name: laravel
description: Review Laravel plans for service-container scope, Eloquent behavior, migrations, queues, events, authorization, caching, and deployment risks. Use when a PHP plan changes Laravel applications, models, controllers, jobs, listeners, or operations.
---

# Laravel plan review

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

## Challenge the plan

### Recurring traps

Watch especially for mass assignment confused with authorization, N+1 query
regressions, queued models reconstructed with stale state, jobs dispatched
before commit, migration operations that lock large tables, and
configuration-cache behavior that differs from local execution.

### HTTP, validation, and authorization

- Require input validation at the request boundary and domain invariants at the
  operation that changes state. Form requests and DTOs do not replace
  authorization or database constraints.
- Verify middleware ordering, route model binding, implicit scoping, guard and
  provider selection, authentication state, CSRF behavior, signed URLs, rate
  limits, and trusted proxy configuration for the actual route group.
- Require policies, gates, or an equivalent explicit authorization decision for
  the specific object and action. Hidden fields, route middleware, tenant query
  scopes, and controller placement are not sufficient authorization by
  themselves.
- Check API resources, JSON serialization, appended attributes, relations,
  visibility, pagination, and error responses for accidental data exposure or
  unstable contracts.

### Eloquent, transactions, and migrations

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

### Queues, events, and long-running processes

- Treat every queued job as repeatable unless the selected queue proves a
  stronger guarantee. Define idempotency at the side effect, not just a unique
  dispatch check.
- Check dispatch-before-commit, after-commit configuration, model identifier
  serialization, relation loading, deleted records, tenant context, encrypted
  payloads, code-version overlap, retry delay, timeout, and worker termination.
- Separate events that announce a committed fact from commands that request an
  effect. Retrying a listener can duplicate email, billing, file, or external
  API effects even if the database update is transactional.
- Define scheduler overlap, single-server locks, clock and timezone behavior,
  missed runs, manual replay, and long-running command failure.
- For Octane or other resident runtimes, require reset of request-scoped state,
  locale, tenant, authentication, static caches, singletons, database sessions,
  and third-party client state. Confirm package compatibility with the runtime.

### Caches, configuration, and deployment

- Check cache key ownership, tenant separation, serialization compatibility,
  TTL, invalidation, stampede behavior, tags, locks, and degraded operation when
  the cache is unavailable.
- Verify configuration, route, event, view, package, and service caches against
  the deployment artifact. Runtime environment changes do not necessarily alter
  an already generated configuration cache.
- Coordinate maintenance mode, health checks, symlink or immutable releases,
  static assets, storage links, migrations, queue draining, worker restarts,
  Octane reload, OPcache, scheduler ownership, and rollback.
- Reject rollback claims that ignore destructive migrations, incompatible job
  payloads, new cache formats, or external effects.

## Verify the claims

- Use feature tests that cross real middleware, route binding, validation,
  authorization, container, database, event, and serialization boundaries. Unit
  tests around controller methods do not prove the framework pipeline.
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

- If framework behavior or package compatibility is version-sensitive, ask which
  Laravel, PHP, database, queue, cache, session, and runtime versions or drivers
  execute the affected paths.
- If a new binding or resident runtime is involved, ask what owns its lifetime,
  what state it retains, and how it resets between requests or jobs.
- If models, observers, events, jobs, or external effects interact, ask where
  the transaction commits and which work is synchronous, after commit, retried,
  unique, or idempotent.
- If a schema or data change is planned, ask how old and new code coexist, how
  the backfill resumes, which locks or scans occur, and what recovery remains
  possible after data changes.
- If deployment caches or workers are affected, ask which artifacts are built,
  when workers drain and restart, and what rollback does with queued payloads
  and persisted formats.

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
