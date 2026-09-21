---
name: gd-express
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Express engineering work for middleware order, async error propagation, request validation, authorization, resource limits, proxy behavior, and shutdown risks."
---

# Express GrumpyDev review

## Quick checks

- Read application setup, Express and Node versions, routers, middleware order,
  validation, authentication, proxy settings, server timeouts, and integration
  tests.

- Trace request data, async handlers, errors, streams, uploads, downstream
  calls, background work, and shutdown.

Watch especially for middleware that falls through or sends twice, rejected
promises or callback failures that are not forwarded under the selected Express
version and wrapper conventions, global request state, body and proxy defaults
treated as security controls, and CPU or synchronous I/O blocking the event
loop.

- Assess auth bypass, spoofed client identity, unhandled async failure, or
  unbounded request input under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Express specialist.

## Verdict context

State middleware and validation boundaries, async error behavior, resource
limits, proxy assumptions, shutdown behavior, and HTTP integration evidence.
