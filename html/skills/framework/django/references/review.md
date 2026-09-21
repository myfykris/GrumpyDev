# Django full-review guidance

## Operating conditions

Establish the project target: Django and Python versions, WSGI or ASGI, server
and worker model, databases, caches, queues, storage, authentication, settings
environments, and migration process. The changed boundary must define: Settings
and app loading, middleware order, ORM and transactions, migrations, signals,
authentication, forms, async boundaries, caching, static media, jobs, and
deployment.

## Failure patterns

- Analyze migration locks, defaults, backfills, old and new code overlap, and
  rollback instead of trusting generated migrations.
- Check N+1 queries, queryset evaluation, transaction scope, select-for-update
  use, uniqueness, and race conditions.
- Verify CSRF, host and proxy settings, object authorization, mass assignment,
  escaping, upload handling, and secret separation.
- Reject important business behavior hidden in signals without explicit
  ordering, idempotency, and failure handling.
- Test production settings, static and media handling, worker shutdown, cache
  invalidation, and mixed-version deployment.

## Verification to run or specify in the plan

- Run changed ORM flows against the actual database with concurrent writes and
  query-count checks. Rehearse migrations on representative data while old and
  new application versions overlap.
- Exercise object permissions, CSRF, proxy settings, and uploaded media under
  production settings. Force signal or transaction failure and verify deferred
  work does not act on rolled-back state.
