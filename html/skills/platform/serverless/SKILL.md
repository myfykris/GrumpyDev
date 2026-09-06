---
name: serverless
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review serverless engineering work for event contracts, concurrency, cold starts, retries, idempotency, time limits, state, networking, permissions, and cost."
---

# Serverless GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the `message-queues`
skill when a broker is involved, and applicable installed storage and provider
specialists.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
