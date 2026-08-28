# DynamoDB standard review

## Inspect additional evidence

- Trace every query and write through key selection, retries, throttling,
  consistency, duplication, growth, and region failure.

## Establish the operating model

Establish the project target: Regions and table topology, capacity mode,
consistency needs, key conventions, indexes, global tables, TTL, streams,
backup, and workload limits. The changed boundary must define: Keys and access
patterns, indexes, capacity, partitions, consistency, transactions, condition
expressions, streams, TTL, global tables, retries, and hot keys.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Keys and access patterns, indexes, capacity, partitions,
consistency, transactions. Prove condition expressions, streams, TTL, global
tables, retries, hot keys under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

- Require each access pattern to map to a key or index; scans are not a fallback
  architecture.
- Test partition-key cardinality and traffic distribution, including celebrity
  keys, monotonic writes, and burst behavior.
- Define conditional writes, idempotency, transaction scope, eventual
  consistency, and global-table conflict behavior.
- Account for item-size limits, index projection and write amplification,
  pagination, TTL delay, and stream redelivery.
- Model on-demand or provisioned capacity cost, throttling backoff, backup,
  point-in-time recovery, and restore validation.

## Verify the claims

- Verify these behaviors through the declared DynamoDB topology and workload:
  Keys and access patterns, indexes, capacity, partitions, consistency,
  transactions. Use production-shaped scale and workload while observing
  latency, resource use, locks or conflicts, replication, and application
  errors.
- Exercise failure and edge behavior for: condition expressions, streams, TTL,
  global tables, retries, hot keys. Exercise concurrent writers, retries,
  duplicate operations, failover, interrupted migration, and mixed application
  versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which access patterns, key distributions, consistency needs, table mode,
  regions, and transaction boundaries apply?
- How are conditional writes, hot keys, retries, streams, indexes, and item
  growth bounded?

## Calibrate findings

- Downgrade when access patterns and distributions are measured and conditional
  operations plus recovery cover concurrency.
