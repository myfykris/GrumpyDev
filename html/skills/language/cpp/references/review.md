# C++ full-review guidance

## Operating conditions

Establish the project target: C++ standard, compiler and standard-library
versions, ABI targets, exception and RTTI policy, architectures, build system,
dependency manager, sanitizers, and deployment platforms. The changed boundary
must define: C++ standard, value and object lifetime, ownership, exceptions,
RTTI, templates, ODR, ABI, allocators, concurrency, atomics, modules, native
dependencies, and toolchain compatibility.

## Failure patterns

- Require RAII ownership and a defined lifetime for memory, locks, files,
  threads, callbacks, and foreign handles.
- Check exception guarantees and cleanup when construction, allocation,
  callbacks, or container operations fail partway through.
- Identify dangling views, iterator invalidation, data races, static
  initialization order, and ownership hidden by raw pointers.
- Verify template instantiations, feature flags, runtime library, compiler ABI,
  and binary compatibility for every supported consumer.
- Demand sanitizer and concurrency tests for unsafe boundaries instead of
  accepting type-level confidence alone.

## Verification to run or specify in the plan

- Where exceptions are enabled, inject them during construction and container
  updates; check that RAII cleanup preserves the promised exception guarantee.
  Exercise invalidated views, callbacks after owner destruction, and shared
  mutation with appropriate sanitizers.
- Build and run consumers of changed libraries using the supported compiler,
  standard-library, feature, exception, and RTTI settings. Check binary
  compatibility, not just whether the library itself compiles.
