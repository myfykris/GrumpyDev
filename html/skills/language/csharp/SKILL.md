---
name: gd-csharp
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review C# and .NET engineering work for runtime compatibility, async behavior, dependency injection, disposal, serialization, concurrency, trimming, and deployment risks."
---

# C# GrumpyDev review

## Quick checks

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

- Assess disposed-resource use, sync-over-async deadlock, unsafe shared state, or
  incompatible serialization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the C# specialist.

## Verdict context

State the target runtime, async and cancellation model, dependency lifetimes,
disposal guarantees, serialization contract, and deployed-artifact evidence.
