# GraphQL API design full-review guidance

## Operating conditions

Establish the project target: GraphQL implementation and version, schema
ownership, clients, authentication, federation, query limits, persisted
operations, subscriptions, and deprecation policy. The changed boundary must
define: Schema ownership, nullability, evolution, resolvers, authorization,
batching, query cost, pagination, errors, subscriptions, caching, and persisted
operations.

## Failure patterns

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
- Define nullability and error propagation deliberately so one field failure
  does not erase unrelated useful data unexpectedly.
- Require additive schema evolution, deprecation telemetry, mixed-client
  evidence, stable identifiers, and cache behavior.

## Verification to run or specify in the plan

- Run denied field, object, mutation, and subscription cases across roles and
  tenants, including aliases, batching, stale tokens, and cached values.
