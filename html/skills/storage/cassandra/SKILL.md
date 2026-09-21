---
name: gd-cassandra
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Cassandra engineering work for query-driven modeling, partition sizing, consistency, tombstones, compaction, repair, topology, and recovery."
---

# Cassandra GrumpyDev review

## Quick checks

- Establish the exact product, version, edition, topology, hosting mode, and
  compatibility boundary.

- Read query inventory, primary keys, partition estimates, consistency levels,
  TTLs, compaction, replication, repair, backup, and load tests.

Watch especially for hot or unbounded partitions, tombstone accumulation, ALLOW
FILTERING accepted as a design, consistency levels treated as freshness
guarantees, lightweight transactions used as general locking, repair falling
behind gc_grace, and topology changes ignored in capacity plans.

- Assess an unbounded partition, unrecoverable consistency gap, or topology
  change that risks data loss under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Cassandra
specialist.

## Verdict context

State query coverage, partition bounds, consistency choices, maintenance burden,
topology assumptions, and recovery evidence.
