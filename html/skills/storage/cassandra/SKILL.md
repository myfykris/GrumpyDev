---
name: cassandra
description: Review Cassandra plans for query-driven modeling, partition sizing, consistency, tombstones, compaction, repair, topology, and recovery. Use when a plan stores or queries distributed data in Cassandra or compatible wide-column databases.
---

# Cassandra plan review

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems` skill.

## Inspect evidence

- Establish the exact product, version, edition, topology, hosting mode, and
  compatibility boundary.
- Read query inventory, primary keys, partition estimates, consistency levels,
  TTLs, compaction, replication, repair, backup, and load tests.
- Trace writes and reads through coordinator loss, replica lag, hinted handoff,
  tombstones, repair, and topology change.

## Establish the operating model

Establish the project target: Cassandra version, topology and replication,
consistency levels, compaction, repair process, workload shape, partition
limits, drivers, and backup strategy. The changed boundary must define:
Partition and clustering keys, consistency levels, tombstones, compaction,
repair, replication, LWT, batches, hot partitions, schema evolution, and
recovery.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Partition and clustering keys, consistency levels,
tombstones, compaction, repair, replication. Prove LWT, batches, hot partitions,
schema evolution, recovery under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the plan

### Recurring traps

Watch especially for hot or unbounded partitions, tombstone accumulation, ALLOW
FILTERING accepted as a design, consistency levels treated as freshness
guarantees, lightweight transactions used as general locking, repair falling
behind gc_grace, and topology changes ignored in capacity plans.

- Require tables designed for known queries; server-side filtering and ad hoc
  joins are not a scaling plan.
- Apply only guarantees documented for the selected product and version;
  compatible wide-column products are not interchangeable by default.
- Bound partition size and hotspot risk across time buckets, high-cardinality
  tenants, and skewed workloads.
- Define read and write consistency as a pair and identify when stale,
  conflicting, or unavailable results are acceptable.
- Check TTL and delete volume, tombstone scans, compaction strategy, disk
  headroom, and repair completion under peak load.
- Prove multi-datacenter replication, node replacement, backup restore, and
  schema rollout with production-like failure drills.

## Verify the claims

- Verify these behaviors through the declared Cassandra topology and workload:
  Partition and clustering keys, consistency levels, tombstones, compaction,
  repair, replication. Use production-shaped scale and workload while observing
  latency, resource use, locks or conflicts, replication, and application
  errors.
- Exercise failure and edge behavior for: LWT, batches, hot partitions, schema
  evolution, recovery. Exercise concurrent writers, retries, duplicate
  operations, failover, interrupted migration, and mixed application versions
  where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which Cassandra-compatible product, exact version, topology, replication, and
  repair model apply?
- Which query paths require which consistency, partition-size, compaction,
  tombstone, and failure behavior?

## Calibrate findings

- Treat an unbounded partition, unrecoverable consistency gap, or topology
  change that risks data loss as critical.
- Downgrade when measured partitions, product-specific semantics, repair, and
  failure tests support the design.

## Add to the verdict

State query coverage, partition bounds, consistency choices, maintenance burden,
topology assumptions, and recovery evidence.
