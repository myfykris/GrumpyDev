---
name: gd-laravel
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Laravel engineering work for service-container scope, Eloquent behavior, migrations, queues, events, authorization, caching, and deployment risks."
---

# Laravel GrumpyDev review

## Quick checks

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

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Laravel specialist.

- [Focused rules](references/http-validation-and-authorization.md):
  Read when the work changes routes, middleware, request
  validation, route model
  binding, guards, providers, policies, gates, CSRF, signed URLs, rate limits, trusted
  proxies, API resources, JSON output, pagination, or HTTP error behavior.
- [Focused rules](references/eloquent-transactions-and-migrations.md):
  Read when the work changes Eloquent models,
  relationships, scopes, casts, observers,
  bulk updates, constraints, transactions, locking, database connections, schema,
  indexes, backfills, or mixed-version data behavior.
- [Focused rules](references/queues-events-and-workers.md):
  Read when the work changes queued jobs, events,
  listeners, notifications, Horizon,
  scheduler behavior, retry, uniqueness, ordering, idempotency, worker termination,
  Octane, or another resident process.
- [Focused rules](references/caching-configuration-and-deployment.md):
  Read when the work changes cache keys, invalidation,
  sessions, generated
  configuration, route or view caches, maintenance mode, release artifacts, storage
  links, OPcache, worker restarts, health checks, rollback, or deployment sequencing.

## Verdict context

Identify the affected request or job path, process lifetime, transaction
boundary, and configured driver assumptions behind each material finding.
