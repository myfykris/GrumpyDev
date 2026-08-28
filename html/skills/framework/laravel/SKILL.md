---
name: laravel
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Laravel plans and other engineering artifacts for service-container scope, Eloquent behavior, migrations, queues, events, authorization, caching, and deployment risks. Project applicability: the project uses or materially depends on Laravel."
---

# Laravel GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Coordinate findings with the active PHP, database, queue, cache, web-server,
and deployment specialists for the configured drivers and runtime.

## Lean review

- Trace an affected request or job through middleware, validation,
  authorization, container resolution, transactions, Eloquent, events,
  serialization, queues, retries, and error handling.
- Establish Laravel and PHP versions, container lifetimes, process model,
  database connection, queue semantics, and generated or cached configuration.
- Challenge mass assignment mistaken for authorization, N+1 queries, jobs
  dispatched before commit, stale queued models, broad tenant scopes, migration
  locks, and local behavior that ignores cached production configuration.
- Require database constraints for concurrent invariants and expand, migrate,
  validate, switch, and contract sequencing when old code, new code, workers,
  and queued payloads can coexist.
- In Octane or another long-running server, reject singleton or static state
  that can retain request, user, or tenant data.

Lean mode is insufficient for schema or backfill work, authorization changes,
queue delivery changes, long-running process adoption, multi-connection
transactions, or a deployment that changes cached artifacts.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/http-validation-and-authorization.md):
  Read when the reviewed work directly or indirectly changes routes, middleware, request
  validation, route model
  binding, guards, providers, policies, gates, CSRF, signed URLs, rate limits, trusted
  proxies, API resources, JSON output, pagination, or HTTP error behavior.
- [Focused rules](references/eloquent-transactions-and-migrations.md):
  Read when the reviewed work directly or indirectly changes Eloquent models,
  relationships, scopes, casts, observers,
  bulk updates, constraints, transactions, locking, database connections, schema,
  indexes, backfills, or mixed-version data behavior.
- [Focused rules](references/queues-events-and-workers.md):
  Read when the reviewed work directly or indirectly changes queued jobs, events,
  listeners, notifications, Horizon,
  scheduler behavior, retry, uniqueness, ordering, idempotency, worker termination,
  Octane, or another resident process.
- [Focused rules](references/caching-configuration-and-deployment.md):
  Read when the reviewed work directly or indirectly changes cache keys, invalidation,
  sessions, generated
  configuration, route or view caches, maintenance mode, release artifacts, storage
  links, OPcache, worker restarts, health checks, rollback, or deployment sequencing.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

Identify the affected request or job path, process lifetime, transaction
boundary, and configured driver assumptions behind each material finding.
