---
name: express
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Express engineering work for middleware order, async error propagation, request validation, authorization, resource limits, proxy behavior, and shutdown risks."
---

# Express GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `javascript` or
`typescript` skill.

## Lean review

- Read application setup, Express and Node versions, routers, middleware order,
  validation, authentication, proxy settings, server timeouts, and integration
  tests.

- Trace request data, async handlers, errors, streams, uploads, downstream
  calls, background work, and shutdown.

Watch especially for middleware that falls through or sends twice, rejected
promises or callback failures that are not forwarded under the selected Express
version and wrapper conventions, global request state, body and proxy defaults
treated as security controls, and CPU or synchronous I/O blocking the event
loop.

Lean mode is insufficient when this material severity condition may apply:

- Treat auth bypass, spoofed client identity, unhandled async failure, or
  unbounded request input as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Express evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State middleware and validation boundaries, async error behavior, resource
limits, proxy assumptions, shutdown behavior, and HTTP integration evidence.
