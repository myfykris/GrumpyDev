---
name: rest-api-design
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review REST API plans and other engineering artifacts for contract, resource, method, idempotency, error, pagination, compatibility, caching, authorization, and operational risks. Project applicability: the project exposes or consumes a resource-oriented HTTP API whose contract intentionally depends on REST and HTTP semantics. An arbitrary HTTP endpoint, webhook, GraphQL endpoint, gRPC gateway, or RPC-style JSON API does not make this specialist applicable by itself."
---

# REST API design review

Apply this specialist to resource-oriented HTTP contracts, not merely to
anything transported over HTTP. If the API is RPC-style, GraphQL, gRPC, or only
a webhook surface, use the more specific applicable skills unless part of its
contract deliberately depends on REST resource, method, status, caching, or
conditional-request semantics.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read the API description, existing routes and conventions, schema validators,
  authorization middleware, client usage, error format, and compatibility tests.

- Identify consumers, deployment independence, traffic shape, retry behavior,
  data sensitivity, and the source of resource identifiers.

Watch especially for PUT, PATCH, and retry semantics left ambiguous,
non-idempotent operations automatically retried, status codes hiding partial
failure, offset pagination drifting under writes, versioning that forks behavior
indefinitely, object or property authorization gaps, mass assignment, automation
of sensitive business flows, third-party responses trusted without limits,
forgotten API versions, and intermediary caches serving private data.

Lean mode is insufficient when this material severity condition may apply:

- Treat unauthorized data access, destructive retry behavior, or an incompatible
  public contract change as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/authorization-input-and-abuse.md):
  Read when the reviewed work directly or indirectly changes authentication, object or
  property authorization, tenant
  isolation, mutable fields, validation, bulk operations, uploads, body or decompression
  limits, expensive filters, automation-sensitive business flows, rate limits, or abuse
  controls.
- [Focused rules](references/idempotency-pagination-and-caching.md):
  Read when the reviewed work directly or indirectly changes retried mutations,
  idempotency keys, concurrent duplicate
  requests, asynchronous jobs, pagination, ordering under concurrent writes, conditional
  requests, cache keys, cache variance, or stale behavior.
- [Focused rules](references/versioning-upstreams-and-evolution.md):
  Read when the reviewed work directly or indirectly changes public contracts,
  independently deployed clients, versions,
  deprecation, compatibility, error formats, third-party or upstream responses,
  redirects, exposed routes, administrative surfaces, retirement, mixed versions, or
  rollout sequencing.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State consumer compatibility, authorization scope, mutation idempotency,
business-flow and resource-abuse controls, upstream trust, API inventory,
pagination consistency, error contract, and the evidence required for approval.
