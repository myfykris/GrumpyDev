---
name: serverless
description: Review serverless plans for event contracts, concurrency, cold starts, retries, idempotency, time limits, state, networking, permissions, and cost. Use when a plan runs application work on functions or managed event-driven compute.
---

# Serverless plan review

Apply this guidance alongside the core GrumpyDev review, the `message-queues`
skill when a broker is involved, and applicable installed storage and provider
specialists.

## Inspect evidence

- Establish the exact provider, service, runtime version, deployment mode,
  region, and provider limits.
- Read triggers, payloads, runtime settings, concurrency, timeouts, retries,
  destinations, permissions, network paths, dependencies, and cost estimates.
- Trace cold start, duplicate event, partial effect, timeout, throttling,
  dependency slowdown, deployment, and regional failure.

## Establish the operating model

Establish the project target: Provider and runtimes, regions, triggers,
concurrency and timeout limits, network attachment, identity, packaging,
deployment tool, and local-test limits. The changed boundary must define:
Invocation lifecycle, concurrency, cold starts, timeouts, retries, events,
idempotency, state, networking, IAM, packaging, observability, and deployment.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Invocation lifecycle, concurrency, cold starts,
timeouts, retries, events, idempotency. Prove state, networking, IAM, packaging,
observability, deployment through rotation, overload, partial rollout, drain,
forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for platform retries repeating effects, timeouts after an
external commit, reused instances retaining request state, cold starts ignored
in latency budgets, event-size and concurrency ceilings, local emulators hiding
managed behavior, and asynchronous destinations with no reconciliation owner.

- Design handlers for duplicate and out-of-order delivery with idempotency at
  the side-effect boundary.
- Bound concurrency against databases and downstream quotas; automatic scale can
  automate an outage.
- Include cold start, package size, initialization, connection reuse, execution
  duration, and memory in latency evidence.
- Keep durable state outside ephemeral execution and make timeout, cancellation,
  continuation, and poison-event handling explicit.
- Model request, duration, transfer, logging, provisioned capacity, and idle
  alternatives before claiming lower cost.

## Verify the claims

- Verify these behaviors through the effective Serverless configuration and
  runtime topology: Invocation lifecycle, concurrency, cold starts, timeouts,
  retries, events, idempotency. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: state, networking, IAM, packaging,
  observability, deployment. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which provider, service, runtime version, deployment mode, trigger, and
  regional limits apply?
- What delivery, concurrency, timeout, retry, state, networking, permission, and
  cost behavior follows from that platform?

## Calibrate findings

- Treat retry-driven irreversible effects, privilege exposure, hard limit
  failure, or unbounded cost amplification as critical.
- Downgrade when the exact provider semantics are known and load, idempotency,
  limits, and recovery are tested.

## Add to the verdict

State trigger semantics, idempotency, concurrency bounds, latency evidence,
state and failure behavior, permissions, and cost model.
