---
name: gd-java
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Java engineering work for JVM compatibility, concurrency, resource management, serialization, dependency resolution, reflection, memory, and deployment risks."
---

# Java GrumpyDev review

## Quick checks

- Read Maven or Gradle configuration, toolchains, dependency locks, module
  settings, JVM flags, serialization mappings, and representative tests.

- Trace thread pools, futures, transactions, resources, class loading,
  reflection, shutdown hooks, and data crossing service boundaries.

Watch especially for nullability assumptions at framework boundaries,
inconsistent identity and equality semantics, mutable shared state, resources
that escape structured cleanup, thread-local state under pooled or virtual
threads, class-loader leaks, XML external entities, dynamic expression or class
loading, and unsafe deserialization.

- Assess a reachable data race, thread starvation, lost interruption, or
  incompatible persisted serialization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Java specialist.

## Verdict context

State JVM and bytecode targets, executor and resource ownership, serialization
compatibility, memory assumptions, and deployed-runtime evidence.
