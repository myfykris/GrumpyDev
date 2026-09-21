# Objective-C full-review guidance

## Operating conditions

Establish the project target: Compiler and language mode, ARC policy, target
Apple platform versions, frameworks, Swift bridging, Objective-C++ use,
architectures, and deployment form. The changed boundary must define:
Objective-C runtime, ARC and manual ownership boundaries, messaging,
nullability, categories, blocks, KVO and notifications, Swift bridging, C and
C++ interop, exceptions, ABI, and concurrency.

## Failure patterns

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

## Verification to run or specify in the plan

- Build every supported architecture and deployment target with warnings treated
  according to project policy.
- Run ownership, address, undefined-behavior, thread, and zombie diagnostics
  where they can represent the boundary.
- Exercise nil, observer removal, callback cancellation, autorelease pressure,
  bridging, and mixed Swift/Objective-C call paths.
