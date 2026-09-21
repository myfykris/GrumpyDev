---
name: gd-ktor
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Ktor engineering work for plugin order, coroutine ownership, request validation, serialization, authentication, client and server lifecycle, and deployment risks."
---

# Ktor GrumpyDev review

## Quick checks

- Read application modules, installed plugins and order, routing, content
  negotiation, authentication, coroutine dispatchers, client configuration, and
  tests.

- Trace calls, cancellation, blocking work, resources, serialization, errors,
  streaming, background tasks, and shutdown.

Watch especially for plugin installation order, coroutine scopes that outlive
requests or the application, blocking I/O on constrained dispatchers,
content-negotiation mismatches, route-scoped authentication gaps, and shutdown
that cancels work without reconciliation.

- Assess auth plugin bypass, blocked event loops, or lost structured cancellation
  on a critical path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Ktor specialist.

## Verdict context

State plugin ordering, coroutine and resource ownership, serialization contract,
resource limits, engine assumptions, and deployment evidence.
