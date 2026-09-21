---
name: gd-cpp
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review C++ engineering work for ownership, lifetime, exception safety, templates, ABI, concurrency, build configuration, and native dependency risks."
---

# C++ GrumpyDev review

## Quick checks

- Read build definitions, compiler and language-standard settings, public
  headers, dependency configuration, sanitizer settings, and representative
  tests.

- Trace object ownership, move and copy behavior, exception boundaries, thread
  use, shared state, and C or other-language interfaces.

Watch especially for mixed raw and smart ownership, iterator or reference
invalidation, objects used outside their lifetime, static initialization order,
exceptions crossing incompatible boundaries, unsynchronized shared state, and
one-definition-rule violations across builds.

- Assess reachable undefined behavior, ownership corruption, ABI mismatch, or
  data race under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the C++ specialist.

## Verdict context

State the ownership and exception model, ABI and toolchain constraints,
concurrency hazards, compatibility impact, and native evidence required for
approval.
