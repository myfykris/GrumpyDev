---
name: gd-gin
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Gin engineering work for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks."
---

# Gin GrumpyDev review

## Quick checks

- Establish the exact Go, Gin, server, and deployment versions or modes.

- Read engine setup, routes and groups, middleware order, binders and
  validators, limits, dependency clients, server settings, and integration
  tests.

Watch especially for binding without explicit validation, mass assignment into
privileged fields, request contexts used from later goroutines, middleware-order
changes, abort and response-write sequencing, and client addresses accepted from
untrusted proxy headers.

- Assess auth-order bypass, unsafe binding, data races, or unbounded request work
  under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Gin specialist.

## Verdict context

State request and context ownership, middleware coverage, binding controls,
proxy trust, shutdown behavior, and HTTP integration evidence.
