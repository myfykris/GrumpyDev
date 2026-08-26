---
name: react-native
description: Review React Native plans for architecture compatibility, native bridges, lifecycle, navigation, state, permissions, performance, accessibility, and release behavior. Use when a plan builds or changes React Native applications.
---

# React Native plan review

Apply this guidance alongside the core GrumpyDev review and the `react`, `javascript` and
`typescript` skills.

## Inspect evidence

- Read React Native, React, platform, engine, native module, navigation, and state-library
  versions.
- Identify New Architecture support, code generation, bridged or bridgeless modules, native
  build settings, and minimum OS levels.
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

## Challenge the plan

### Recurring traps

Watch especially for old native modules assumed compatible with the New Architecture,
JavaScript-thread stalls hidden by simulators, lifecycle work lost in background state,
navigation state duplicated, and platform permission differences ignored.

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

- Treat unsafe native memory behavior, secret exposure, inaccessible core flows, or lost
  committed data as critical.
- Downgrade when architecture compatibility, lifecycle, native boundaries, accessibility, and
  real-device release evidence are complete.

## Add to the verdict

State the architecture matrix, native boundaries, lifecycle and state owners, platform
differences, accessibility, and release evidence.
