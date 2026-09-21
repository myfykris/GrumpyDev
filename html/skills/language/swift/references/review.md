# Swift full-review guidance

## Operating conditions

Establish the project target: Swift and toolchain versions, Apple or server
targets, deployment versions, strict concurrency mode, package manager,
architectures, interop boundaries, and distribution form. The changed boundary
must define: Swift version semantics, ownership and value behavior, optionals,
errors, structured concurrency, actors and isolation, Sendable, ABI, packages,
Objective-C and C interop, and platform lifecycle.

## Failure patterns

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

## Verification to run or specify in the plan

- Run affected tasks through cancellation and actor hops; exercise
  continuations on both success and failure. Check state isolation and that
  callbacks cannot retain or update an owner beyond its intended lifetime.
- Build the supported deployment targets with the selected concurrency
  settings. Test release artifacts on the actual device or server targets,
  including changed Objective-C or C ownership and nullability boundaries.
