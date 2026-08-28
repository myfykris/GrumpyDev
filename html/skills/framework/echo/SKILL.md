---
name: echo
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Echo framework plans and other engineering artifacts for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks. Project applicability: the project uses or materially depends on Echo."
---

# Echo GrumpyDev review

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

- Establish the exact Go, Echo, server, and deployment versions or modes.

- Read server setup, routes, middleware order, binders and validators, context
  use, limits, dependency clients, shutdown, and integration tests.

Watch especially for middleware-order changes, binders accepting fields that
callers must not control, request contexts retained after the request, blocking
handlers, partial responses followed by error handling, and proxy headers
trusted without an explicit proxy boundary.

Lean mode is insufficient when this material severity condition may apply:

- Treat mass assignment, auth-order bypass, unbounded input, or shutdown data
  loss as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Echo evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State context and request ownership, middleware order, binding controls, timeout
and shutdown behavior, and end-to-end HTTP evidence.
