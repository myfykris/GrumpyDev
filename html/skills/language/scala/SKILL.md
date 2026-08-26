---
name: scala
description: Review Scala engineering plans for effect ownership, concurrency, type-level assumptions, Java interoperability, serialization, build compatibility, and distributed runtime risks. Use when a plan changes Scala services, libraries, streaming jobs, or JVM data systems.
---

# Scala plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read sbt or build configuration, Scala and JVM versions, effect or actor
  libraries, serialization settings, generated code, and representative tests.
- Trace effects, execution contexts, futures or fibers, blocking work, Java
  boundaries, implicits or givens, state, and shutdown.

## Establish the operating model

Establish the project target: Scala and JDK versions, build tool, major
libraries and effect system, binary compatibility target, runtime topology,
serialization stack, and deployment platform. The changed boundary must define:
Scala 2 and 3 differences, type and implicit behavior, JVM interop, effect
systems, futures and streams, concurrency, serialization, macros, binary
compatibility, and build graph.

Define ownership, errors, cancellation, and concurrency for Scala 2 and 3
differences, type and implicit behavior, JVM interop, effect systems, futures
and streams. Verify version, package, native, serialization, and artifact
compatibility for concurrency, serialization, macros, binary compatibility,
build graph across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for surprising implicit or given resolution, lazy
initialization under concurrency, futures using an unsuitable execution context,
strict and lazy collection behavior being confused, erased runtime types,
variance hiding unsafe assumptions, and binary incompatibility across library
versions.

- Require one effect and cancellation model; reject uncontrolled mixing of
  futures, blocking calls, actors, and multiple runtimes.
- Check execution-context starvation, unbounded parallelism, lost failures,
  resource scopes, and shutdown behavior.
- Verify binary and source compatibility across Scala versions, cross-built
  artifacts, Java consumers, and independently deployed nodes.
- Treat serialization of algebraic data types, implicits, reflection, and erased
  generics as runtime contracts that need tests.
- Demand production-like tests for backpressure, partitioning, retries, delivery
  semantics, and cluster upgrades when distributed frameworks apply.

## Verify the claims

- Verify these behaviors through the declared Scala compiler and runtime
  targets: Scala 2 and 3 differences, type and implicit behavior, JVM interop,
  effect systems, futures and streams. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: concurrency, serialization, macros,
  binary compatibility, build graph. Exercise boundary values, encoding,
  cancellation, resource exhaustion, concurrency, dependency failure, and
  termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Scala version, JVM, build tool, binary version, effect system, and
  dependency versions apply?
- How do effects, futures, cancellation, blocking, implicits, serialization, and
  Java interop cross the boundary?

## Calibrate findings

- Treat binary incompatibility, lost effect cancellation, dispatcher starvation,
  or unsafe shared state as critical.
- Downgrade when runtime and effects are bounded and binary, concurrency,
  serialization, and failure tests cover the path.

## Add to the verdict

State Scala and JVM targets, effect and execution model, binary compatibility,
serialization assumptions, and distributed failure evidence.
