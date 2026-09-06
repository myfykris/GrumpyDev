---
name: fastapi
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review FastAPI engineering work for dependency lifetime, async blocking, validation, serialization, OpenAPI contracts, background work, authentication, and deployment risks."
---

# FastAPI GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `python` skill.

## Lean review

- Read application and router construction, dependencies, Pydantic models and
  settings, middleware, lifespan handlers, server configuration, and tests.

- Trace request data, async and sync boundaries, database sessions, streaming,
  background tasks, authentication, errors, and shutdown.

Watch especially for blocking libraries inside async endpoints, lifespan state
initialized differently in tests, dependency caching or scope surprises,
response models exposing fields unintentionally, and background tasks treated as
durable jobs after the response is sent.

Lean mode is insufficient when this material severity condition may apply:

- Treat event-loop blocking, auth dependency bypass, or incompatible validation
  semantics on a public API as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete FastAPI evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State async boundaries, dependency and resource lifetimes, validation and
response contracts, background-work durability, and deployed-server evidence.
