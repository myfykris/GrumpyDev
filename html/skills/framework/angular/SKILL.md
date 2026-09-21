---
name: gd-angular
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Angular engineering work for dependency injection scope, signals and RxJS ownership, change detection, routing, forms, rendering, accessibility, and build risks."
---

# Angular GrumpyDev review

## Quick checks

- Read Angular and TypeScript versions, bootstrap and provider configuration,
  routes, state and data libraries, rendering mode, forms, build targets, and
  tests.

- Trace service lifetimes, signals, observables, subscriptions, navigation,
  server and browser boundaries, and loading or error states.

Watch especially for mutable singleton-service state, duplicated providers with
surprising scope, leaked subscriptions, change-detection assumptions that fail
outside the expected zone or signal boundary, and route guards mistaken for
server-side authorization.

- Assess client-side authorization as the only control, leaked long-lived
  subscriptions, or broken core hydration under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Angular specialist.

## Verdict context

State provider and state ownership, reactive cleanup, routing and rendering
assumptions, user-visible failure states, and production-build evidence.
