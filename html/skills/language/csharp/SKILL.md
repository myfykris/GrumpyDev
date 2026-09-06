---
name: csharp
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review C# and .NET engineering work for runtime compatibility, async behavior, dependency injection, disposal, serialization, concurrency, trimming, and deployment risks."
---

# C# GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
