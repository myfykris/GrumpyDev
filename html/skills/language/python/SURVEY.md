# Python survey contribution

## Applicability

Apply this contribution when a plan changes Python applications, libraries,
workers, scripts, APIs, or their deployment environment. Skip it when Python
does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

For Python, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Interpreter implementations and versions,
  packaging and lock tooling, OS and architecture, worker model, async
  framework, native dependencies, locale and encoding, and deployment form.
- Review doctrine for: Interpreter behavior, typing limits, packaging, import
  and environment rules, async, threads and processes, GIL implications, object
  lifetime, serialization, native extensions, signals, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Interpreter and version, WSGI or ASGI or worker
  runtime, process and thread model, event loop, native wheels, OS and
  architecture, packaging, environment management, and shutdown.

## Ask only when materially unresolved

- Which Python version and implementation, target platforms, dependency
  resolver, and packaging mode apply?
- How do async and sync work, cancellation, typing boundaries, serialization,
  resources, and process concurrency interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Interpreter and version, WSGI or ASGI or
  worker runtime, process and thread model, event loop, native wheels, OS and
  architecture, packaging, environment management, and shutdown? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Python answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Python deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Python doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Python when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
