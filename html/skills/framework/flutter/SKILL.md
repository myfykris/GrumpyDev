---
name: flutter
description: Review Flutter plans for widget and application state, lifecycle, navigation, asynchronous work, platform plugins, accessibility, performance, and release risks. Use when a Dart plan changes Flutter applications, widgets, routes, state management, or native integration.
---

# Flutter plan review

Apply this guidance alongside the core GrumpyDev review and the `dart` skill.

## Inspect evidence

- Read Flutter and Dart versions, supported platforms, navigation, state and
  data libraries, plugin configuration, persistence, permissions, and tests.
- Trace widget and app lifecycle, state ownership, futures and streams,
  background work, platform channels, navigation, and offline or error states.

## Establish the operating model

Establish the project target: Flutter and Dart versions, target platforms and
minimum versions, state and navigation libraries, build flavors, plugin set,
signing boundary, and distribution channels. The changed boundary must define:
Widget and element lifecycle, state ownership, async context, navigation,
isolates, plugins, platform channels, rendering, accessibility, persistence, and
release modes.

Assign lifecycle, state, dependency, persistence, and security ownership for
Widget and element lifecycle, state ownership, async context, navigation,
isolates, plugins. Prove platform channels, rendering, accessibility,
persistence, release modes through startup, invalid or denied work,
cancellation, background execution, mixed versions, shutdown, rollback, and
recovery.

## Challenge the plan

### Recurring traps

Watch especially for side effects during build, use of a stale BuildContext
after asynchronous work, undisposed controllers and subscriptions, two state
owners for the same value, and mobile-only testing that misses desktop, web,
accessibility, or restoration behavior.

- Require one owner for each state value and dispose controllers, subscriptions,
  focus nodes, animations, and platform resources.
- Check stale BuildContext use, work after disposal, duplicate requests,
  navigation restoration, and app background or resume behavior.
- Verify plugin support, permissions, storage, networking, and platform-channel
  contracts on every target platform.
- Require complete loading, empty, stale, offline, denied, error, and retry
  states with keyboard and screen-reader behavior.
- Use profile or release evidence for frame time, memory, startup, binary size,
  tree shaking, and native build behavior.

## Verify the claims

- Verify these behaviors through the actual Flutter lifecycle and production
  pipeline: Widget and element lifecycle, state ownership, async context,
  navigation, isolates, plugins. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: platform channels, rendering,
  accessibility, persistence, release modes. Exercise invalid input, denied
  access, cancellation, dependency failure, concurrent work, shutdown, and
  mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Flutter and Dart versions, target platforms, rendering constraints, and
  state approach apply?
- How are widget lifetime, navigation, async cancellation, offline state,
  accessibility, and platform channels handled?

## Calibrate findings

- Treat cross-user state leakage, lost critical offline data, or a core flow
  inaccessible on a supported platform as critical.
- Downgrade when lifecycle, platform, state restoration, and accessibility
  behavior are covered by representative tests.

## Add to the verdict

State platform targets, state and lifecycle ownership, plugin boundaries,
user-visible failure states, accessibility, and release evidence.
