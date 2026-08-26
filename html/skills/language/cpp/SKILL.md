---
name: cpp
description: Review C++ engineering plans for ownership, lifetime, exception safety, templates, ABI, concurrency, build configuration, and native dependency risks. Use when a plan changes C++ applications, libraries, services, bindings, or toolchains.
---

# C++ plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read build definitions, compiler and language-standard settings, public
  headers, dependency configuration, sanitizer settings, and representative
  tests.
- Trace object ownership, move and copy behavior, exception boundaries, thread
  use, shared state, and C or other-language interfaces.

## Establish the operating model

Establish the project target: C++ standard, compiler and standard-library
versions, ABI targets, exception and RTTI policy, architectures, build system,
dependency manager, sanitizers, and deployment platforms. The changed boundary
must define: C++ standard, value and object lifetime, ownership, exceptions,
RTTI, templates, ODR, ABI, allocators, concurrency, atomics, modules, native
dependencies, and toolchain compatibility.

Define ownership, errors, cancellation, and concurrency for C++ standard, value
and object lifetime, ownership, exceptions, RTTI, templates, ODR. Verify
version, package, native, serialization, and artifact compatibility for ABI,
allocators, concurrency, atomics, modules, native dependencies, toolchain
compatibility across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for mixed raw and smart ownership, iterator or reference
invalidation, objects used outside their lifetime, static initialization order,
exceptions crossing incompatible boundaries, unsynchronized shared state, and
one-definition-rule violations across builds.

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

## Verify the claims

- Verify these behaviors through the declared C++ compiler and runtime targets:
  C++ standard, value and object lifetime, ownership, exceptions, RTTI,
  templates, ODR. Use the real compiler or interpreter and supported release
  modes rather than a development substitute.
- Exercise failure and edge behavior for: ABI, allocators, concurrency, atomics,
  modules, native dependencies, toolchain compatibility. Exercise boundary
  values, encoding, cancellation, resource exhaustion, concurrency, dependency
  failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which C++ standard, compiler, standard library, target ABI, and exception or
  RTTI settings apply?
- Who owns each object and resource across move, exception, concurrency, and
  binary boundaries?

## Calibrate findings

- Treat reachable undefined behavior, ownership corruption, ABI mismatch, or
  data race as critical.
- Downgrade when ownership is local and explicit and sanitizers, static
  analysis, ABI, and failure tests cover the path.

## Add to the verdict

State the ownership and exception model, ABI and toolchain constraints,
concurrency hazards, compatibility impact, and native evidence required for
approval.
