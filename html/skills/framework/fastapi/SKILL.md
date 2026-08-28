---
name: fastapi
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review FastAPI plans and other engineering artifacts for dependency lifetime, async blocking, validation, serialization, OpenAPI contracts, background work, authentication, and deployment risks. Project applicability: the project uses or materially depends on FastAPI."
---

# FastAPI GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
