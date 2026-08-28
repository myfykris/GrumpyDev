---
name: actix-web
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Actix Web plans and other engineering artifacts for worker state, extractor behavior, async blocking, middleware order, cancellation, error responses, and graceful shutdown risks. Project applicability: the project uses or materially depends on Actix Web."
---

# Actix Web GrumpyDev review

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

- Establish the exact Actix Web, Rust, Tokio, and target-platform versions.

- Read application construction, worker configuration, shared state types,
  extractors, middleware, route registration, server settings, and integration
  tests.

Watch especially for synchronous work blocking Actix workers, extractors that
turn domain errors into accidental responses, shared-state locks held across
await points, middleware ordering changes, and shutdown paths that abandon
in-flight work.

Lean mode is insufficient when this material severity condition may apply:

- Treat blocking or unbounded work on workers, unsafe shared state, or shutdown
  data loss as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Actix Web evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State worker and state ownership, blocking boundaries, middleware and extractor
controls, shutdown behavior, and end-to-end server evidence.
