---
name: gin
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Gin plans and other engineering artifacts for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks. Project applicability: the project uses or materially depends on Gin."
---

# Gin GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
