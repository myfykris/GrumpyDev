# REST API design full-review guidance

## Operating conditions

Establish the project target: HTTP and API standards, base paths, clients,
authentication, versioning and deprecation, error format, pagination,
idempotency, and rate limits. The changed boundary must define: Resource
semantics, HTTP methods, status codes, validation, errors, pagination,
filtering, concurrency, idempotency, caching, versioning, authentication, and
evolution.

## Failure patterns

- Define resource and operation semantics before arguing about URL aesthetics.
  Separate create, replace, partial update, action, and asynchronous job
  behavior.
- Require runtime validation, stable error codes, correct status semantics, and
  a safe policy for validation details and sensitive data.

## Verification to run or specify in the plan

- Run the published contract and real clients through methods, statuses, error
  bodies, conditional requests, content negotiation, validation, pagination,
  filtering and cache behavior at the actual gateway and application boundary.
- Repeat mutations before, during and after ambiguous timeouts; race concurrent
  writes; change data between pages; and verify idempotency, preconditions,
  stable ordering and partial-failure behavior.
- Run supported old and new clients and API versions together through rollout,
  deprecation and rollback, including cached responses and stale schemas.
- Exercise oversized and compressed inputs, expensive filters, concurrent
  requests, business-flow automation, malicious upstream responses, redirect
  chains, stale API versions, and failed partial mutations.
