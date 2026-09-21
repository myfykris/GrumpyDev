# Redis full-review guidance

## Operating conditions

Establish the project target: Redis product and version, topology, persistence,
eviction, memory limits, key ownership, cluster mode, failover, TLS and
authentication, and workload role. The changed boundary must define: Data
structures, atomicity, Lua or functions, expiration, eviction, persistence,
replication, cluster slots, failover, hot keys, caching, locks, and queues.

## Failure patterns

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

## Verification to run or specify in the plan

- Drive hot keys, large collections, and memory pressure through the selected
  eviction and persistence settings. Check cache stampedes and whether
  required state can disappear or commands block unrelated work.
- Interrupt clients and nodes around writes, script execution, and queue
  acknowledgement. Where clustering applies, check multi-key slot behavior and
  failover; verify persisted recovery or safe reconstruction from the
  authoritative store.
