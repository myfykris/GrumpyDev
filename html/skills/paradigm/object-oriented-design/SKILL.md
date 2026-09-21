---
name: gd-object-oriented-design
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review object-oriented design engineering work for ownership, invariants, mutability, inheritance, polymorphism, dependency direction, and test seams."
---

# Object-oriented design GrumpyDev review

## Quick checks

- Read object responsibilities, constructors, state transitions, public methods,
  inheritance trees, interfaces, dependencies, and tests.

- Trace who owns mutable state, who may change it, and how invariants survive
  callbacks, exceptions, persistence, and concurrency.

Watch especially for inheritance used only for reuse, god objects, mutable
aliases crossing ownership boundaries, subtype behavior that violates caller
expectations, temporal coupling hidden behind setters, domain behavior displaced
into services, and accessors that trigger surprising I/O.

- Assess split ownership or polymorphism that can violate a core invariant or
  resource lifecycle under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Object-oriented
design specialist.

## Verdict context

State object ownership, protected invariants, mutation boundaries, polymorphism
justification, dependency direction, and test evidence.
