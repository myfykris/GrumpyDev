# Java full-review guidance

## Operating conditions

Establish the project target: JDK vendor and versions, language and bytecode
target, JVM flags and GC, build tool, module use, container limits, native
dependencies, and supported platforms. The changed boundary must define: Java
and JVM semantics, memory model, threads and virtual threads, exceptions, class
loading, reflection, serialization, JNI, GC, resource lifecycle, modules,
bytecode compatibility, and container behavior.

## Failure patterns

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

## Verification to run or specify in the plan

- Run the packaged application on the supported JVMs with representative heap,
  GC, and container settings. Exercise reflective loading, module access,
  serialization, and JNI where the change affects them.
- Saturate affected executors and interrupt work during exceptions, timeouts,
  and shutdown. Check bounded queues, observable failures, and release of
  connections, files, and transaction state.

- Exercise hostile serialized types, external XML references, archive entries,
  dynamic lookup values, command options, expensive regular expressions, and
  parser limits where those boundaries exist.
