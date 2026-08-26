# Cassandra survey contribution

## Applicability

Apply this contribution when a plan stores or queries distributed data in
Cassandra or compatible wide-column databases. Skip it when Cassandra does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

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

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable Cassandra
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Cassandra when product version or provider, topology, engine,
consistency policy, scale class, schema authority, migration tooling,
replication or failover, security, or recovery objectives materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
