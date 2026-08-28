# Ruby on Rails standard review

## Establish the operating model

Establish the project target: Rails and Ruby versions, web and job servers,
database, cache and queue adapters, autoload mode, asset stack, session store,
and deployment process. The changed boundary must define: Autoloading, Active
Record and transactions, callbacks, migrations, jobs, mailers, caching,
sessions, authorization, Hotwire, asset pipeline, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Autoloading, Active Record and transactions, callbacks, migrations, jobs,
mailers. Prove caching, sessions, authorization, Hotwire, asset pipeline,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Check N+1 queries, implicit saves, callbacks, validations, default scopes,
  association loading, transaction boundaries, and race conditions.
- Require expand, backfill, and contract migrations that tolerate old code, new
  code, and long-running workers.
- Define Active Job idempotency, retry and discard policy, uniqueness,
  transaction timing, and worker shutdown.
- Verify object-level authorization, CSRF, host and proxy settings, session
  behavior, upload handling, and secret redaction.
- Test eager loading, bootsnap and cache behavior, assets, database pools,
  process signals, and rolling deploys in production mode.

## Verify the claims

- Verify these behaviors through the actual Ruby on Rails lifecycle and
  production pipeline: Autoloading, Active Record and transactions, callbacks,
  migrations, jobs, mailers. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: caching, sessions, authorization,
  Hotwire, asset pipeline, deployment. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Ruby, Rails, database, job adapter, cache, and application-server
  versions apply?
- How do callbacks, validations, transactions, authorization, autoloading, jobs,
  and migrations interact?

## Calibrate findings

- Downgrade when ownership is explicit and request, job, transaction, and
  migration paths are feature-tested.
