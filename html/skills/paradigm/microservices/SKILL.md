---
name: microservices
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review microservice plans and other engineering artifacts for service boundaries, data ownership, distributed failure, deployment independence, operational cost, and accidental coupling. Project applicability: a system is split into independently deployed network services."
---

# Microservices GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems` skill.

## Lean review

- Read service responsibilities, data stores, APIs and events, dependency graph,
  deployment units, ownership, observability, and incident history.

- Trace one business operation across calls, transactions, retries, releases,
  rollback, and support ownership.

Watch especially for a distributed monolith with shared writable data, chatty
synchronous call chains, lockstep releases, generated clients that spread
coupling, unclear incident ownership, and service boundaries justified by
organization charts rather than independent runtime needs.

Lean mode is insufficient when this material severity condition may apply:

- Treat shared writable data, an unrecoverable distributed workflow, or a
  boundary with no operational owner as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Microservices evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the evidence for each boundary, data ownership, cross-service failure
behavior, deployment independence, and operational cost.
