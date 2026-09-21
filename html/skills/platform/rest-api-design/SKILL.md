---
name: gd-rest-api-design
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review REST API engineering work for contract, resource, method, idempotency, error, pagination, compatibility, caching, authorization, and operational risks."
---

# REST API design review

## Quick checks

- Inspect the API description, existing routes, validators, authorization,
  client usage, error format, compatibility tests, and deployed API inventory.
- Establish consumers, deployment independence, traffic and retry behavior,
  data sensitivity, and identifier ownership.
- Challenge ambiguous mutation semantics, unsafe automatic retries, partial
  failures hidden by status codes, pagination drift, endless version forks,
  object or property authorization gaps, mass assignment, unbounded work,
  upstream responses trusted without limits, and private data in shared caches.

## References

- For a material REST API effect or uncertainty in a full review, read
  [review.md](references/review.md).
- For authorization, validation, bulk work, uploads, limits, or abuse controls,
  read [authorization-input-and-abuse.md](references/authorization-input-and-abuse.md).
- For retried mutations, idempotency, pagination, ordering, or caching, read
  [idempotency-pagination-and-caching.md](references/idempotency-pagination-and-caching.md).
- For public contracts, independent clients, upstreams, versions, deprecation,
  or mixed-version rollout, read
  [versioning-upstreams-and-evolution.md](references/versioning-upstreams-and-evolution.md).

## Verdict context

State consumer compatibility, authorization scope, mutation idempotency, abuse
controls, upstream trust, API inventory, pagination, and error-contract evidence.
