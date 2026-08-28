# Swift standard review

## Establish the operating model

Establish the project target: Swift and toolchain versions, Apple or server
targets, deployment versions, strict concurrency mode, package manager,
architectures, interop boundaries, and distribution form. The changed boundary
must define: Swift version semantics, ownership and value behavior, optionals,
errors, structured concurrency, actors and isolation, Sendable, ABI, packages,
Objective-C and C interop, and platform lifecycle.

Define ownership, errors, cancellation, and concurrency for Swift version
semantics, ownership and value behavior, optionals, errors, structured
concurrency, actors and isolation. Verify version, package, native,
serialization, and artifact compatibility for Sendable, ABI, packages,
Objective-C and C interop, platform lifecycle across every declared target and
rollback path.

## Challenge the reviewed work

### Recurring traps

- Require structured task ownership, cancellation, actor isolation, and a
  defined boundary for main-thread work.
- Check force unwraps, implicitly unwrapped optionals, unchecked Sendable
  conformance, escaping closures, and continuation completion.
- Verify API availability, platform permissions, background execution, and
  lifecycle behavior on every supported OS version.
- Treat Objective-C nullability, memory ownership, and C pointers as runtime
  boundaries outside Swift safety guarantees.
- Demand device and release-build tests for concurrency, persistence migration,
  low-memory behavior, and background transitions.

## Verify the claims

- Verify these behaviors through the declared Swift compiler and runtime
  targets: Swift version semantics, ownership and value behavior, optionals,
  errors, structured concurrency, actors and isolation. Use the real compiler or
  interpreter and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: Sendable, ABI, packages, Objective-C
  and C interop, platform lifecycle. Exercise boundary values, encoding,
  cancellation, resource exhaustion, concurrency, dependency failure, and
  termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Swift language, compiler, OS, deployment target, package, and
  concurrency versions apply?
- How do actors, tasks, cancellation, sendability, ownership, errors, and
  Objective-C interop cross the boundary?

## Calibrate findings

- Downgrade when isolation is local and compiler checks, target-version,
  concurrency, interop, and failure tests cover it.
