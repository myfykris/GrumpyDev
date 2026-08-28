# Distributed coordination, clocks, and leadership

Read this reference when the reviewed work directly or indirectly changes locks, leader
election, consensus,
coordination services, logical or wall clocks, time-based correctness, split-brain
prevention, or ownership transfer.

## Coordination, clocks, and leadership

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
