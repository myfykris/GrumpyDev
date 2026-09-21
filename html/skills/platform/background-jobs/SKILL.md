---
name: gd-background-jobs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review background-job engineering work for durability, scheduling, idempotency, retries, concurrency, leases, cancellation, and operator recovery."
---

# Background jobs GrumpyDev review

## Quick checks

- Read enqueue boundaries, payloads, worker configuration, leases, retries,
  schedules, idempotency records, dead-letter handling, and dashboards.

- Trace enqueue failure, duplicate delivery, timeout, worker death, partial side
  effects, redrive, cancellation, and deployment shutdown.

Watch especially for jobs published before a transaction commits, retries
repeating side effects, visibility timeouts shorter than work, poison jobs
cycling forever, ordering assumed across workers, cancellation ignored during
shutdown, and success acknowledged before durable completion.

- Assess possible duplicate side effects, silent job loss, or an unrecoverable
  queue backlog under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Background jobs
specialist.

## Verdict context

State durability, delivery semantics, idempotency boundary, retry and lease
rules, concurrency limits, and recovery tooling.
