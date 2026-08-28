# React Native standard review

## Inspect additional evidence

- Trace application lifecycle, navigation, deep links, background work, permissions, storage,
  networking, and offline behavior.
- Inspect list rendering, image use, thread work, memory, accessibility, signing, and
  production bundle configuration.

## Establish the operating model

Establish the project target: React Native and React versions, New Architecture status,
JavaScript engine, target platforms and OS versions, native modules, navigation, state
ownership, build variants, permissions, signing, updates, and release channels.

The plan must separate JavaScript-thread work, UI-thread work, native module work, and durable
platform services. A library claim is not enough without compatibility on each target
architecture and OS.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Build signed release variants for each platform and architecture, then test on representative
  physical devices.
- Exercise native module failure, background transitions, process termination, low memory,
  offline launch, and deep links.
- Profile JavaScript and UI threads, startup, memory, lists, and animations with
  production-like data.

## Ask when evidence is missing

- Which React Native, React, engine, architecture, platforms, OS versions, and native modules
  apply?
- How are threads, lifecycle, navigation, permissions, offline state, accessibility, signing,
  and release behavior handled?

## Calibrate findings

- Downgrade when architecture compatibility, lifecycle, native boundaries, accessibility, and
  real-device release evidence are complete.
