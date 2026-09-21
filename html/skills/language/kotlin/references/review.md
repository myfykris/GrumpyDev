# Kotlin full-review guidance

## Operating conditions

Establish the project target: Kotlin and plugin versions, backend targets, JDK
and Android API levels, coroutine stack, multiplatform targets, build tooling,
serialization, and native dependencies. The changed boundary must define: Kotlin
type and null semantics, coroutines and structured concurrency, Java interop,
JVM or Android lifecycle, multiplatform boundaries, serialization, generated
code, reflection, and native targets.

## Failure patterns

- Require structured concurrency and an explicit owner for every scope, job,
  flow collection, and long-lived callback.
- Check cancellation propagation, blocking calls on constrained dispatchers,
  exception supervision, and cleanup in finally blocks.
- Treat Java platform types and unchecked casts as runtime risks, not Kotlin
  null-safety guarantees.
- Verify serialization defaults, sealed-class evolution, and JVM or
  multiplatform compatibility across deployed versions.
- Demand platform-specific and release-build tests where source sets,
  reflection, native behavior, or Android lifecycle can diverge.

## Verification to run or specify in the plan

- Cancel parent jobs while child coroutines, flow collectors, and blocking
  dependencies are active. Check cleanup, exception propagation, and the
  absence of work that outlives its declared scope.
- Exercise Java platform types and serialized data at runtime boundaries.
  Build and run the supported source sets and release targets where
  reflection, native interop, or Android lifecycle behavior can differ.
