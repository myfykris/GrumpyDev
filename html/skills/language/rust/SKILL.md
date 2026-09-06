---
name: rust
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Rust engineering work for ownership boundaries, unsafe code, async execution, trait and feature behavior, FFI, error handling, dependency features, and deployment risks."
---

# Rust GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Establish the Rust edition, minimum supported Rust version, Cargo version,
  target toolchains, and supported feature combinations.

- Read Cargo manifests and locks, feature flags, target triples, unsafe modules,
  async runtime setup, build scripts, FFI declarations, and representative
  tests.

Watch especially for unsafe blocks whose invariants are undocumented, incorrect
Send or Sync claims, async work cancelled at arbitrary await points, panics
crossing FFI boundaries, self-referential or pinned state moved incorrectly,
interior mutability hiding contention, and untested feature combinations.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsound unsafe or FFI behavior, reachable data race, or cancellation
  that violates a durable invariant as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Rust evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State unsafe invariants, async ownership, feature and target assumptions, panic
and FFI behavior, and specialized verification evidence.
