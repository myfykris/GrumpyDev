# C# survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with C# or .NET code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For C#, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Target frameworks, runtime and SDK versions, OS
  targets, nullable mode, server or desktop model, trimming or AOT, deployment
  mode, and native dependencies.
- Review doctrine for: Language and .NET semantics, nullability, async and
  cancellation, dependency injection lifetimes, GC, threading, reflection,
  serialization, interop, trimming, AOT, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: .NET runtime, Windows or cross-platform target,
  architecture, framework-dependent versus self-contained deployment, trimming
  or AOT, service or desktop process model, and native dependencies.

## Ask only when materially unresolved

- Which C# language, .NET runtime, nullable context, target framework, and
  deployment versions apply?
- How do async cancellation, disposal, dependency lifetime, serialization, and
  concurrency cross the changed boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: .NET runtime, Windows or cross-platform
  target, architecture, framework-dependent versus self-contained deployment,
  trimming or AOT, service or desktop process model, and native dependencies?
  Ask only when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record C# answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed C# deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable C# doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey C# when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
