# Distributed systems full-review guidance

## Operating conditions

State which component is authoritative for each piece of data and each business
decision. Define where an operation commits, how that fact becomes observable,
and whether a caller can distinguish committed, rejected, still-running, and
unknown outcomes. If two authorities must agree, identify the coordination or
compensation protocol explicitly.

## Failure patterns

Watch especially for timeout treated as proof of failure, retries repeating
committed effects, clocks used as a total order, split-brain authority, partial
success hidden behind one status, quorum rules that do not match failure
domains, and reconciliation with no deterministic winner.

## Verification to run or specify in the plan

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
