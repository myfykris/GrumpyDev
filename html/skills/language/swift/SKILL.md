---
name: swift
description: Review Swift engineering plans for ownership, concurrency, actor isolation, optionals, error handling, platform availability, Objective-C interoperability, and application lifecycle risks. Use when a plan changes Swift applications, packages, services, or Apple-platform code.
---

# Swift plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read package or project settings, Swift and platform targets, concurrency
  checks, entitlements, generated code, bridging headers, and representative
  tests.
- Trace tasks, actors, continuations, delegates, resources, application
  lifecycle, persistence, and Objective-C or C boundaries.

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

## Challenge the plan

### Recurring traps

Watch especially for ARC cycles, copy-on-write values assumed to be cheap or
isolated, actor isolation bypassed at legacy boundaries, tasks that ignore
cancellation, forced optionals on external data, availability checks that miss
linked symbols, and bridging that changes ownership or nullability.

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

- Treat actor isolation violation, use-after-lifetime through interop, or
  cancellation that corrupts durable state as critical.
- Downgrade when isolation is local and compiler checks, target-version,
  concurrency, interop, and failure tests cover it.

## Add to the verdict

State platform targets, concurrency and actor model, unsafe interoperability
boundaries, lifecycle guarantees, and device-level evidence.
