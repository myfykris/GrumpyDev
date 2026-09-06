---
name: message-queues
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review message-queue engineering work for delivery semantics, ordering, acknowledgement, idempotency, retries, dead letters, backpressure, and recovery."
---

# Message queues GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the
`event-driven-architecture` or `background-jobs` skill.

## Lean review

- Read topic and queue topology, keys, payload schemas, acknowledgements,
  visibility or leases, retries, retention, dead letters, quotas, and
  dashboards.

- Trace publish failure, duplicate and out-of-order delivery, consumer crash,
  poison data, backlog growth, redrive, and broker outage.

Watch especially for acknowledgements before durable effects, visibility or
lease expiry during long work, redelivery treated as exceptional, poison
messages blocking a partition, global ordering assumed from partitioned systems,
reconnect storms, and producers outrunning consumer backpressure.

Lean mode is insufficient when this material severity condition may apply:

- Treat data loss, duplicate irreversible side effects, or an unbounded
  poison-message failure loop as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Message queues evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State delivery and ordering guarantees, acknowledgement and idempotency
boundaries, backlog limits, retry policy, and recovery evidence.
