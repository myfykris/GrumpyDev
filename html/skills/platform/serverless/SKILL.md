---
name: gd-serverless
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review serverless engineering work for event contracts, concurrency, cold starts, retries, idempotency, time limits, state, networking, permissions, and cost."
---

# Serverless GrumpyDev review

## Quick checks

- Establish the exact provider, service, runtime version, deployment mode,
  region, and provider limits.

- Read triggers, payloads, runtime settings, concurrency, timeouts, retries,
  destinations, permissions, network paths, dependencies, and cost estimates.

Watch especially for platform retries repeating effects, timeouts after an
external commit, reused instances retaining request state, cold starts ignored
in latency budgets, event-size and concurrency ceilings, local emulators hiding
managed behavior, and asynchronous destinations with no reconciliation owner.

- Assess retry-driven irreversible effects, privilege exposure, hard limit
  failure, or unbounded cost amplification under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Serverless
specialist.

## Verdict context

State trigger semantics, idempotency, concurrency bounds, latency evidence,
state and failure behavior, permissions, and cost model.
