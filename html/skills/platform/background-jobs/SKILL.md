---
name: background-jobs
description: Review background-job plans for durability, scheduling, idempotency, retries, concurrency, leases, cancellation, and operator recovery. Use when work continues outside the request or initiating process.
---

# Background jobs plan review

Apply this guidance alongside the core GrumpyDev review and the relevant queue,
framework, and storage skills.

## Inspect evidence

- Read enqueue boundaries, payloads, worker configuration, leases, retries,
  schedules, idempotency records, dead-letter handling, and dashboards.
- Trace enqueue failure, duplicate delivery, timeout, worker death, partial side
  effects, redrive, cancellation, and deployment shutdown.

## Establish the operating model

Establish the project target: Queue implementation, delivery semantics, worker
topology, retry and timeout policy, concurrency limits, scheduler, dead-letter
handling, and retention. The changed boundary must define: Enqueue and commit
boundaries, delivery guarantees, idempotency, retries, timeouts, scheduling,
uniqueness, concurrency, poison jobs, draining, and replay.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Enqueue and commit boundaries, delivery guarantees,
idempotency, retries, timeouts, scheduling. Prove uniqueness, concurrency,
poison jobs, draining, replay through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for jobs published before a transaction commits, retries
repeating side effects, visibility timeouts shorter than work, poison jobs
cycling forever, ordering assumed across workers, cancellation ignored during
shutdown, and success acknowledged before durable completion.

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

- Verify these behaviors through the effective Background jobs configuration and
  runtime topology: Enqueue and commit boundaries, delivery guarantees,
  idempotency, retries, timeouts, scheduling. Use effective rendered
  configuration and deployable artifacts in a representative identity, topology,
  capacity, and policy boundary.
- Exercise failure and edge behavior for: uniqueness, concurrency, poison jobs,
  draining, replay. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- What durable record owns each job, and what makes retry or duplicate execution
  safe?
- How are cancellation, lease expiry, poison work, and operator recovery
  handled?

## Calibrate findings

- Treat possible duplicate side effects, silent job loss, or an unrecoverable
  queue backlog as critical.
- Downgrade when work is disposable by requirement or durable state,
  idempotency, and recovery are proven.

## Add to the verdict

State durability, delivery semantics, idempotency boundary, retry and lease
rules, concurrency limits, and recovery tooling.
