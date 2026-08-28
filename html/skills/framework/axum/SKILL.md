---
name: axum
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Axum plans and other engineering artifacts for router state, extractor limits, Tower middleware, async blocking, error responses, cancellation, and graceful shutdown risks. Project applicability: the project uses or materially depends on Axum."
---

# Axum GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `rust` skill.

## Lean review

- Establish the exact Axum, Rust, Tokio, Tower, and target-platform versions.

- Read router composition, state types, extractors, Tower layers, body limits,
  server configuration, dependency clients, and integration tests.

Watch especially for inconsistent extractor rejections, blocking work inside
async handlers, shared-state guards held across await points, body consumption
by middleware, and graceful shutdown that stops accepting work without draining
it.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsafe shared state, unbounded request work, or lost critical work
  during shutdown as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Axum evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State router-state ownership, layer ordering, resource bounds, cancellation and
shutdown behavior, and server-level evidence.
