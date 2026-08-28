# Kotlin standard review

## Establish the operating model

Establish the project target: Kotlin and plugin versions, backend targets, JDK
and Android API levels, coroutine stack, multiplatform targets, build tooling,
serialization, and native dependencies. The changed boundary must define: Kotlin
type and null semantics, coroutines and structured concurrency, Java interop,
JVM or Android lifecycle, multiplatform boundaries, serialization, generated
code, reflection, and native targets.

Define ownership, errors, cancellation, and concurrency for Kotlin type and null
semantics, coroutines and structured concurrency, Java interop, JVM or Android
lifecycle, multiplatform boundaries. Verify version, package, native,
serialization, and artifact compatibility for serialization, generated code,
reflection, native targets across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared Kotlin compiler and runtime
  targets: Kotlin type and null semantics, coroutines and structured
  concurrency, Java interop, JVM or Android lifecycle, multiplatform boundaries.
  Use the real compiler or interpreter and supported release modes rather than a
  development substitute.
- Exercise failure and edge behavior for: serialization, generated code,
  reflection, native targets. Exercise boundary values, encoding, cancellation,
  resource exhaustion, concurrency, dependency failure, and termination where
  they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Kotlin, target platform, JDK or Android version, compiler mode, and
  coroutine library versions apply?
- How do nullability, structured concurrency, cancellation, dispatchers,
  serialization, and Java interop cross the boundary?

## Calibrate findings

- Downgrade when ownership is bounded and target, coroutine, nullability,
  interop, and failure tests cover the path.
