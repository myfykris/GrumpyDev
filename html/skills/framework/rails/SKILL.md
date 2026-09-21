---
name: gd-rails
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Rails engineering work for Active Record behavior, migrations, callbacks, jobs, caching, authorization, request security, and zero-downtime deployment risks."
---

# Ruby on Rails GrumpyDev review

## Quick checks

- Read Rails and Ruby versions, routes, middleware, models and migrations,
  callbacks, jobs, caches, credentials, server and worker configuration, and
  tests.

- Trace requests and jobs through strong parameters, authorization,
  transactions, queries, callbacks, retries, and deployment.

Watch especially for callbacks hiding transactional side effects, N+1 query
regressions, autoload and eager-load differences, jobs enqueued before commit,
non-idempotent retries, and migrations whose locks or rewrites are invisible in
development data.

- Assess authorization bypass, callback-driven duplicate effects, or destructive
  migration behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Ruby on Rails
specialist.

## Verdict context

State ORM and callback behavior, migration safety, job guarantees, authorization
boundaries, runtime configuration, and production deployment evidence.
