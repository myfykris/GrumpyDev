# REST API design survey contribution

## Applicability

Apply this contribution when a plan creates or changes HTTP endpoints, request
or response schemas, API clients, or public service contracts. Skip it when REST
API design does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

## Inspect before asking

For REST API design, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: HTTP and API standards, base paths, clients,
  authentication, versioning and deprecation, error format, pagination,
  idempotency, and rate limits.
- Review doctrine for: Resource semantics, HTTP methods, status codes,
  validation, errors, pagination, filtering, concurrency, idempotency, caching,
  versioning, object and property authorization, business-flow abuse, resource
  limits, upstream trust, inventory, and evolution.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Gateway and proxy path, TLS and identity, cache,
  body and timeout limits, retries, regions, version rollout, rate limits, and
  object-authorization boundary.

## Ask only when materially unresolved

- Which clients depend on the changed resource, method, schema, status, and
  error contract?
- What idempotency, object and property authorization, business-flow abuse,
  resource limits, upstream trust, pagination, caching, and compatibility
  behavior applies?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Gateway and proxy path, TLS and
  identity, cache, body and timeout limits, retries, regions, version rollout,
  rate limits, and object-authorization boundary? Ask only when evidence and
  the core profile confirmation do not resolve them.

## Record in .grump

Record REST API design answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed REST API design deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable REST API
design doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey REST API design when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
