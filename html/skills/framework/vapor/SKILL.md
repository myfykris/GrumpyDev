---
name: vapor
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Vapor plans and other engineering artifacts for event-loop safety, request lifecycle, async ownership, Fluent transactions, validation, authentication, streaming, and deployment risks. Project applicability: the project uses or materially depends on Vapor."
---

# Vapor GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
