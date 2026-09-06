---
name: jetpack-compose
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Jetpack Compose engineering work for state ownership, recomposition, effects, navigation, lifecycle, persistence, accessibility, performance, and platform integration."
---

# Jetpack Compose GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `kotlin`, `android` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read Compose BOM and compiler compatibility, Kotlin and Android plugin versions, navigation,
  state, and dependency injection choices.

- Trace state ownership, snapshot state, flows, effects, lifecycle collection, saved state, and
  process recreation.

Watch especially for unstable parameters causing broad recomposition, effects
keyed incorrectly, flows collected outside lifecycle, list items without stable
keys, process death ignored, and clickable visuals with incomplete semantics.

Lean mode is insufficient when this material severity condition may apply:

- Treat inaccessible core flows, lost committed user data, cross-user state, or permission
  abuse as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Jetpack Compose evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State UI and durable state owners, effect lifecycle, restoration behavior, semantics, device
coverage, and release measurements.
