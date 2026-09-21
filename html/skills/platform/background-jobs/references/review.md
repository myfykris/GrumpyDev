# Background jobs full-review guidance

## Operating conditions

Establish the project target: Queue implementation, delivery semantics, worker
topology, retry and timeout policy, concurrency limits, scheduler, dead-letter
handling, and retention. The changed boundary must define: Enqueue and commit
boundaries, delivery guarantees, idempotency, retries, timeouts, scheduling,
uniqueness, concurrency, poison jobs, draining, and replay.

## Failure patterns

- Require durable enqueue for work that must survive process loss; in-memory
  tasks do not qualify.
- Design every handler for at-least-once delivery unless the transport and
  effect boundary prove otherwise.
- Bound retries by error class, attempt count, age, backoff, and downstream
  budget; poison work must become visible.
- Check lease expiry, overlapping schedules, clock skew, long-running jobs,
  fairness, priority, and per-tenant concurrency.
- Provide cancellation, replay, manual repair, progress, and deployment drain
  procedures that operators can actually use.

## Verification to run or specify in the plan

- Exercise failure before and after the enqueue commit and before, during and
  after each external effect. Verify retry or duplicate delivery cannot repeat
  an unsafe effect or lose required work.
- Expire leases, overlap schedules, terminate workers, slow dependencies, grow a
  backlog, inject poison jobs and replay dead letters under production-shaped
  concurrency and tenant mix.
- Run old and new workers together, then drain and roll back while long-running
  jobs are active. Verify payload compatibility, cancellation, visibility and
  operator repair.
