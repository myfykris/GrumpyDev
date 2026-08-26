# Java survey contribution

## Applicability

Apply this contribution when a plan changes Java services, libraries, workers,
build plugins, or JVM runtime configuration. Skip it when Java does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Java, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: JDK vendor and versions, language and bytecode
  target, JVM flags and GC, build tool, module use, container limits, native
  dependencies, and supported platforms.
- Review doctrine for: Java and JVM semantics, memory model, threads and virtual
  threads, exceptions, class loading, reflection, serialization, JNI, GC,
  resource lifecycle, modules, bytecode compatibility, and container behavior.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: JDK vendor and version, JVM flags and collector,
  container limits, application server or standalone process, architecture,
  native libraries, packaging, and shutdown.

## Ask only when materially unresolved

- Which Java language level, JDK vendor and version, JVM settings, target
  runtime, and dependency versions apply?
- How do threads, virtual threads, interruption, resource lifetime,
  serialization, and memory visibility cross the boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: JDK vendor and version, JVM flags and
  collector, container limits, application server or standalone process,
  architecture, native libraries, packaging, and shutdown? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Java answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Java deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Java doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Java when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
