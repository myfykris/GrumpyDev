# Distributed systems standard review

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

## Challenge the reviewed work

### Recurring traps

Watch especially for timeout treated as proof of failure, retries repeating
committed effects, clocks used as a total order, split-brain authority, partial
success hidden behind one status, quorum rules that do not match failure
domains, and reconciliation with no deterministic winner.

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
