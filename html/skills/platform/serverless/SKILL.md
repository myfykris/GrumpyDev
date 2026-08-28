---
name: serverless
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review serverless plans and other engineering artifacts for event contracts, concurrency, cold starts, retries, idempotency, time limits, state, networking, permissions, and cost. Project applicability: the project runs application work on functions or managed event-driven compute."
---

# Serverless GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the `message-queues`
skill when a broker is involved, and applicable installed storage and provider
specialists.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Establish the exact provider, service, runtime version, deployment mode,
  region, and provider limits.

- Read triggers, payloads, runtime settings, concurrency, timeouts, retries,
  destinations, permissions, network paths, dependencies, and cost estimates.

Watch especially for platform retries repeating effects, timeouts after an
external commit, reused instances retaining request state, cold starts ignored
in latency budgets, event-size and concurrency ceilings, local emulators hiding
managed behavior, and asynchronous destinations with no reconciliation owner.

Lean mode is insufficient when this material severity condition may apply:

- Treat retry-driven irreversible effects, privilege exposure, hard limit
  failure, or unbounded cost amplification as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Serverless evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State trigger semantics, idempotency, concurrency bounds, latency evidence,
state and failure behavior, permissions, and cost model.
