---
name: gd-vapor
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Vapor engineering work for event-loop safety, request lifecycle, async ownership, Fluent transactions, validation, authentication, streaming, and deployment risks."
---

# Vapor GrumpyDev review

## Quick checks

- Read Vapor, Swift, and dependency versions, application configuration, routes,
  middleware, content models, Fluent schemas and migrations, clients, and tests.

- Trace requests, event loops, async tasks, database access, authentication,
  errors, streaming, jobs, and shutdown.

Watch especially for blocking work on event loops, incorrect bridging between
futures and async code, request-owned objects escaping their lifetime, Fluent
query or migration assumptions, streams without backpressure, and shutdown that
drops scheduled or in-flight work.

- Assess event-loop blocking, unsafe cross-request state, or lost critical work
  during shutdown under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Vapor specialist.

## Verdict context

State event-loop and task ownership, validation and authorization boundaries,
persistence safety, server lifecycle, and production evidence.
