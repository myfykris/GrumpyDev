# REST idempotency, pagination, and caching

Read this reference when the reviewed work directly or indirectly changes retried
mutations, idempotency keys,
concurrent duplicate requests, asynchronous jobs, pagination, ordering under concurrent
writes, conditional requests, cache keys, cache variance, or stale behavior.

## Review requirements

- Establish idempotency for retried mutations, including key scope, persistence,
  expiration, concurrent duplicates, and mismatched payloads.

- Require deterministic pagination under concurrent changes. Flag unbounded
  collections and offset pagination where deep or mutating data matters.

- Define timeouts, rate limits, caching and conditional requests, async
  completion, observability, and partial failure where relevant.
