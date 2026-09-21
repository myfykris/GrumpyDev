---
name: gd-fastapi
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review FastAPI engineering work for dependency lifetime, async blocking, validation, serialization, OpenAPI contracts, background work, authentication, and deployment risks."
---

# FastAPI GrumpyDev review

## Quick checks

- Read application and router construction, dependencies, Pydantic models and
  settings, middleware, lifespan handlers, server configuration, and tests.

- Trace request data, async and sync boundaries, database sessions, streaming,
  background tasks, authentication, errors, and shutdown.

Watch especially for blocking libraries inside async endpoints, lifespan state
initialized differently in tests, dependency caching or scope surprises,
response models exposing fields unintentionally, and background tasks treated as
durable jobs after the response is sent.

- Assess event-loop blocking, auth dependency bypass, or incompatible validation
  semantics on a public API under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the FastAPI specialist.

## Verdict context

State async boundaries, dependency and resource lifetimes, validation and
response contracts, background-work durability, and deployed-server evidence.
