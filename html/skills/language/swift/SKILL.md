---
name: gd-swift
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Swift engineering work for ownership, concurrency, actor isolation, optionals, error handling, platform availability, Objective-C interoperability, and application lifecycle risks."
---

# Swift GrumpyDev review

## Quick checks

- Read package or project settings, Swift and platform targets, concurrency
  checks, entitlements, generated code, bridging headers, and representative
  tests.

- Trace tasks, actors, continuations, delegates, resources, application
  lifecycle, persistence, and Objective-C or C boundaries.

Watch especially for ARC cycles, copy-on-write values assumed to be cheap or
isolated, actor isolation bypassed at legacy boundaries, tasks that ignore
cancellation, forced optionals on external data, availability checks that miss
linked symbols, and bridging that changes ownership or nullability.

- Assess actor isolation violation, use-after-lifetime through interop, or
  cancellation that corrupts durable state under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Swift specialist.

## Verdict context

State platform targets, concurrency and actor model, unsafe interoperability
boundaries, lifecycle guarantees, and device-level evidence.
