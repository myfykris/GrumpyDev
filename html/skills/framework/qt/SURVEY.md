# Qt survey contribution

## Applicability

Apply this contribution when a C++ plan changes Qt desktop, embedded, or
cross-platform applications. Skip it when Qt does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Qt, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Qt and compiler versions, widgets or QML, target
  OS and architectures, static or dynamic linking, plugin and graphics stack,
  packaging, and accessibility targets.
- Review doctrine for: QObject ownership, parent-child lifetime, signals and
  slots, thread affinity, event loops, QML and C++ boundaries, models,
  resources, plugins, and packaging.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Qt version, language binding, OS and window-system
  targets, platform plugins, native libraries, architecture, packaging,
  signing, display environment, and update channel.

## Ask only when materially unresolved

- Which Qt, C++ compiler, platform, rendering backend, and ownership model
  apply?
- How do parent ownership, signals, threads, event loops, shutdown,
  accessibility, and native resources interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Qt version, language binding, OS and
  window-system targets, platform plugins, native libraries, architecture,
  packaging, signing, display environment, and update channel? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Qt answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Qt deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Qt doctrine. Do
not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Qt when framework or runtime versions, lifecycle or rendering model,
dependency scopes, persistence, authentication, workers, supported clients, or
deployment process materially change, when evidence conflicts with saved
doctrine, or when the user requests a context refresh.
