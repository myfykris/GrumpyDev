---
name: background-jobs
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review background-job plans and other engineering artifacts for durability, scheduling, idempotency, retries, concurrency, leases, cancellation, and operator recovery. Project applicability: work continues outside the request or initiating process."
---

# Background jobs GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
