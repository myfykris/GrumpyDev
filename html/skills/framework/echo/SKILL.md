---
name: echo
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Echo framework engineering work for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks."
---

# Echo GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
