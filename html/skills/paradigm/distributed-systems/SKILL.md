---
name: gd-distributed-systems
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review distributed-system engineering work for partial failure, consistency, partitions, retries, clocks, coordination, and operability."
---

# Distributed systems GrumpyDev review

## Review focus

This specialist remains relevant whenever correctness spans independently failing processes, machines, regions, services, or authorities, even when the project does not call itself distributed.

## Quick checks

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

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Distributed systems
specialist.

- [Focused rules](references/partial-failure-retries-and-overload.md):
  Read when the work changes remote calls, timeouts,
  retries, hedging, backoff, circuit
  breaking, overload behavior, admission control, cancellation, uncertain outcomes, or
  dependency failure.
- [Focused rules](references/consistency-replication-and-caches.md):
  Read when the work changes replicated state, read or
  write consistency, quorum
  behavior, lag, failover, cache ownership, invalidation, leases, fencing, or stale data
  tolerance.
- [Focused rules](references/messaging-ordering-and-reconciliation.md):
  Read when the work changes events, queues, delivery
  guarantees, ordering,
  deduplication, idempotency, outboxes, sagas, compensation, reconciliation, replay, or
  poison work.
- [Focused rules](references/coordination-clocks-and-leadership.md):
  Read when the work changes locks, leader election,
  consensus, coordination services,
  logical or wall clocks, time-based correctness, split-brain prevention, or ownership
  transfer.
- [Focused rules](references/evolution-operations-and-recovery.md):
  Read when the work changes protocols, schemas, rolling
  versions, topology, region or
  zone placement, data migration, observability, incident response, rollback, disaster
  recovery, or restoration.

## Verdict context

Name the affected authorities, uncertain outcomes, failure domains, consistency
promise, repair owner, and evidence supporting recovery claims.
