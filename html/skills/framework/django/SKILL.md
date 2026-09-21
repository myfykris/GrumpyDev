---
name: gd-django
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Django engineering work for model and migration behavior, transactions, ORM queries, request security, caching, background work, settings, and deployment risks."
---

# Django GrumpyDev review

## Quick checks

- Read settings, URL and middleware order, models and migrations, managers and
  querysets, authentication, templates or API layers, caching, tasks, and tests.

- Trace requests and jobs through transactions, permissions, ORM queries,
  signals, files, caching, and deployment or migration order.

Watch especially for generated migrations assumed to be operationally safe, N+1
query regressions, business behavior hidden in signals, transaction scopes that
do not cover deferred work, sync and async crossings, and development settings
presented as deployment evidence.

- Assess authorization bypass, blocking migration, or async-unsafe state on a
  critical path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Django specialist.

## Verdict context

State migration and transaction safety, query behavior, authorization controls,
signal or task ownership, settings assumptions, and deployment evidence.
