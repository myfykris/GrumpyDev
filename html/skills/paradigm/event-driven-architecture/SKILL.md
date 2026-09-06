---
name: event-driven-architecture
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review event-driven architecture engineering work for event contracts, delivery semantics, ordering, idempotency, replay, coupling, and operational recovery."
---

# Event-driven architecture GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `message-queues`
and `schema-evolution` skills.

## Lean review

- Read event schemas, producers, consumers, brokers, delivery settings, retry
  and dead-letter policy, replay tooling, and ownership.

- Trace creation, publication, duplication, reordering, consumption, failure,
  redrive, and retirement of each event type.

Watch especially for exactly-once claims built on at-least-once components,
database and event dual writes, out-of-order or duplicate delivery, poison
events, consumers with non-idempotent side effects, schema changes that strand
old consumers, and replay that recontacts external systems.

Lean mode is insufficient when this material severity condition may apply:

- Treat ambiguous command ownership, lost committed events, or duplicate
  irreversible effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Event-driven architecture evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State event ownership, delivery and ordering guarantees, publication atomicity,
replay policy, and recovery evidence.
