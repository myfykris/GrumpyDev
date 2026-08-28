# Actix Web survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Actix Web.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Actix Web, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Actix and Rust versions, Tokio runtime, worker
  counts, proxy and TLS termination, payload limits, state ownership, and
  deployment model.
- Review doctrine for: Extractor limits, application and worker state, async
  blocking, middleware ordering, error mapping, streaming, shutdown, TLS and
  proxy behavior.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Rust and Actix versions, worker count, async
  runtime, blocking pool, reverse proxy, TLS, body and timeout limits, process
  manager, drain, and shutdown.

## Ask only when materially unresolved

- Which Actix Web, Rust, and Tokio versions and worker model apply to the
  service?
- How do extractors, shared state, blocking work, errors, limits, and graceful
  shutdown behave?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Rust and Actix versions, worker count,
  async runtime, blocking pool, reverse proxy, TLS, body and timeout limits,
  process manager, drain, and shutdown? Ask only when evidence and the core
  profile confirmation do not resolve them.

## Record in .grump

Record Actix Web answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Actix Web deployment facts on the affected `DEP-###` profile.
Use a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Actix Web
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Actix Web when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
