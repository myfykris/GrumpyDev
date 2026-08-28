---
name: sinatra
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Sinatra plans and other engineering artifacts for route and middleware order, application state, request validation, concurrency, sessions, errors, and deployment risks. Project applicability: the project uses or materially depends on Sinatra."
---

# Sinatra GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `ruby` skill.

## Lean review

- Establish the exact Ruby, Sinatra, Rack, server, and deployment versions or
  modes.

- Read application style, Rack and middleware setup, routes, helpers, settings,
  session configuration, server model, dependency clients, and tests.

Watch especially for route and filter ordering, shared mutable state under
threaded servers, middleware-dependent session or proxy behavior, blocking
request handlers, error handlers that write after a response starts, and
development-server behavior assumed in production.

Lean mode is insufficient when this material severity condition may apply:

- Treat mutable cross-request state, auth-order bypass, or unsafe multi-threaded
  behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Sinatra evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State application and state model, middleware and route behavior, request trust
boundaries, concurrency assumptions, and production-server evidence.
