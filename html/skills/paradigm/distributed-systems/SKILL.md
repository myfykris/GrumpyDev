---
name: distributed-systems
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review distributed-system engineering work for partial failure, consistency, partitions, retries, clocks, coordination, and operability."
---

# Distributed systems GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

This specialist remains relevant whenever correctness spans independently
failing processes, machines, regions, services, or authorities, even when the
project does not call itself distributed. Coordinate findings with the active
protocol, message, storage, security, observability, and platform specialists.

## Lean review

- Identify the authority and commit point for each user-visible decision and
  what a caller observes after success, rejection, delay, timeout, or partition.
- Trace loss, duplication, reordering, concurrent execution, stale reads,
  failover, restart, and ambiguous completion across every remote boundary.
- Challenge timeout treated as failure, retries repeating committed effects,
  clocks used as total order, split-brain authority, hidden partial success,
  mismatched quorum and failure domains, and reconciliation without a
  deterministic winner.
- Require stable operation identity, one clear retry owner, bounded timeout and
  retry budgets, idempotency scope, backpressure, poison handling, repair
  ownership, and honest unknown states.
- State the promised consistency, durability, ordering, availability, and
  degraded user behavior rather than relying on labels such as exactly once.

Lean mode is insufficient for new coordination, replication, cross-region
behavior, failover, consensus, sagas, distributed transactions, or a changed
consistency contract.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/partial-failure-retries-and-overload.md):
  Read when the reviewed work directly or indirectly changes remote calls, timeouts,
  retries, hedging, backoff, circuit
  breaking, overload behavior, admission control, cancellation, uncertain outcomes, or
  dependency failure.
- [Focused rules](references/consistency-replication-and-caches.md):
  Read when the reviewed work directly or indirectly changes replicated state, read or
  write consistency, quorum
  behavior, lag, failover, cache ownership, invalidation, leases, fencing, or stale data
  tolerance.
- [Focused rules](references/messaging-ordering-and-reconciliation.md):
  Read when the reviewed work directly or indirectly changes events, queues, delivery
  guarantees, ordering,
  deduplication, idempotency, outboxes, sagas, compensation, reconciliation, replay, or
  poison work.
- [Focused rules](references/coordination-clocks-and-leadership.md):
  Read when the reviewed work directly or indirectly changes locks, leader election,
  consensus, coordination services,
  logical or wall clocks, time-based correctness, split-brain prevention, or ownership
  transfer.
- [Focused rules](references/evolution-operations-and-recovery.md):
  Read when the reviewed work directly or indirectly changes protocols, schemas, rolling
  versions, topology, region or
  zone placement, data migration, observability, incident response, rollback, disaster
  recovery, or restoration.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

Name the affected authorities, uncertain outcomes, failure domains, consistency
promise, repair owner, and evidence supporting recovery claims.
