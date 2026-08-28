# GraphQL API design standard review

## Establish the operating model

Establish the project target: GraphQL implementation and version, schema
ownership, clients, authentication, federation, query limits, persisted
operations, subscriptions, and deprecation policy. The changed boundary must
define: Schema ownership, nullability, evolution, resolvers, authorization,
batching, query cost, pagination, errors, subscriptions, caching, and persisted
operations.

Identify the owners of schema evolution, resolver data access, field and object
authorization, batching, query-cost policy, pagination, persisted operations,
subscriptions, caches, and client compatibility. Prove authorization and cost
limits apply after aliases, fragments and variables are resolved, and show how
old clients, cached operations, and long-lived subscriptions behave while the
schema and servers change.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Run denied field, object, mutation, and subscription cases across roles and
  tenants, including aliases, batching, stale tokens, and cached values.
## Ask when evidence is missing

- Where is authorization enforced for each changed field, object, and resolver
  path?
- What query depth, breadth, alias, batching, subscription, result, and
  downstream-cost limits apply to untrusted clients?

## Calibrate findings

- Downgrade when the schema is internal and trusted or authorization and cost
  limits are enforced and tested at execution time.
