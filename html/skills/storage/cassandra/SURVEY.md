# Cassandra survey contribution

## Applicability

Apply this contribution when the project stores or queries distributed data in Cassandra
or a compatible wide-column database.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Cassandra, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Cassandra version, topology and replication,
  consistency levels, compaction, repair process, workload shape, partition
  limits, drivers, and backup strategy.
- Review doctrine for: Partition and clustering keys, consistency levels,
  tombstones, compaction, repair, replication, LWT, batches, hot partitions,
  schema evolution, and recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product and version, nodes, data centers,
  replication, consistency, partitioning, repair, compaction, storage,
  capacity, backup, restore, failover, and ownership.

## Ask only when materially unresolved

- Which Cassandra-compatible product, exact version, topology, replication, and
  repair model apply?
- Which query paths require which consistency, partition-size, compaction,
  tombstone, and failure behavior?
- Align existing domain questions with this deployment guidance when it is
  material: Product and version, nodes, data centers, replication, consistency,
  partitioning, repair, compaction, storage, capacity, backup, restore,
  failover, and ownership. Do not repeat the core profile confirmation.

## Record in .grump

Record Cassandra answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing Cassandra survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep one-off query traces, current node identities, transient compaction,
repair, tombstone and latency readings, temporary rebuild operations, and copied
partition data out of durable Cassandra doctrine. Do not duplicate facts owned
by another applicable contribution.

## Re-survey triggers

Re-survey Cassandra when its distribution or version, data-center topology,
replication factor or strategy, consistency levels, table or partition-key
design, compaction, repair, tombstone policy, security boundary, backup, restore,
or disaster-recovery objective materially changes. Also re-survey when evidence
conflicts with saved doctrine or the user requests a context refresh.
