---
name: message-queues
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review message-queue plans and other engineering artifacts for delivery semantics, ordering, acknowledgement, idempotency, retries, dead letters, backpressure, and recovery. Project applicability: work or data crosses a broker, queue, stream, or pub-sub system."
---

# Message queues GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
