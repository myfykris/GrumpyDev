# Java survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Java, JVM bytecode, or JVM runtime behavior.

## Inspect

- Read Maven or Gradle configuration, toolchains, dependency locks, module
  settings, JVM flags, serialization mappings, and representative tests.

## Ask when unresolved

- Which Java language level, JDK vendor and version, JVM settings, target
  runtime, and dependency versions apply?

- How do threads, virtual threads, interruption, resource lifetime,
  serialization, and memory visibility cross the boundary?

- Which runtime or deployment differences materially change future reviews: JDK
  vendor and version, JVM flags and collector, container limits, application
  server or standalone process, architecture, native libraries, packaging, and
  shutdown?

## Record

Map durable Java version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
