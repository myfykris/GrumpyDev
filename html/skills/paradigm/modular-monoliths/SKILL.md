---
name: gd-modular-monoliths
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review modular-monolith engineering work for enforceable boundaries, dependency direction, data ownership, transaction scope, deployment coupling, and extraction seams."
---

# Modular monolith GrumpyDev review

## Quick checks

- Read module APIs, dependency rules, build layout, database ownership,
  transaction boundaries, background work, and architecture tests.

- Trace calls and data access that cross modules, including shortcuts through
  shared helpers, tables, and internal types.

Watch especially for package names without enforceable boundaries, cyclic
dependencies, shared mutable tables with no owning module, framework-wide
dependency injection bypassing module APIs, global events with unclear delivery
rules, and speculative extraction driving needless indirection.

- Assess cyclic ownership or unenforced writes that allow modules to violate core
  invariants under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Modular monolith
specialist.

## Verdict context

State module boundaries, enforcement mechanism, data ownership, allowed
coupling, transaction scope, and realistic extraction seams.
