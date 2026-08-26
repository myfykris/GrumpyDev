---
name: jetpack-compose
description: Review Jetpack Compose plans for state ownership, recomposition, effects, navigation, lifecycle, persistence, accessibility, performance, and platform integration. Use when a plan creates or changes Android Compose UI.
---

# Jetpack Compose plan review

Apply this guidance alongside the core GrumpyDev review and the `kotlin`, `android` and
`web-accessibility` skills.

## Inspect evidence

- Read Compose BOM and compiler compatibility, Kotlin and Android plugin versions, navigation,
  state, and dependency injection choices.
- Trace state ownership, snapshot state, flows, effects, lifecycle collection, saved state, and
  process recreation.
- Inspect semantics, focus, input methods, adaptive layouts, back handling, permissions, and
  view interoperability.
- Review stability annotations, keys, lazy collections, derived state, previews, tests, and
  release performance evidence.

## Establish the operating model

Establish the project target: Compose, Kotlin, and Android plugin versions, minimum and target
SDK, navigation, state and dependency injection model, lifecycle owners, saved-state policy,
accessibility targets, supported form factors, and test devices.

Compose state is not automatically durable application state. The plan must distinguish
recomposition state, screen state, saved instance state, persisted data, and server authority.

## Challenge the plan

### Recurring traps

Watch especially for unstable parameters causing broad recomposition, effects keyed incorrectly,
flows collected outside lifecycle, list items without stable keys, process death ignored, and
clickable visuals with incomplete semantics.

- Require one state owner per value and explicit conversion among repository data, screen
  state, saved state, and UI state.
- Review every effect for keys, cancellation, restart behavior, stale captures, and lifecycle
  ownership.
- Test rotation, process death, background and resume, multi-window, navigation restoration,
  and interrupted work.
- Require semantic roles, labels, traversal, focus, touch targets, keyboard input, font
  scaling, and contrast evidence.
- Measure startup, frame timing, allocation, lazy-list behavior, and release builds before
  accepting performance claims.

## Verify the claims

- Run instrumentation and UI tests on supported API levels, screen sizes, font scales, input
  modes, and process recreation.
- Use recomposition and layout diagnostics on representative screens with production-like data
  and release settings.
- Exercise denied permissions, offline data, deep links, back navigation, state restoration,
  and View interop.

## Ask when evidence is missing

- Which Compose, Kotlin, Android plugin, SDK, navigation, state, and dependency injection
  versions apply?
- How do state, effects, process recreation, accessibility, adaptive layouts, permissions, and
  performance behave?

## Calibrate findings

- Treat inaccessible core flows, lost committed user data, cross-user state, or permission
  abuse as critical.
- Downgrade when lifecycle, saved state, effects, semantics, adaptive layout, and release
  performance are tested.

## Add to the verdict

State UI and durable state owners, effect lifecycle, restoration behavior, semantics, device
coverage, and release measurements.
