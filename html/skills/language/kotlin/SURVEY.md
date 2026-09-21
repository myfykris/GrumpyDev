# Kotlin survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Kotlin code, artifacts, or runtime behavior.

## Inspect

- Read Gradle configuration, Kotlin and JVM targets, compiler options, coroutine
  usage, serialization settings, platform source sets, and representative tests.

## Ask when unresolved

- Which Kotlin, target platform, JDK or Android version, compiler mode, and
  coroutine library versions apply?

- How do nullability, structured concurrency, cancellation, dispatchers,
  serialization, and Java interop cross the boundary?

- Which runtime or deployment differences materially change future reviews:
  JVM, Android, native, or multiplatform targets; JDK or device versions;
  coroutine dispatcher environment; packaging; and interop boundaries?

## Record

Map durable Kotlin version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
