---
name: gd-graphql-api-design
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review GraphQL API engineering work for schema ownership, authorization, resolver behavior, query cost, batching, nullability, errors, caching, and evolution."
---

# GraphQL API design GrumpyDev review

## Quick checks

- Read schemas, directives, resolvers, loaders, authorization, pagination, query
  limits, error conventions, persisted operations, and contract tests.

- Trace one nested query and mutation through parsing, authorization, data
  access, partial failure, retries, caching, and schema rollout.

Watch especially for N+1 resolver behavior, unbounded query depth or cost,
authorization applied only at entry points, nullable failures propagating
farther than expected, batching caches shared across users, deprecated fields
never removed, mutation input mapped directly to persistence, subscription
permissions that outlive the user role, and schema changes that break persisted
operations.

- Assess field-level data exposure or unbounded query work reachable by clients
  under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the GraphQL API design
specialist.

- [Focused rules](references/subscriptions-and-persisted-operations.md):
  Read when the work changes subscriptions, long-lived
  authorization, token expiry,
  revocation, reconnect, fan-out, event filtering, persisted operations, operation
  registration, allowlists, rollout, or revocation.

## Verdict context

State schema ownership, authorization coverage, mutation property controls,
query-cost and subscription limits, cache scope, production exposure, resolver
evidence, error semantics, and evolution safety.
