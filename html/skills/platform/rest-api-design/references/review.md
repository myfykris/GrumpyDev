# REST API design standard review

## Inspect additional evidence

- Trace one successful request and representative failure paths end to end.

## Establish the operating model

Establish the project target: HTTP and API standards, base paths, clients,
authentication, versioning and deprecation, error format, pagination,
idempotency, and rate limits. The changed boundary must define: Resource
semantics, HTTP methods, status codes, validation, errors, pagination,
filtering, concurrency, idempotency, caching, versioning, authentication, and
evolution.

Identify the API contract and resource owners, independently deployed clients,
gateway and cache behavior, identity and authorization enforcement, validation
authority, mutation and concurrency semantics, error format, pagination order,
version policy, and retirement owner. Prove retries, conditional requests,
concurrent writes, cache variance, partial failure and old-client overlap obey
the documented HTTP contract.

## Challenge the reviewed work

### Recurring traps

- Define resource and operation semantics before arguing about URL aesthetics.
  Separate create, replace, partial update, action, and asynchronous job
  behavior.
- Require runtime validation, stable error codes, correct status semantics, and
  a safe policy for validation details and sensitive data.
## Verify the claims

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

## Ask when evidence is missing

- Which clients depend on the changed resource, method, schema, status, and
  error contract?
## Calibrate findings

- Downgrade when the endpoint is private and coordinated or contract,
  idempotency, and rollout tests cover every client.
