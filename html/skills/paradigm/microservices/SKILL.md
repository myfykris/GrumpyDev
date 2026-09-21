---
name: gd-microservices
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review microservice engineering work for service boundaries, data ownership, distributed failure, deployment independence, operational cost, and accidental coupling."
---

# Microservices GrumpyDev review

## Quick checks

- Read service responsibilities, data stores, APIs and events, dependency graph,
  deployment units, ownership, observability, and incident history.

- Trace one business operation across calls, transactions, retries, releases,
  rollback, and support ownership.

Watch especially for a distributed monolith with shared writable data, chatty
synchronous call chains, lockstep releases, generated clients that spread
coupling, unclear incident ownership, and service boundaries justified by
organization charts rather than independent runtime needs.

- Assess shared writable data, an unrecoverable distributed workflow, or a
  boundary with no operational owner under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Microservices
specialist.

## Verdict context

State the evidence for each boundary, data ownership, cross-service failure
behavior, deployment independence, and operational cost.
