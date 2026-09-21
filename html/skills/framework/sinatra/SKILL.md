---
name: gd-sinatra
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Sinatra engineering work for route and middleware order, application state, request validation, concurrency, sessions, errors, and deployment risks."
---

# Sinatra GrumpyDev review

## Quick checks

- Establish the exact Ruby, Sinatra, Rack, server, and deployment versions or
  modes.

- Read application style, Rack and middleware setup, routes, helpers, settings,
  session configuration, server model, dependency clients, and tests.

Watch especially for route and filter ordering, shared mutable state under
threaded servers, middleware-dependent session or proxy behavior, blocking
request handlers, error handlers that write after a response starts, and
development-server behavior assumed in production.

- Assess mutable cross-request state, auth-order bypass, or unsafe multi-threaded
  behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Sinatra specialist.

## Verdict context

State application and state model, middleware and route behavior, request trust
boundaries, concurrency assumptions, and production-server evidence.
