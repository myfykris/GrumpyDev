# MongoDB survey contribution

## Applicability

Apply this contribution when the project stores or queries application data in MongoDB.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

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

Keep one-off query profiles, current member identities or replica lag, transient
balancer and cache readings, temporary migration batches, and copied documents
out of durable MongoDB doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey MongoDB when its version or provider, replica-set or sharded topology,
shard key, document model or validation, index strategy, read or write concern,
transaction use, change streams, balancer policy, security boundary, backup, or
recovery objective materially changes. Also re-survey when evidence conflicts
with saved doctrine or the user requests a context refresh.
