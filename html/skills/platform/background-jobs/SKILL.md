---
name: background-jobs
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review background-job engineering work for durability, scheduling, idempotency, retries, concurrency, leases, cancellation, and operator recovery."
---

# Background jobs GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the relevant queue,
framework, and storage skills.

## Lean review

- Read enqueue boundaries, payloads, worker configuration, leases, retries,
  schedules, idempotency records, dead-letter handling, and dashboards.

- Trace enqueue failure, duplicate delivery, timeout, worker death, partial side
  effects, redrive, cancellation, and deployment shutdown.

Watch especially for jobs published before a transaction commits, retries
repeating side effects, visibility timeouts shorter than work, poison jobs
cycling forever, ordering assumed across workers, cancellation ignored during
shutdown, and success acknowledged before durable completion.

Lean mode is insufficient when this material severity condition may apply:

- Treat possible duplicate side effects, silent job loss, or an unrecoverable
  queue backlog as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Background jobs evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State durability, delivery semantics, idempotency boundary, retry and lease
rules, concurrency limits, and recovery tooling.
