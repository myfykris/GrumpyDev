---
name: axum
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Axum engineering work for router state, extractor limits, Tower middleware, async blocking, error responses, cancellation, and graceful shutdown risks."
---

# Axum GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
