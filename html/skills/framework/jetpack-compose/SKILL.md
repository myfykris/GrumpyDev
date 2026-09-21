---
name: gd-jetpack-compose
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Jetpack Compose engineering work for state ownership, recomposition, effects, navigation, lifecycle, persistence, accessibility, performance, and platform integration."
---

# Jetpack Compose GrumpyDev review

## Quick checks

- Read Compose BOM and compiler compatibility, Kotlin and Android plugin versions, navigation,
  state, and dependency injection choices.

- Trace state ownership, snapshot state, flows, effects, lifecycle collection, saved state, and
  process recreation.

Watch especially for unstable parameters causing broad recomposition, effects
keyed incorrectly, flows collected outside lifecycle, list items without stable
keys, process death ignored, and clickable visuals with incomplete semantics.

- Assess inaccessible core flows, lost committed user data, cross-user state, or permission
  abuse under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Jetpack Compose
specialist.

## Verdict context

State UI and durable state owners, effect lifecycle, restoration behavior, semantics, device
coverage, and release measurements.
