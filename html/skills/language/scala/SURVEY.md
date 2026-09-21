# Scala survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Scala code, artifacts, or runtime behavior.

## Inspect

- Read sbt or build configuration, Scala and JVM versions, effect or actor
  libraries, serialization settings, generated code, and representative tests.

## Ask when unresolved

- Which Scala version, JVM, build tool, binary version, effect system, and
  dependency versions apply?

- How do effects, futures, cancellation, blocking, implicits, serialization,
  and Java interop cross the boundary?

- Which runtime or deployment differences materially change future reviews:
  Scala and JDK versions, JVM and execution context, application or cluster
  runtime, serializer, packaging, resource limits, and rolling compatibility?

## Record

Map durable Scala version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
