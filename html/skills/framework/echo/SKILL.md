---
name: gd-echo
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Echo framework engineering work for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks."
---

# Echo GrumpyDev review

## Quick checks

- Establish the exact Go, Echo, server, and deployment versions or modes.

- Read server setup, routes, middleware order, binders and validators, context
  use, limits, dependency clients, shutdown, and integration tests.

Watch especially for middleware-order changes, binders accepting fields that
callers must not control, request contexts retained after the request, blocking
handlers, partial responses followed by error handling, and proxy headers
trusted without an explicit proxy boundary.

- Assess mass assignment, auth-order bypass, unbounded input, or shutdown data
  loss under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Echo specialist.

## Verdict context

State context and request ownership, middleware order, binding controls, timeout
and shutdown behavior, and end-to-end HTTP evidence.
