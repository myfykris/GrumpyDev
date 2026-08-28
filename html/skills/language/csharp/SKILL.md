---
name: csharp
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review C# and .NET plans and other engineering artifacts for runtime compatibility, async behavior, dependency injection, disposal, serialization, concurrency, trimming, and deployment risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with C# or .NET code, artifacts, or runtime behavior."
---

# C# GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read project and solution files, target frameworks, nullable settings, package
  locks, analyzers, publish settings, dependency registration, and
  representative tests.

- Trace async calls, cancellation, scoped services, disposable resources,
  serialization, background work, and hosting or shutdown behavior.

Watch especially for async void outside event handlers, sync-over-async
deadlocks or starvation, undisposed resources, nullable annotations treated as
runtime validation, repeated or deferred LINQ execution, reflection-dependent
code broken by trimming, unsafe polymorphic or legacy deserialization, XML
external resolution, and mutable identity keys.

Lean mode is insufficient when this material severity condition may apply:

- Treat disposed-resource use, sync-over-async deadlock, unsafe shared state, or
  incompatible serialization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete C# evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the target runtime, async and cancellation model, dependency lifetimes,
disposal guarantees, serialization contract, and deployed-artifact evidence.
