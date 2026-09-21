---
name: gd-actix-web
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Actix Web engineering work for worker state, extractor behavior, async blocking, middleware order, cancellation, error responses, and graceful shutdown risks."
---

# Actix Web GrumpyDev review

## Quick checks

- Establish the exact Actix Web, Rust, Tokio, and target-platform versions.

- Read application construction, worker configuration, shared state types,
  extractors, middleware, route registration, server settings, and integration
  tests.

Watch especially for synchronous work blocking Actix workers, extractors that
turn domain errors into accidental responses, shared-state locks held across
await points, middleware ordering changes, and shutdown paths that abandon
in-flight work.

- Assess blocking or unbounded work on workers, unsafe shared state, or shutdown
  data loss under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Actix Web
specialist.

## Verdict context

State worker and state ownership, blocking boundaries, middleware and extractor
controls, shutdown behavior, and end-to-end server evidence.
