---
name: gd-blazor
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Blazor engineering work for rendering mode, circuit or WebAssembly state, dependency lifetimes, JavaScript interop, navigation, security, accessibility, and deployment risks."
---

# Blazor GrumpyDev review

## Quick checks

- Establish the exact .NET, Blazor, hosting, rendering, and deployment versions
  or modes.

- Read rendering-mode configuration, component routes, service lifetimes,
  authentication state, persistence, JavaScript interop, publish settings, and
  browser tests.

Watch especially for server-circuit state surviving longer than intended,
WebAssembly and server execution assumptions being mixed, prerendering that runs
initialization twice, JavaScript interop after component disposal, and UI
visibility mistaken for authorization.

- Assess server-only authorization missing, cross-circuit state leakage, or
  unrecoverable core interaction loss under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Blazor specialist.

## Verdict context

State rendering mode, state and service lifetimes, authorization boundary,
interop lifecycle, reconnection behavior, and published-browser evidence.
