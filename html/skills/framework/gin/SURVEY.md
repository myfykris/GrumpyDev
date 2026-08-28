# Gin survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Gin.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Gin, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Gin and Go versions, middleware, trusted proxies,
  binding and validation approach, request limits, server topology, and
  deployment target.
- Review doctrine for: Middleware order, context reuse, binding and validation,
  errors, goroutine safety, streaming, shutdown, proxy trust, and server
  configuration.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Go and Gin versions, proxy trust, worker process,
  limits, timeouts, file serving, signals, drain, and deployment architecture.

## Ask only when materially unresolved

- Which Go and Gin versions, server configuration, middleware order, and binding
  rules apply?
- How are validation, authentication, limits, cancellation, errors, shared
  state, and shutdown handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Go and Gin versions, proxy trust, worker
  process, limits, timeouts, file serving, signals, drain, and deployment
  architecture? Ask only when evidence and the core profile confirmation do not
  resolve them.

## Record in .grump

Record Gin answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Gin deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Gin doctrine. Do
not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Gin when framework or runtime versions, lifecycle or rendering model,
dependency scopes, persistence, authentication, workers, supported clients, or
deployment process materially change, when evidence conflicts with saved
doctrine, or when the user requests a context refresh.
