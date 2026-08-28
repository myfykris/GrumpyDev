# Objective-C standard review

## Inspect additional evidence

- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: Compiler and language mode, ARC policy, target
macOS versions, frameworks, Swift bridging, Objective-C++ use, architectures,
and deployment form. The changed boundary must define: Objective-C runtime, ARC
and manual ownership boundaries, messaging, nullability, categories, blocks, KVO
and notifications, Swift bridging, C and C++ interop, exceptions, ABI, and
concurrency.

Define ownership, errors, cancellation, and concurrency for Objective-C runtime,
ARC and manual ownership boundaries, messaging, nullability, categories, blocks.
Verify version, package, native, serialization, and artifact compatibility for
KVO and notifications, Swift bridging, C and C++ interop, exceptions, ABI,
concurrency across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

- Treat nullable messaging behavior as a compatibility property, not a
  validation strategy. Require explicit nullability at public and Swift-facing
  boundaries and verify the behavior of collection contents, out parameters, and
  error channels.
- Check block capture and copy behavior, retain cycles, weak-to-strong
  promotion, callback queue, and cancellation. A weak reference prevents a cycle
  but can silently discard required work.
- Confine UI and non-thread-safe framework objects to their required executor.
  Prove synchronization for mutable shared objects rather than assuming property
  atomicity protects a multi-step invariant.

## Verify the claims

- Build every supported architecture and deployment target with warnings treated
  according to project policy.
- Run ownership, address, undefined-behavior, thread, and zombie diagnostics
  where they can represent the boundary.
- Exercise nil, observer removal, callback cancellation, autorelease pressure,
  bridging, and mixed Swift/Objective-C call paths.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Compiler and
language mode, ARC policy, target macOS versions, frameworks, Swift bridging,
Objective-C++ use, architectures, and deployment form. For the changed boundary,
ask only about unresolved Objective-C runtime, ARC and manual ownership
boundaries, messaging, nullability, categories, blocks, KVO and notifications,
Swift bridging, C and C++ interop, exceptions, ABI, and concurrency when the
answer can change the verdict or implementation.

## Calibrate findings

- Treat unsupported runtime or compiler assumptions, undefined behavior,
  resource corruption, or an ABI boundary that can fail on a supported target as
  material when the reviewed work depends on it and lacks either a safe design or
  credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
