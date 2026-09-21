# Scala full-review guidance

## Operating conditions

Establish the project target: Scala and JDK versions, build tool, major
libraries and effect system, binary compatibility target, runtime topology,
serialization stack, and deployment platform. The changed boundary must define:
Scala 2 and 3 differences, type and implicit behavior, JVM interop, effect
systems, futures and streams, concurrency, serialization, macros, binary
compatibility, and build graph.

## Failure patterns

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

## Verification to run or specify in the plan

- Compile and run consumers against the supported Scala and JDK artifact
  combinations. Exercise changed macros, implicit resolution, Java interop,
  and serialized data across independently deployed versions.
- Cancel streams or effects while dependencies block or fail. Check that
  execution contexts remain responsive, parallelism stays bounded, and
  resource scopes close on failure and shutdown.
