---
name: gd-c
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review C engineering work for memory safety, ownership, ABI, undefined behavior, concurrency, portability, build, and native dependency risks."
---

# C GrumpyDev review

## Quick checks

- Read build files, compiler flags, target platforms, public headers, allocation
  conventions, sanitizer settings, and representative tests.

- Trace ownership, lifetime, bounds, error returns, cleanup paths, thread
  interaction, and data crossing ABI or hardware boundaries.

Watch especially for undefined behavior from lifetime, bounds, alignment,
aliasing, or signed arithmetic; silent integer conversions; ownership that
changes across error paths; struct layout assumed across ABI boundaries; and
signal handlers calling unsafe operations.

- Assess reachable undefined behavior, memory corruption, integer-controlled
  allocation, or unsafe concurrency under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the C specialist.

## Verdict context

State the ownership model, ABI assumptions, supported toolchains and targets,
undefined-behavior risks, cleanup behavior, and evidence from native tests or
analysis.
