---
name: gd-javascript
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review JavaScript engineering work for runtime coercion, asynchronous control flow, module compatibility, dependency behavior, browser or Node differences, validation, and build risks."
---

# JavaScript GrumpyDev review

## Quick checks

- Read package metadata, lockfiles, runtime and browser targets, module type,
  bundler settings, lint rules, generated artifacts, and representative tests.

- Trace external data, promises, events, timers, shared state, cleanup, module
  loading, and browser or Node API usage.

Watch especially for coercion and truthiness changing control flow, promises
that are neither awaited nor returned, shared mutation across callbacks, CPU
work blocking the event loop, prototype or property-name hazards, floating-point
assumptions, catastrophic regular expressions, dynamic code evaluation, and
local-time conversions.

- Assess unhandled async failure, prototype or input abuse, event-loop
  starvation, or cross-user state leakage under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the JavaScript
specialist.

## Verdict context

State runtime targets, validation boundaries, async ownership, module format,
compatibility assumptions, and built-artifact evidence.
