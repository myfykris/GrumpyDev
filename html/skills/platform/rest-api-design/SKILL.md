---
name: rest-api-design
description: Review HTTP REST API plans for contract, resource, idempotency, error, pagination, compatibility, caching, authorization, and operational risks. Use when a plan creates or changes HTTP endpoints, request or response schemas, API clients, or public service contracts.
---

# REST API design review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read the API description, existing routes and conventions, schema validators,
  authorization middleware, client usage, error format, and compatibility tests.
- Identify consumers, deployment independence, traffic shape, retry behavior,
  data sensitivity, and the source of resource identifiers.
- Trace one successful request and representative failure paths end to end.

## Establish the operating model

Establish the project target: HTTP and API standards, base paths, clients,
authentication, versioning and deprecation, error format, pagination,
idempotency, and rate limits. The changed boundary must define: Resource
semantics, HTTP methods, status codes, validation, errors, pagination,
filtering, concurrency, idempotency, caching, versioning, authentication, and
evolution.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Resource semantics, HTTP methods, status codes,
validation, errors, pagination, filtering. Prove concurrency, idempotency,
caching, versioning, authentication, evolution through rotation, overload,
partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for PUT, PATCH, and retry semantics left ambiguous,
non-idempotent operations automatically retried, status codes hiding partial
failure, offset pagination drifting under writes, versioning that forks behavior
indefinitely, object or property authorization gaps, mass assignment,
automation of sensitive business flows, third-party responses trusted without
limits, forgotten API versions, and intermediary caches serving private data.

- Define resource and operation semantics before arguing about URL aesthetics.
  Separate create, replace, partial update, action, and asynchronous job
  behavior.
- Require runtime validation, stable error codes, correct status semantics, and
  a safe policy for validation details and sensitive data.
- Establish idempotency for retried mutations, including key scope, persistence,
  expiration, concurrent duplicates, and mismatched payloads.
- Check authorization for every object, property, function, and state
  transition, not only authentication at the route. Apply request property
  allowlists and response filtering at the server; include identifier
  enumeration, cross-tenant access, bulk operations, and stale permissions.
- Require deterministic pagination under concurrent changes. Flag unbounded
  collections and offset pagination where deep or mutating data matters.
- Analyze backward and forward compatibility across independently deployed
  clients. Adding a required field or tightening validation is a breaking
  change.
- Define timeouts, rate limits, caching and conditional requests, async
  completion, observability, and partial failure where relevant.
- Bound request bytes, decompression, parsing, result size, page size, uploaded
  files, expensive filters, concurrent work, and downstream cost by authenticated
  actor and tenant where possible. An IP-only rate limit is not an abuse model.
- Identify business flows whose value can be abused through automation, such as
  reservations, invitations, recovery, signup, or purchases. Define economic,
  identity, sequence, and velocity controls in addition to transport rate limits.
- Treat upstream and third-party API data as untrusted. Validate its schema and
  semantics, bound response and decompression size, set timeouts, restrict
  redirects, and prevent returned URLs or fields from bypassing local policy.
- Inventory every exposed version, host, route, method, documentation endpoint,
  administrative surface, and debug mode. Define owners and retirement dates so
  an obsolete endpoint cannot silently escape current controls.

## Verify the claims

- Verify these behaviors through the effective REST API design configuration and
  runtime topology: Resource semantics, HTTP methods, status codes, validation,
  errors, pagination, filtering. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: concurrency, idempotency, caching,
  versioning, authentication, evolution. Exercise startup, readiness, normal
  load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Run an authorization matrix across actor, tenant, object, property, function,
  and state, including bulk requests and identifiers obtained from another
  account.
- Exercise oversized and compressed inputs, expensive filters, concurrent
  requests, business-flow automation, malicious upstream responses, redirect
  chains, stale API versions, and failed partial mutations.

## Ask when evidence is missing

- Which clients depend on the changed resource, method, schema, status, and
  error contract?
- What idempotency, object and property authorization, business-flow abuse,
  resource limits, upstream trust, pagination, caching, and compatibility
  behavior applies?

## Calibrate findings

- Treat unauthorized data access, destructive retry behavior, or an incompatible
  public contract change as critical.
- Downgrade when the endpoint is private and coordinated or contract,
  idempotency, and rollout tests cover every client.

## Add to the verdict

State consumer compatibility, authorization scope, mutation idempotency,
business-flow and resource-abuse controls, upstream trust, API inventory,
pagination consistency, error contract, and the evidence required for approval.
