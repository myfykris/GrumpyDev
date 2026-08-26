# MongoDB survey contribution

## Applicability

Apply this contribution when a plan stores or queries application data in
MongoDB. Skip it when MongoDB does not constrain a supported build, runtime,
client, data, deployment, or operating boundary.

## Inspect before asking

For MongoDB, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: MongoDB version, replica or shard topology, read
  and write concerns, drivers, schema and index ownership, transaction use,
  backup, and data-volume profile.
- Review doctrine for: Document boundaries, schema validation, indexes,
  transactions, read and write concerns, replication, sharding, change streams,
  migrations, and backup.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product and version, managed or self-hosted
  mode, replica set or sharding, regions, read and write concerns, storage,
  backup, restore, failover, and driver behavior.

## Ask only when materially unresolved

- Which MongoDB version, topology, storage mode, read concern, write concern,
  and transaction use apply?
- How are schema variation, indexes, retries, migrations, replication lag, and
  restore handled?
- Align existing domain questions with this deployment guidance when it is
  material: Product and version, managed or self-hosted mode, replica set or
  sharding, regions, read and write concerns, storage, backup, restore,
  failover, and driver behavior. Do not repeat the core profile confirmation.

## Record in .grump

Record MongoDB answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing MongoDB survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable MongoDB
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey MongoDB when product version or provider, topology, engine,
consistency policy, scale class, schema authority, migration tooling,
replication or failover, security, or recovery objectives materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
