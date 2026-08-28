# Background jobs standard review

## Establish the operating model

Establish the project target: Queue implementation, delivery semantics, worker
topology, retry and timeout policy, concurrency limits, scheduler, dead-letter
handling, and retention. The changed boundary must define: Enqueue and commit
boundaries, delivery guarantees, idempotency, retries, timeouts, scheduling,
uniqueness, concurrency, poison jobs, draining, and replay.

Identify who owns the durable enqueue record, broker state, worker effect,
scheduler, retry policy, concurrency budget, poison queue, cancellation, replay,
and operator repair. Trace the transaction gap between business state and
enqueue, then prove duplicate delivery, lease expiry, worker termination,
backlog growth, and mixed worker versions preserve the required effects.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Exercise failure before and after the enqueue commit and before, during and
  after each external effect. Verify retry or duplicate delivery cannot repeat
  an unsafe effect or lose required work.
- Expire leases, overlap schedules, terminate workers, slow dependencies, grow a
  backlog, inject poison jobs and replay dead letters under production-shaped
  concurrency and tenant mix.
- Run old and new workers together, then drain and roll back while long-running
  jobs are active. Verify payload compatibility, cancellation, visibility and
  operator repair.

## Ask when evidence is missing

- What durable record owns each job, and what makes retry or duplicate execution
  safe?
- How are cancellation, lease expiry, poison work, and operator recovery
  handled?

## Calibrate findings

- Downgrade when work is disposable by requirement or durable state,
  idempotency, and recovery are proven.
