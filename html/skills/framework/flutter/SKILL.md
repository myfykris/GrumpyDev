---
name: gd-flutter
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Flutter engineering work for widget and application state, lifecycle, navigation, asynchronous work, platform plugins, accessibility, performance, and release risks."
---

# Flutter GrumpyDev review

## Quick checks

- Read Flutter and Dart versions, supported platforms, navigation, state and
  data libraries, plugin configuration, persistence, permissions, and tests.

- Trace widget and app lifecycle, state ownership, futures and streams,
  background work, platform channels, navigation, and offline or error states.

Watch especially for side effects during build, use of a stale BuildContext
after asynchronous work, undisposed controllers and subscriptions, two state
owners for the same value, and mobile-only testing that misses desktop, web,
accessibility, or restoration behavior.

- Assess cross-user state leakage, lost critical offline data, or a core flow
  inaccessible on a supported platform under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Flutter specialist.

## Verdict context

State platform targets, state and lifecycle ownership, plugin boundaries,
user-visible failure states, accessibility, and release evidence.
