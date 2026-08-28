# Scala survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Scala code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Scala, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Scala and JDK versions, build tool, major
  libraries and effect system, binary compatibility target, runtime topology,
  serialization stack, and deployment platform.
- Review doctrine for: Scala 2 and 3 differences, type and implicit behavior,
  JVM interop, effect systems, futures and streams, concurrency, serialization,
  macros, binary compatibility, and build graph.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Scala and JDK versions, JVM and execution context,
  application or cluster runtime, serializer, packaging, resource limits, and
  rolling compatibility.

## Ask only when materially unresolved

- Which Scala version, JVM, build tool, binary version, effect system, and
  dependency versions apply?
- How do effects, futures, cancellation, blocking, implicits, serialization, and
  Java interop cross the boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Scala and JDK versions, JVM and
  execution context, application or cluster runtime, serializer, packaging,
  resource limits, and rolling compatibility? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Scala answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Scala deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Scala doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Scala when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
