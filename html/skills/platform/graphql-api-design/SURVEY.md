# GraphQL API design survey contribution

## Applies when

Apply this contribution when the project exposes, consumes, or operates GraphQL schemas,
resolvers, clients, or gateways.

## Inspect

- Read schemas, directives, resolvers, loaders, authorization, pagination, query
  limits, error conventions, persisted operations, and contract tests.

## Ask when unresolved

- What authorization rules and enforcement points govern the project's
  GraphQL fields, objects, and resolver paths?

- What query depth, breadth, alias, batching, subscription, result, and
  downstream-cost limits apply to untrusted clients?

- Which runtime or deployment differences materially change future reviews:
  Gateway and service topology, resolver placement, batching scope, cache,
  subscription transport, proxy limits, authorization boundary, scaling, and
  persisted-operation deployment?

## Record

Map durable GraphQL API design requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
