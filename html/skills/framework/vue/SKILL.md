---
name: gd-vue
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Vue engineering work for reactive state ownership, composable lifecycle, routing, rendering, asynchronous work, accessibility, and build risks."
---

# Vue GrumpyDev review

## Quick checks

- Read Vue and build-tool versions, component API style, router, store and data
  libraries, rendering mode, plugins, configuration, and tests.

- Trace props, emits, reactive state, watchers, composables, subscriptions,
  navigation, data requests, and component disposal.

Watch especially for reactivity lost through destructuring, watchers or effects
that outlive their owner, computed values with side effects, unstable keys,
server-rendered state leaking between requests, hydration mismatches, and store
state duplicated outside its authority.

- Assess cross-user SSR state leakage, client-only authorization, or an
  inaccessible core flow under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Vue specialist.

## Verdict context

State reactive state ownership, lifecycle cleanup, routing and rendering
assumptions, user-visible failure states, and production-build evidence.
