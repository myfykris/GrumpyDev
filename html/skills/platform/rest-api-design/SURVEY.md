# REST API design survey contribution

## Applies when

Apply this contribution when the project exposes or consumes a resource-oriented
HTTP API whose contract intentionally depends on REST and HTTP semantics. Do not
apply it merely because a system has an HTTP endpoint, webhook, GraphQL endpoint,
gRPC gateway, or RPC-style JSON API. Apply the more specific applicable skills
unless some part of that contract deliberately uses REST resource, method,
status, caching, or conditional-request semantics.

## Inspect

- Inspect the API description, existing routes, validators, authorization,
  client usage, error format, compatibility tests, and deployed API inventory.

## Ask when unresolved

- Which clients must remain compatible with the project's resource, method,
  schema, status, and error contracts?

- What idempotency, object and property authorization, business-flow abuse,
  resource limits, upstream trust, pagination, caching, and compatibility
  behavior applies?

- Which runtime or deployment differences materially change future reviews:
  Gateway and proxy path, TLS and identity, cache, body and timeout limits,
  retries, regions, version rollout, rate limits, and object-authorization
  boundary?

## Record

Map durable REST API design requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
