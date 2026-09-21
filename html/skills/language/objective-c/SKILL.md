---
name: gd-objective-c
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Objective-C engineering work for runtime dispatch, object ownership, nullability, blocks, categories, KVO, interoperability, ABI, and concurrency risks."
---

# Objective-C GrumpyDev review

## Quick checks

- Inspect compiler and target settings, headers, module maps, ownership
  annotations, bridging headers, categories, blocks, observers, native
  boundaries, and build products.

- Read the declarations and produced binaries in addition to source. Compiler
  defaults, language modes, optimization, architecture, linker behavior, and
  foreign dependencies are part of the program.

Watch especially for messages to nil masking missing work, selector-based
behavior escaping compiler checks, retain cycles through blocks or delegates,
KVO and notification teardown, Core Foundation bridging ownership, exceptions
crossing language boundaries, and Objective-C++ ABI assumptions.

- Inspect memory corruption, use-after-free, ABI breakage, cross-thread UI access,
  or an ownership error that can corrupt persistent state.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Objective-C
specialist.

- [Focused rules](references/dynamic-runtime-kvo-and-notifications.md):
  Read when the work changes selectors, forwarding,
  swizzling, categories, associated
  objects, runtime registration, KVO, notifications, observer lifetime, reentrancy, or
  dynamic callback ordering.
- [Focused rules](references/swift-c-cpp-and-abi-interop.md):
  Read when the work crosses Core Foundation, Swift, C,
  C++, Objective-C++, native
  callbacks, exception boundaries, modules, symbols, method signatures, architecture
  slices, or ABI and binary compatibility.

## Verdict context

State the runtime messaging, ARC and manual ownership boundaries, nullability,
categories, blocks, KVO and notifications, Swift bridging, C and C++
interoperability, exceptions, ABI, and concurrency, supporting evidence,
deployment or recovery limits, and unresolved material assumptions.
