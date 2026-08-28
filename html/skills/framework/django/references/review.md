# Django standard review

## Establish the operating model

Establish the project target: Django and Python versions, WSGI or ASGI, server
and worker model, databases, caches, queues, storage, authentication, settings
environments, and migration process. The changed boundary must define: Settings
and app loading, middleware order, ORM and transactions, migrations, signals,
authentication, forms, async boundaries, caching, static media, jobs, and
deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Settings and app loading, middleware order, ORM and transactions, migrations,
signals, authentication. Prove forms, async boundaries, caching, static media,
jobs, deployment through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual Django lifecycle and production
  pipeline: Settings and app loading, middleware order, ORM and transactions,
  migrations, signals, authentication. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: forms, async boundaries, caching,
  static media, jobs, deployment. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Django, Python, database, application server, and deployment versions
  apply?
- How do middleware, transactions, migrations, authentication, async boundaries,
  caching, and background work interact?

## Calibrate findings

- Downgrade when framework-version-specific middleware, migration, transaction,
  and permission tests cover the change.
