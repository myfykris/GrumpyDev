---
name: gd-rust
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Rust engineering work for ownership boundaries, unsafe code, async execution, trait and feature behavior, FFI, error handling, dependency features, and deployment risks."
---

# Rust GrumpyDev review

## Quick checks

- Establish the Rust edition, minimum supported Rust version, Cargo version,
  target toolchains, and supported feature combinations.

- Read Cargo manifests and locks, feature flags, target triples, unsafe modules,
  async runtime setup, build scripts, FFI declarations, and representative
  tests.

Watch especially for unsafe blocks whose invariants are undocumented, incorrect
Send or Sync claims, async work cancelled at arbitrary await points, panics
crossing FFI boundaries, self-referential or pinned state moved incorrectly,
interior mutability hiding contention, and untested feature combinations.

- Assess unsound unsafe or FFI behavior, reachable data race, or cancellation
  that violates a durable invariant under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Rust specialist.

## Verdict context

State unsafe invariants, async ownership, feature and target assumptions, panic
and FFI behavior, and specialized verification evidence.
