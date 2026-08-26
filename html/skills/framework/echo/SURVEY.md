# Echo survey contribution

## Applicability

Apply this contribution when a Go plan changes Echo HTTP services, handlers,
middleware, or server configuration. Skip it when Echo does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Echo, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Echo and Go versions, server topology, middleware
  stack, trusted proxies, request limits, validation, TLS termination, and
  deployment target.
- Review doctrine for: Middleware order, context lifetime, binder and validator
  behavior, error handling, concurrency, streaming, shutdown, proxy trust, and
  deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Go and Echo versions, worker process, reverse proxy
  and trusted addresses, TLS, body and timeout limits, filesystem, signals,
  drain, and cross-compilation target.

## Ask only when materially unresolved

- Which Go and Echo versions, server settings, middleware order, and binder
  behavior apply?
- How are validation, authentication, request limits, cancellation, errors, and
  graceful shutdown handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Go and Echo versions, worker process,
  reverse proxy and trusted addresses, TLS, body and timeout limits,
  filesystem, signals, drain, and cross-compilation target? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Echo answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Echo deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Echo doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Echo when framework or runtime versions, lifecycle or rendering model,
dependency scopes, persistence, authentication, workers, supported clients, or
deployment process materially change, when evidence conflicts with saved
doctrine, or when the user requests a context refresh.
