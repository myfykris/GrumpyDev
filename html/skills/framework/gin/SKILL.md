---
name: gin
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Gin engineering work for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks."
---

# Gin GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `go` skill.

## Lean review

- Establish the exact Go, Gin, server, and deployment versions or modes.

- Read engine setup, routes and groups, middleware order, binders and
  validators, limits, dependency clients, server settings, and integration
  tests.

Watch especially for binding without explicit validation, mass assignment into
privileged fields, request contexts used from later goroutines, middleware-order
changes, abort and response-write sequencing, and client addresses accepted from
untrusted proxy headers.

Lean mode is insufficient when this material severity condition may apply:

- Treat auth-order bypass, unsafe binding, data races, or unbounded request work
  as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Gin evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State request and context ownership, middleware coverage, binding controls,
proxy trust, shutdown behavior, and HTTP integration evidence.
