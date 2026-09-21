# DynamoDB full-review guidance

## Operating conditions

Establish the project target: Regions and table topology, capacity mode,
consistency needs, key conventions, indexes, global tables, TTL, streams,
backup, and workload limits. The changed boundary must define: Keys and access
patterns, indexes, capacity, partitions, consistency, transactions, condition
expressions, streams, TTL, global tables, retries, and hot keys.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise conditional writes and transaction retries with concurrent callers
  and ambiguous timeouts. Check index-read freshness, paginated results, and
  duplicate stream delivery against the application's contract.
- Load skewed partition keys and throttled requests using the selected
  capacity mode. Where used, test delayed TTL removal and global-table
  conflicts; restore a backup and verify application access to the recovered
  table.
