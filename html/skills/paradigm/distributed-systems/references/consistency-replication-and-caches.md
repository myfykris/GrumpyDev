# Distributed consistency, replication, and caches

Read this reference when the reviewed work directly or indirectly changes replicated
state, read or write consistency,
quorum behavior, lag, failover, cache ownership, invalidation, leases, fencing, or stale
data tolerance.

## Consistency, replication, and caches

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
