# MongoDB full-review guidance

## Operating conditions

Establish the project target: MongoDB version, replica or shard topology, read
and write concerns, drivers, schema and index ownership, transaction use,
backup, and data-volume profile. The changed boundary must define: Document
boundaries, schema validation, indexes, transactions, read and write concerns,
replication, sharding, change streams, migrations, and backup.

## Failure patterns

- Require embedding or referencing decisions to follow access and consistency
  boundaries, not fear of joins.
- Enforce schema shape and evolution deliberately; schemaless does not mean
  contractless.
- Check compound index order, multikey limits, covered queries, sort memory,
  aggregation spill, and index write cost with `explain` evidence.
- Define read preference, read concern, write concern, retryable writes,
  transaction scope, and stale-read tolerance.
- Prove shard-key distribution, resharding path, replica failover, backup
  consistency, and restore behavior before scale depends on them.

## Verification to run or specify in the plan

- Run actual query and aggregation shapes with representative document sizes
  and array growth. Inspect explain output, sort or spill behavior, validator
  failures, and index write cost.
- Exercise concurrent updates and transaction retries through failover with
  the selected read and write concerns. Where sharding or change streams
  apply, test their recovery paths; restore a backup and verify indexes,
  validators, and application startup.
