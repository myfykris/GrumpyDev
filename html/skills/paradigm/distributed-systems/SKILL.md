---
name: distributed-systems
description: Review distributed-system plans for partial failure, consistency, partitions, retries, clocks, coordination, and operability. Use when correctness depends on communication between independently failing processes or services.
---

# Distributed systems plan review

Apply this guidance alongside the core GrumpyDev review and the installed
protocol, message, storage, security, observability, and platform specialists
for the actual boundaries. Use it whenever a correctness decision spans
independently scheduled processes, machines, regions, services, or authorities,
even if the project does not call itself a distributed system.

## Inspect evidence

- Draw or read the concrete service and data boundaries. Identify every remote
  call, message, replication path, cache, coordinator, scheduler, and external
  authority involved in a user-visible operation.
- Trace success, rejection, delay, loss, duplication, reordering, concurrent
  execution, partition, stale reads, failover, restart, and ambiguous completion
  across each boundary. Include what the caller observes after its own timeout.
- Establish the required invariants, consistency model, durability, latency and
  availability objectives, data ownership, geographic scope, and which degraded
  behaviors the product permits.
- Inspect timeout, retry, backoff, idempotency, deduplication, ordering,
  reconciliation, lease, quorum, fencing, and disaster-recovery mechanisms in
  code and configuration. Names such as "exactly once" or "highly available" are
  claims to prove, not designs.
- Read operational evidence: dependency latency distributions, saturation, queue
  age, replica lag, failover tests, incident history, recovery runbooks, and
  fault-injection results.

## Establish the operating model

State which component is authoritative for each piece of data and each business
decision. Define where an operation commits, how that fact becomes observable,
and whether a caller can distinguish committed, rejected, still-running, and
unknown outcomes. If two authorities must agree, identify the coordination or
compensation protocol explicitly.

Define the consistency promised to callers: linearizable, sequential, causal,
read-your-writes, monotonic, bounded-staleness, eventual, or a narrower
domain-specific contract. State the partition and regional failure policy and
which side remains available. Do not use CAP terminology as a substitute for the
actual user-visible behavior.

For every asynchronous operation, define the message identity, ordering scope,
delivery semantics, state transition, retry owner, duplicate handling,
poison-message path, reconciliation owner, and terminal state. Define timeout
budgets from the outer request inward so nested calls do not outlive the work
that requested them.

## Challenge the plan

### Recurring traps

Watch especially for timeout treated as proof of failure, retries repeating
committed effects, clocks used as a total order, split-brain authority, partial
success hidden behind one status, quorum rules that do not match failure
domains, and reconciliation with no deterministic winner.

### Partial failure and uncertain outcomes

- Reject reasoning that treats a remote call like a local function. The server
  may commit after the caller times out, the response may be lost, or a retry
  may race the original request.
- Require an explicit response to ambiguous completion: query by stable
  operation identity, retry an idempotent command, reconcile later, or surface
  an honest unknown state. Blind retry is not a general answer.
- Trace partial success across databases, queues, object stores, caches, and
  external APIs. State which state becomes authoritative and how abandoned or
  duplicate effects are detected and repaired.
- Challenge distributed transactions and sagas equally. A transaction protocol
  needs coordinator and blocking-failure analysis; a saga needs compensation
  semantics, ordering, irreversibility, and human-repair behavior.

### Timeouts, retries, and overload

- Require bounded timeouts at connection, request, stream, lock, lease, and
  overall-operation layers. Defaults can be infinite or misaligned across
  proxies, clients, servers, and queues.
- Assign one retry owner when possible. Multiply attempts across clients,
  gateways, services, SDKs, queues, and operators to expose retry amplification.
- Use exponential backoff, jitter, retry budgets, deadlines, and circuit or
  admission control where they match the failure mode. Retrying overload can
  turn a degraded dependency into a full outage.
- Retry only errors and operations proven safe to retry. Preserve a stable
  idempotency identity across attempts and define its scope, retention,
  concurrency behavior, result replay, and payload-conflict rule.
- Include backpressure and load shedding. Bounded queues, concurrency limits,
  and admission rules must preserve the work and tenants that matter most.

### Consistency, replication, and caches

- Map each read to an authority or replica and state how stale it may be after a
  local write, failover, or partition. User-facing workflows often need a
  stronger session guarantee than background analytics.
- Identify invariant enforcement under concurrent writers. Last-write-wins can
  silently discard valid work; conflict-free or commutative updates apply only
  where the domain operation really has those properties.
- Treat cache invalidation as a consistency design. Define ownership, key and
  version strategy, write ordering, expiration, stampede control, negative
  caching, and recovery after missed invalidation.
- Check replication lag, quorum size, membership changes, failover data loss,
  stale leaders, and read repair. Verify the behavior of the actual storage or
  coordination product rather than assuming all quorums behave alike.

### Ordering, messages, and reconciliation

- Define the smallest ordering scope the invariant needs. Global ordering is
  expensive and often unnecessary, while partition ordering may not survive key
  changes, retries, or producer concurrency.
- Assume at-least-once processing unless stronger end-to-end evidence exists.
  Broker deduplication alone does not make database or external side effects
  exactly once.
- Coordinate state and message publication with an outbox, log, change stream,
  or other proven boundary. Analyze the inverse inbox/deduplication problem at
  consumers.
- Make consumers restartable and idempotent. Define poison-message quarantine,
  schema compatibility, replay limits, and what happens when an old message
  arrives after newer state.
- Require reconciliation for any state that can diverge. Define comparison
  source, scan or event trigger, safe repair, rate limit, observability,
  ownership, and completion evidence.

### Coordination, clocks, and leadership

- Identify every assumption about wall-clock order, time zones, monotonic time,
  clock skew, token expiry, scheduled execution, and timestamp uniqueness. Wall
  clocks can jump and timestamps do not establish causality by themselves.
- For leases and leader election, define quorum, lease duration, renewal,
  pause/skew assumptions, failover time, and fencing. An expired leader can
  continue acting unless the protected resource rejects stale fencing tokens.
- Analyze split brain, network partition, delayed messages, coordinator loss,
  membership change, and rejoining nodes. "Only one leader" needs a mechanism
  and evidence at the point of side effect.
- Challenge distributed locks used to hide poor ownership. Specify lock scope,
  fairness, timeout, failure release, and authority; then verify the invariant
  still holds when a holder pauses or loses connectivity.

### Evolution and operations

- Prove protocol, event, schema, and behavior compatibility while old and new
  versions coexist. Include rollback after some nodes or messages have adopted
  the new representation.
- Define observability by operation identity across traces, structured logs,
  metrics, queues, and durable state without leaking sensitive data. Operators
  need to distinguish slow, failed, duplicated, stuck, and reconciled work.
- Set service objectives and alerts on user-visible outcomes, saturation,
  backlog age, error budgets, replication lag, and reconciliation debt, not
  merely process health.
- Require runbooks and authority for dependency isolation, traffic shifting,
  queue pausing, replay, failover, data repair, and degraded-mode exit.

## Verify the claims

- Use deterministic concurrency tests where possible, then inject latency, loss,
  duplication, reordering, process termination, clock disturbances, dependency
  overload, partitions, and failover in representative environments.
- Test a caller timeout just before and just after server commit. Verify stable
  identity, result discovery, retries, and duplicate effects.
- Exercise every supported degraded mode and the return to normal. Confirm data
  convergence, backlog drain, cache repair, alerts, and operator steps.
- Load test retry and timeout behavior at the system level. Measure aggregate
  attempts and downstream saturation rather than only first-attempt latency.
- Rehearse rolling upgrades and rollback with old/new processes and old/new
  messages in flight. Verify reconciliation after interruption at each boundary.
- Restore regional or authoritative state from the declared recovery source and
  prove dependent services resume consistently.

## Ask when evidence is missing

Ask only what can change the evaluation: the authoritative owner, invariant,
commit point, consistency and staleness contract, partition behavior, delivery
and ordering semantics, retry owner, idempotency scope, reconciliation process,
lease/fencing model, failure budget, degraded mode, mixed-version window, and
recovery authority. For a plan, follow the concrete operation from request to
terminal state and ask at the first unresolved material boundary.

Do not demand a question count. Do not ask the user for facts already available
in `.grump`, code, configuration, diagrams, protocol definitions, operational
evidence, or project documents.

## Calibrate findings

- Treat violations of core invariants, irreversible duplicate side effects,
  split-brain writes, silent data loss, unbounded failure amplification, or a
  partition/failover mode that cannot recover as critical or high according to
  impact and plausibility.
- Treat vague consistency, unowned retries, missing reconciliation, unsafe clock
  assumptions, weak overload control, or incompatible rolling evolution as
  material when linked to a realistic failure.
- Downgrade when the operation is naturally idempotent or commutative, the
  consistency contract permits the behavior, and fault-injection plus recovery
  evidence supports the design.
- Do not penalize a simple single-authority design for lacking machinery it does
  not need. Complexity without a demonstrated requirement is itself risk.

## Add to the verdict

State authorities and failure boundaries, commit and ambiguous-outcome
semantics, consistency guarantees, timeout and retry ownership, idempotency and
ordering scope, coordination assumptions, degraded modes, reconciliation,
mixed-version behavior, recovery evidence, and unanswered material questions.
