---
name: ktor
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Ktor plans and other engineering artifacts for plugin order, coroutine ownership, request validation, serialization, authentication, client and server lifecycle, and deployment risks. Project applicability: the project uses or materially depends on Ktor."
---

# Ktor GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `kotlin` skill.

## Lean review

- Read application modules, installed plugins and order, routing, content
  negotiation, authentication, coroutine dispatchers, client configuration, and
  tests.

- Trace calls, cancellation, blocking work, resources, serialization, errors,
  streaming, background tasks, and shutdown.

Watch especially for plugin installation order, coroutine scopes that outlive
requests or the application, blocking I/O on constrained dispatchers,
content-negotiation mismatches, route-scoped authentication gaps, and shutdown
that cancels work without reconciliation.

Lean mode is insufficient when this material severity condition may apply:

- Treat auth plugin bypass, blocked event loops, or lost structured cancellation
  on a critical path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Ktor evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State plugin ordering, coroutine and resource ownership, serialization contract,
resource limits, engine assumptions, and deployment evidence.
