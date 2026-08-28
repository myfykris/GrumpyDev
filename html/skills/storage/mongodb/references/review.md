# MongoDB standard review

## Establish the operating model

Establish the project target: MongoDB version, replica or shard topology, read
and write concerns, drivers, schema and index ownership, transaction use,
backup, and data-volume profile. The changed boundary must define: Document
boundaries, schema validation, indexes, transactions, read and write concerns,
replication, sharding, change streams, migrations, and backup.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Document boundaries, schema validation, indexes,
transactions, read and write concerns. Prove replication, sharding, change
streams, migrations, backup under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared MongoDB topology and workload:
  Document boundaries, schema validation, indexes, transactions, read and write
  concerns. Use production-shaped scale and workload while observing latency,
  resource use, locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: replication, sharding, change streams,
  migrations, backup. Exercise concurrent writers, retries, duplicate
  operations, failover, interrupted migration, and mixed application versions
  where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which MongoDB version, topology, storage mode, read concern, write concern,
  and transaction use apply?
- How are schema variation, indexes, retries, migrations, replication lag, and
  restore handled?

## Calibrate findings

- Downgrade when document ownership is bounded and concerns, atomic operations,
  validation, and restore tests match the topology.
