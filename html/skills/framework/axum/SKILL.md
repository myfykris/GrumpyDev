---
name: gd-axum
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Axum engineering work for router state, extractor limits, Tower middleware, async blocking, error responses, cancellation, and graceful shutdown risks."
---

# Axum GrumpyDev review

## Quick checks

- Establish the exact Axum, Rust, Tokio, Tower, and target-platform versions.

- Read router composition, state types, extractors, Tower layers, body limits,
  server configuration, dependency clients, and integration tests.

Watch especially for inconsistent extractor rejections, blocking work inside
async handlers, shared-state guards held across await points, body consumption
by middleware, and graceful shutdown that stops accepting work without draining
it.

- Assess unsafe shared state, unbounded request work, or lost critical work
  during shutdown under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Axum specialist.

## Verdict context

State router-state ownership, layer ordering, resource bounds, cancellation and
shutdown behavior, and server-level evidence.
