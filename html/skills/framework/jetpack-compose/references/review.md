# Jetpack Compose full-review guidance

## Operating conditions

Establish the project target: Compose, Kotlin, and Android plugin versions, minimum and target
SDK, navigation, state and dependency injection model, lifecycle owners, saved-state policy,
accessibility targets, supported form factors, and test devices.

## Failure patterns

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

## Verification to run or specify in the plan

- Run instrumentation and UI tests on supported API levels, screen sizes, font scales, input
  modes, and process recreation.
- Use recomposition and layout diagnostics on representative screens with production-like data
  and release settings.
- Exercise denied permissions, offline data, deep links, back navigation, state restoration,
  and View interop.
