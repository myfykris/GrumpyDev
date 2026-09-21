---
name: gd-htmx
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review htmx engineering work for hypermedia contracts, fragment and full-page responses, swaps, request ordering, history, caching, security, and accessibility."
---

# htmx GrumpyDev review

## Quick checks

- Read the htmx version, extensions, configuration, server framework, template system, and
  response conventions.

- Map each request to its trigger, method, parameters, target, swap, synchronization,
  validation, and failure behavior.

Watch especially for the same URL caching both fragments and full pages,
race-prone requests overwriting newer state, sensitive HTML entering history
storage, injected htmx attributes becoming executable behavior, and swaps losing
focus or form errors.

- Assess stored sensitive fragments, forged state-changing requests, or executable untrusted
  HTML under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the htmx specialist.

## Verdict context

State fragment and full-page contracts, request ordering, cache keys, history policy, security
controls, focus behavior, and browser tests.
