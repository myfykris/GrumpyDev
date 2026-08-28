# Redis standard review

## Inspect additional evidence

- Trace cache miss, concurrent fill, expiration, eviction, restart, failover,
  resharding, and dependency loss.

## Establish the operating model

Establish the project target: Redis product and version, topology, persistence,
eviction, memory limits, key ownership, cluster mode, failover, TLS and
authentication, and workload role. The changed boundary must define: Data
structures, atomicity, Lua or functions, expiration, eviction, persistence,
replication, cluster slots, failover, hot keys, caching, locks, and queues.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Data structures, atomicity, Lua or functions, expiration,
eviction, persistence, replication. Prove cluster slots, failover, hot keys,
caching, locks, queues under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

- State whether Redis is a disposable cache or a system of record; durability
  and recovery requirements differ completely.
- Check key cardinality, hot keys, unbounded collections, large values, blocking
  commands, and memory fragmentation under peak load.
- Require a cache-consistency policy for invalidation, stale reads, stampedes,
  negative caching, and source failure.
- Keep multi-key atomicity within actual cluster slot and transaction
  guarantees; verify Lua or functions for blocking and retry behavior.
- Define eviction, persistence, replica lag, failover data loss, cluster
  partition, and cold-start recovery explicitly.

## Verify the claims

- Verify these behaviors through the declared Redis topology and workload: Data
  structures, atomicity, Lua or functions, expiration, eviction, persistence,
  replication. Use production-shaped scale and workload while observing latency,
  resource use, locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: cluster slots, failover, hot keys,
  caching, locks, queues. Exercise concurrent writers, retries, duplicate
  operations, failover, interrupted migration, and mixed application versions
  where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which Redis-compatible product, exact version, deployment mode, persistence,
  eviction, and failover behavior apply?
- Is the data disposable cache, coordination state, queue state, session state,
  or primary data, and how is loss recovered?

## Calibrate findings

- Downgrade when data is safely reconstructible or product-specific atomicity,
  persistence, failover, and load evidence are complete.
