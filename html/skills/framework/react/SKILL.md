---
name: gd-react
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review React engineering work for state ownership, effect lifecycle, rendering, accessibility, performance, hydration, and user-experience failure risks."
---

# React GrumpyDev review

## Quick checks

- Establish React and framework versions, rendering mode, routing, data and
  form libraries, build output, tests, and supported browsers.
- Trace ownership of server data, URL state, forms, local interaction state,
  caches, and cross-page state.
- Challenge duplicated derived state, stale closures, incomplete effect
  dependencies, unstable keys, async results applied after ownership changes,
  non-idempotent effects, and client checks mistaken for authorization.
- Inspect unsafe HTML or URL sinks, browser secrets, cross-user cache or
  hydration leakage, loading and failure states, keyboard flow, focus, and
  accessible semantics.

## References

- For a material React effect or uncertainty in a full review, read
  [review.md](references/review.md).
- For server rendering, server components, hydration, streaming, Suspense, or
  serialized initial data, read
  [server-rendering-and-hydration.md](references/server-rendering-and-hydration.md).
- For untrusted content, DOM sinks, browser storage, CSP, framing, or
  cross-origin behavior, read
  [untrusted-content-and-browser-security.md](references/untrusted-content-and-browser-security.md).

## Verdict context

State each flow's owner, server and client trust boundaries, user-visible
failure states, accessibility evidence, and behavior-level tests.
