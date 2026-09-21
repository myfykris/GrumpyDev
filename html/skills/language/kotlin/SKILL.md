---
name: gd-kotlin
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Kotlin engineering work for nullability, coroutine ownership, Java interoperability, serialization, multiplatform differences, dependency compatibility, and lifecycle risks."
---

# Kotlin GrumpyDev review

## Quick checks

- Read Gradle configuration, Kotlin and JVM targets, compiler options, coroutine
  usage, serialization settings, platform source sets, and representative tests.

- Trace coroutine scopes, dispatchers, cancellation, flows, Java calls, nullable
  platform types, resources, and application lifecycle.

Watch especially for nullable Java platform types, coroutine scopes detached
from their owner, cancellation swallowed as an ordinary exception, blocking
calls on constrained dispatchers, data-class equality used for mutable identity,
and JVM interop changing default or overload behavior.

- Assess lost cancellation, blocking on a constrained dispatcher, unsafe platform
  types, or incompatible serialization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Kotlin specialist.

## Verdict context

State platform targets, coroutine ownership, Java boundary risks, serialization
contract, lifecycle behavior, and platform-specific evidence.
