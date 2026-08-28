# Scala standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when runtime and effects are bounded and binary, concurrency,
  serialization, and failure tests cover the path.
