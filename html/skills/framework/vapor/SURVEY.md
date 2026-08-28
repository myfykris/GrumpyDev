# Vapor survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Vapor.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Vapor, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Vapor and Swift versions, event-loop topology,
  database drivers, queues, proxy and TLS, container or host deployment, and
  supported operating systems.
- Review doctrine for: Event loops, async and blocking work, request lifecycle,
  content decoding, authentication, Fluent transactions, queues, WebSockets,
  shutdown, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Swift and Vapor versions, event-loop and worker
  sizing, proxy, TLS, files, database pool, queues, executable platform,
  signals, drain, and deployment.

## Ask only when materially unresolved

- Which Swift, Vapor, SwiftNIO, database driver, and deployment versions apply?
- How do event-loop affinity, async work, request state, authentication,
  transactions, errors, and shutdown interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Swift and Vapor versions, event-loop and
  worker sizing, proxy, TLS, files, database pool, queues, executable platform,
  signals, drain, and deployment? Ask only when evidence and the core profile
  confirmation do not resolve them.

## Record in .grump

Record Vapor answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Vapor deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Vapor doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Vapor when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
