---
name: event-sourcing-cqrs
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review event sourcing and CQRS plans and other engineering artifacts for immutable history, projection rebuilds, command invariants, event evolution, consistency lag, and operational burden. Project applicability: events are the source of truth or reads and writes use distinct models."
---

# Event sourcing and CQRS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the
`event-driven-architecture`, `schema-evolution`, and applicable installed
storage skills.

## Lean review

- Read command handlers, aggregate reconstruction, event store guarantees,
  snapshots, projections, checkpoints, and rebuild tooling.

- Trace a command through validation, event append, projection lag, failure,
  replay, correction, and data erasure requirements.

Watch especially for rewriting historical events, projections treated as
immediately consistent, replay triggering live side effects, command retries
without idempotency, snapshots treated as a correctness boundary, event schemas
that cannot evolve, and deletion obligations with no workable policy.

Lean mode is insufficient when this material severity condition may apply:

- Treat unrebuildable history, conflicting aggregate writes, or a projection
  used beyond its consistency contract as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Event sourcing and CQRS evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State why the pattern is justified, append guarantees, event evolution,
projection recovery, consistency lag, and operational cost.
