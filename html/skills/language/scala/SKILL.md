---
name: gd-scala
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Scala engineering work for effect ownership, concurrency, type-level assumptions, Java interoperability, serialization, build compatibility, and distributed runtime risks."
---

# Scala GrumpyDev review

## Quick checks

- Read sbt or build configuration, Scala and JVM versions, effect or actor
  libraries, serialization settings, generated code, and representative tests.

- Trace effects, execution contexts, futures or fibers, blocking work, Java
  boundaries, implicits or givens, state, and shutdown.

Watch especially for surprising implicit or given resolution, lazy
initialization under concurrency, futures using an unsuitable execution context,
strict and lazy collection behavior being confused, erased runtime types,
variance hiding unsafe assumptions, and binary incompatibility across library
versions.

- Assess binary incompatibility, lost effect cancellation, dispatcher starvation,
  or unsafe shared state under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Scala specialist.

## Verdict context

State Scala and JVM targets, effect and execution model, binary compatibility,
serialization assumptions, and distributed failure evidence.
