# Background jobs survey contribution

## Applicability

Apply this contribution when work continues outside the request or initiating
process. Skip it when Background jobs does not constrain a supported build,
runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Background jobs, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Queue implementation, delivery semantics, worker
  topology, retry and timeout policy, concurrency limits, scheduler, dead-letter
  handling, and retention.
- Review doctrine for: Enqueue and commit boundaries, delivery guarantees,
  idempotency, retries, timeouts, scheduling, uniqueness, concurrency, poison
  jobs, draining, and replay.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Queue backend, worker topology, concurrency,
  acknowledgement and visibility, retry, dead letters, scheduler, shutdown,
  scaling, and deployment ordering.

## Ask only when materially unresolved

- What durable record owns each job, and what makes retry or duplicate execution
  safe?
- How are cancellation, lease expiry, poison work, and operator recovery
  handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Queue backend, worker topology,
  concurrency, acknowledgement and visibility, retry, dead letters, scheduler,
  shutdown, scaling, and deployment ordering? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Background jobs answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Background jobs deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Background jobs doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Background jobs when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
