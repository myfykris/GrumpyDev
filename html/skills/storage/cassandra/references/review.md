# Cassandra full-review guidance

## Operating conditions

Establish the project target: Cassandra version, topology and replication,
consistency levels, compaction, repair process, workload shape, partition
limits, drivers, and backup strategy. The changed boundary must define:
Partition and clustering keys, consistency levels, tombstones, compaction,
repair, replication, LWT, batches, hot partitions, schema evolution, and
recovery.

## Failure patterns

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

## Verification to run or specify in the plan

- Load representative hot partitions and TTL or delete traffic; measure
  partition growth, tombstone scans, compaction pressure, and read latency
  under the selected consistency levels.
- Interrupt replicas and repair, then verify reads and writes obey the
  declared availability and consistency policy. Restore backups and rehearse
  node replacement using the supported product and version.
