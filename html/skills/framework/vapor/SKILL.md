---
name: vapor
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Vapor engineering work for event-loop safety, request lifecycle, async ownership, Fluent transactions, validation, authentication, streaming, and deployment risks."
---

# Vapor GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `swift` skill.

## Lean review

- Read Vapor, Swift, and dependency versions, application configuration, routes,
  middleware, content models, Fluent schemas and migrations, clients, and tests.

- Trace requests, event loops, async tasks, database access, authentication,
  errors, streaming, jobs, and shutdown.

Watch especially for blocking work on event loops, incorrect bridging between
futures and async code, request-owned objects escaping their lifetime, Fluent
query or migration assumptions, streams without backpressure, and shutdown that
drops scheduled or in-flight work.

Lean mode is insufficient when this material severity condition may apply:

- Treat event-loop blocking, unsafe cross-request state, or lost critical work
  during shutdown as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Vapor evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State event-loop and task ownership, validation and authorization boundaries,
persistence safety, server lifecycle, and production evidence.
