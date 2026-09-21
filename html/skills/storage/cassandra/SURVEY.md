# Cassandra survey contribution

## Applies when

Apply this contribution when the project stores or queries distributed data in Cassandra
or a compatible wide-column database.

## Inspect

- Establish the exact product, version, edition, topology, hosting mode, and
  compatibility boundary.

## Ask when unresolved

- Which Cassandra-compatible product, exact version, topology, replication, and
  repair model apply?

- Which query paths require which consistency, partition-size, compaction,
  tombstone, and failure behavior?

- Which runtime or deployment differences are material for future reviews:
  Product and version, nodes, data centers, replication, consistency,
  partitioning, repair, compaction, storage, capacity, backup, restore,
  failover, and ownership?

## Record

Map Cassandra data guarantees to `Requirements`, accepted tradeoffs to
`Accepted decisions`, topology and recovery facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
