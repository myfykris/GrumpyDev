# Ruby on Rails full-review guidance

## Operating conditions

Establish the project target: Rails and Ruby versions, web and job servers,
database, cache and queue adapters, autoload mode, asset stack, session store,
and deployment process. The changed boundary must define: Autoloading, Active
Record and transactions, callbacks, migrations, jobs, mailers, caching,
sessions, authorization, Hotwire, asset pipeline, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Run competing Active Record writes and fail callbacks or transactions before
  commit. Retry affected jobs and verify external effects occur only once
  under the declared delivery contract.
- Rehearse migrations with old web and job workers still running. Boot
  production-mode artifacts and check eager loading, database pools, assets,
  session behavior, and worker draining.
