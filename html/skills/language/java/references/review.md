# Java standard review

## Establish the operating model

Establish the project target: JDK vendor and versions, language and bytecode
target, JVM flags and GC, build tool, module use, container limits, native
dependencies, and supported platforms. The changed boundary must define: Java
and JVM semantics, memory model, threads and virtual threads, exceptions, class
loading, reflection, serialization, JNI, GC, resource lifecycle, modules,
bytecode compatibility, and container behavior.

Define ownership, errors, cancellation, and concurrency for Java and JVM
semantics, memory model, threads and virtual threads, exceptions, class loading,
reflection, serialization. Verify version, package, native, serialization, and
artifact compatibility for JNI, GC, resource lifecycle, modules, bytecode
compatibility, container behavior across every declared target and rollback
path.

## Challenge the reviewed work

### Recurring traps

- Require bounded executors, explicit queue policy, cancellation, and shutdown
  ownership for asynchronous work.
- Check resource and transaction cleanup for exceptions, interruption, timeout,
  and partial initialization.
- Verify source, bytecode, library, and runtime compatibility across every
  deployed JVM and consumer.
- Inspect equality, mutability, nullability, generic erasure, reflection, and
  serialization assumptions at trust boundaries.
- Reject native object deserialization from untrusted data. A class allowlist or
  serialization filter is defense in depth, not a reason to accept executable
  object graphs when a bounded data schema will work.
- Configure XML, transformation, and schema factories to disable external
  entities, external DTDs, and unintended network or filesystem resolution.
  Apply equivalent restrictions to archive, image, document, and template
  parsers.
- Keep untrusted values out of expression languages, script engines, dynamic
  class or naming lookups, template source, and shell command strings. Pass
  fixed executables and separated arguments with explicit option policy.
- Bound request, collection, parser, decompression, regular-expression,
  executor, and response work before memory allocation or thread occupation.
- Demand tests under production JVM settings for memory pressure, concurrency,
  graceful shutdown, and dependency conflicts.

## Verify the claims

- Verify these behaviors through the declared Java compiler and runtime targets:
  Java and JVM semantics, memory model, threads and virtual threads, exceptions,
  class loading, reflection, serialization. Use the real compiler or interpreter
  and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: JNI, GC, resource lifecycle, modules,
  bytecode compatibility, container behavior. Exercise boundary values,
  encoding, cancellation, resource exhaustion, concurrency, dependency failure,
  and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise hostile serialized types, external XML references, archive entries,
  dynamic lookup values, command options, expensive regular expressions, and
  parser limits where those boundaries exist.

## Ask when evidence is missing

- Which Java language level, JDK vendor and version, JVM settings, target
  runtime, and dependency versions apply?
- How do threads, virtual threads, interruption, resource lifetime,
  serialization, and memory visibility cross the boundary?

## Calibrate findings

- Downgrade when concurrency is isolated and target-JDK, resource, failure, and
  compatibility tests cover the path.
