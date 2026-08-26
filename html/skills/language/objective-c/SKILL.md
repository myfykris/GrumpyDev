---
name: objective-c
description: Review Objective-C plans for runtime dispatch, object ownership, nullability, blocks, categories, KVO, interoperability, ABI, and concurrency risks. Use when a plan changes Objective-C or Objective-C++ code, Apple framework integration, or Swift bridging.
---

# Objective-C plan review

Apply this guidance alongside the core GrumpyDev review and the `c`, `cpp`,
`swift`, `macos`, and applicable Apple UI framework skills. Select only
companions that match the plan's real boundaries. Verify behavior against the
project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect compiler and target settings, headers, module maps, ownership
  annotations, bridging headers, categories, blocks, observers, native
  boundaries, and build products.
- Read the declarations and produced binaries in addition to source. Compiler
  defaults, language modes, optimization, architecture, linker behavior, and
  foreign dependencies are part of the program.
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

## Challenge the plan

### Recurring traps

Watch especially for messages to nil masking missing work, selector-based
behavior escaping compiler checks, retain cycles through blocks or delegates,
KVO and notification teardown, Core Foundation bridging ownership, exceptions
crossing language boundaries, and Objective-C++ ABI assumptions.

- Follow ownership across Core Foundation, Objective-C, C++, blocks, callbacks,
  autorelease pools, weak references, and asynchronous work. Bridging syntax
  does not by itself prove which side owns a value.
- Treat nullable messaging behavior as a compatibility property, not a
  validation strategy. Require explicit nullability at public and Swift-facing
  boundaries and verify the behavior of collection contents, out parameters, and
  error channels.
- Review selectors, dynamic lookup, forwarding, swizzling, categories,
  associated objects, and runtime registration for collision, ordering, and
  discoverability. A category cannot safely add ordinary instance storage.
- Match KVO and notification registration to removal, lifetime, thread,
  reentrancy, and payload contracts. Check automatic versus manual KVO and
  whether an observer can see a partly updated invariant.
- Check block capture and copy behavior, retain cycles, weak-to-strong
  promotion, callback queue, and cancellation. A weak reference prevents a cycle
  but can silently discard required work.
- Keep Objective-C exceptions out of ordinary recoverable control flow and
  define how C++, Swift, C callbacks, and error-return conventions cross the
  boundary without unwinding through an incompatible ABI.
- Validate method signatures, lightweight generics, modules, symbols, deployment
  availability, architecture slices, and Swift import names across every shipped
  binary.
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
- Inspect the produced symbols, modules, architecture slices, entitlements, and
  minimum operating-system metadata.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Compiler and
language mode, ARC policy, target macOS versions, frameworks, Swift bridging,
Objective-C++ use, architectures, and deployment form. For the changed boundary,
ask only about unresolved Objective-C runtime, ARC and manual ownership
boundaries, messaging, nullability, categories, blocks, KVO and notifications,
Swift bridging, C and C++ interop, exceptions, ABI, and concurrency when the
answer can change the verdict or implementation.

## Calibrate findings

- Treat memory corruption, use-after-free, ABI breakage, cross-thread UI access,
  or an ownership error that can corrupt persistent state as critical or high
  according to blast radius and realistic likelihood.
- Treat unsupported runtime or compiler assumptions, undefined behavior,
  resource corruption, or an ABI boundary that can fail on a supported target as
  material when the plan depends on it and lacks either a safe design or
  credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
runtime messaging, ARC and manual ownership boundaries, nullability, categories,
blocks, KVO and notifications, Swift bridging, C and C++ interoperability,
exceptions, ABI, and concurrency, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
