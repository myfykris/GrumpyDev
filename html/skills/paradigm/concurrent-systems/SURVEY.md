# Concurrent systems survey contribution

## Applicability

Apply this contribution when work runs in parallel across threads, processes, tasks,
actors, or workers. Skip it when Concurrent systems do not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Concurrent systems, inspect architecture records, module or service maps,
dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Concurrency model, thread or process limits,
  synchronization primitives, scheduler assumptions, latency targets,
  race-detection tools, and failure policy.
- Review doctrine for: Memory ordering, races, deadlocks, starvation,
  cancellation, ownership, synchronization, work queues, backpressure,
  scheduling, and deterministic evidence.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Process, thread, actor, coroutine, or device model;
  scheduler; core count; shared memory; clock; cancellation; resource limits;
  and failure isolation.

## Ask only when materially unresolved

- Which task owns each mutable resource, and which synchronization or message
  boundary orders access?
- What progress, cancellation, fairness, timeout, and failure behavior applies
  under contention?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Process, thread, actor, coroutine, or
  device model; scheduler; core count; shared memory; clock; cancellation;
  resource limits; and failure isolation? Ask only when evidence and the core
  profile confirmation do not resolve them.

## Record in .grump

Record Concurrent systems answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Concurrent systems deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Concurrent systems
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Concurrent systems when business invariants, ownership boundaries,
data authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
