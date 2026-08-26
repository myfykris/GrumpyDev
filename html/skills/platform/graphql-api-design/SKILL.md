---
name: graphql-api-design
description: Review GraphQL API plans for schema ownership, authorization, resolver behavior, query cost, batching, nullability, errors, caching, and evolution. Use when a plan creates or changes a GraphQL schema, resolver, client contract, or gateway.
---

# GraphQL API design plan review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and applicable installed framework and storage
specialists.

## Inspect evidence

- Read schemas, directives, resolvers, loaders, authorization, pagination, query
  limits, error conventions, persisted operations, and contract tests.
- Trace one nested query and mutation through parsing, authorization, data
  access, partial failure, retries, caching, and schema rollout.

## Establish the operating model

Establish the project target: GraphQL implementation and version, schema
ownership, clients, authentication, federation, query limits, persisted
operations, subscriptions, and deprecation policy. The changed boundary must
define: Schema ownership, nullability, evolution, resolvers, authorization,
batching, query cost, pagination, errors, subscriptions, caching, and persisted
operations.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Schema ownership, nullability, evolution, resolvers,
authorization, batching. Prove query cost, pagination, errors, subscriptions,
caching, persisted operations through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for N+1 resolver behavior, unbounded query depth or cost,
authorization applied only at entry points, nullable failures propagating
farther than expected, batching caches shared across users, deprecated fields
never removed, mutation input mapped directly to persistence, subscription
permissions that outlive the user role, and schema changes that break persisted
operations.

- Enforce authorization in resolvers or domain boundaries for every returned
  object, field, mutation, subscription event, and state transition. Do not
  treat schema visibility, authentication, or a top-level resolver check as
  field or object authorization.
- Detect N+1 access, duplicate loads, unbounded lists, deep fragments, aliases,
  repeated fields, batching leaks, and expensive computed fields.
- Set depth, complexity, time, result-size, and rate budgets based on actual
  resolver and downstream cost, not syntax alone. Count aliases, fragments,
  batching, list multipliers, and separately transported operations.
- Define input types and mutable properties explicitly. Reject direct binding of
  mutation input to database or domain objects, and filter response properties
  after authorization.
- Scope DataLoader and resolver caches to one request and the complete identity,
  tenant, locale, and authorization context. Never share user-sensitive cached
  values through a process-global loader.
- Decide whether introspection, explorers, suggestions, detailed errors, and
  development endpoints are exposed in each environment. Their restriction is
  defense in depth, not a replacement for execution-time authorization.
- Authenticate and authorize subscription connection, operation, topic, and
  each delivered event. Define token expiry, permission change, revocation,
  reconnect, message size, and per-client fan-out limits.
- Treat persisted operations as a controlled contract with ownership,
  registration, rollout, revocation, and query-cost evidence. An allowlisted
  operation still requires normal authorization and input validation.
- Define nullability and error propagation deliberately so one field failure
  does not erase unrelated useful data unexpectedly.
- Require additive schema evolution, deprecation telemetry, mixed-client
  evidence, stable identifiers, and cache behavior.

## Verify the claims

- Verify these behaviors through the effective GraphQL API design configuration
  and runtime topology: Schema ownership, nullability, evolution, resolvers,
  authorization, batching. Use effective rendered configuration and deployable
  artifacts in a representative identity, topology, capacity, and policy
  boundary.
- Exercise failure and edge behavior for: query cost, pagination, errors,
  subscriptions, caching, persisted operations. Exercise startup, readiness,
  normal load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Run denied field, object, mutation, and subscription cases across roles and
  tenants, including aliases, batching, stale tokens, and cached values.
- Exercise deep and broad fragments, repeated aliases, list multipliers,
  malformed variables, oversized batches, expensive mutations, reconnect, and
  introspection or persisted-operation policy in the production configuration.

## Ask when evidence is missing

- Where is authorization enforced for each changed field, object, and resolver
  path?
- What query depth, breadth, alias, batching, subscription, result, and
  downstream-cost limits apply to untrusted clients?

## Calibrate findings

- Treat field-level data exposure or unbounded query work reachable by clients
  as critical.
- Downgrade when the schema is internal and trusted or authorization and cost
  limits are enforced and tested at execution time.

## Add to the verdict

State schema ownership, authorization coverage, mutation property controls,
query-cost and subscription limits, cache scope, production exposure, resolver
evidence, error semantics, and evolution safety.
