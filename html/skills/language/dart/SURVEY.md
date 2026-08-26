# Dart survey contribution

## Applicability

Apply this contribution when a plan changes Dart packages, services,
command-line tools, or Flutter application code. Skip it when Dart does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Dart, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Dart SDK range, target platforms, JIT or AOT mode,
  package and code-generation tools, isolate use, native dependencies, and
  deployment packaging.
- Review doctrine for: Sound null safety, async scheduling, isolates, streams,
  package resolution, code generation, FFI, runtime and compilation modes,
  resource cleanup, and platform differences.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Dart VM, AOT, Flutter, browser, server, isolate,
  architecture, packaging, and platform service boundaries.

## Ask only when materially unresolved

- Which Dart version, target runtime, null-safety mode, package constraints, and
  isolate model apply?
- How do futures, streams, cancellation, serialization, errors, and mutable
  state cross isolates or UI lifecycles?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Dart VM, AOT, Flutter, browser, server,
  isolate, architecture, packaging, and platform service boundaries? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Dart answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Dart deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Dart doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Dart when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
