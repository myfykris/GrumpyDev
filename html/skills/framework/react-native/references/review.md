# React Native full-review guidance

## Operating conditions

Establish the project target: React Native and React versions, New Architecture status,
JavaScript engine, target platforms and OS versions, native modules, navigation, state
ownership, build variants, permissions, signing, updates, and release channels.

## Failure patterns

- Require a version and architecture compatibility matrix for React Native, React, engine,
  native modules, and build tools.
- Trace every native boundary for thread, ownership, cancellation, serialization, error, and
  platform-specific behavior.
- Define startup, background, resume, termination, deep-link, offline, denied-permission, and
  state-restoration behavior.
- Check lists, images, animations, memory, bundle size, startup, and bridge traffic using
  release builds on real devices.
- Require semantic roles, labels, focus, screen-reader flow, text scaling, touch targets,
  keyboard, and reduced-motion behavior.

## Verification to run or specify in the plan

- Build signed release variants for each platform and architecture, then test on representative
  physical devices.
- Exercise native module failure, background transitions, process termination, low memory,
  offline launch, and deep links.
- Profile JavaScript and UI threads, startup, memory, lists, and animations with
  production-like data.
