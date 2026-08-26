# SQL Server survey contribution

## Applicability

Apply this contribution when a plan creates, changes, queries, or operates
Microsoft SQL Server or Azure SQL. Skip it when SQL Server does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For SQL Server, inspect product and client declarations, migration
configuration, schema sources, indexes or key definitions, topology and
infrastructure files, backup and restore runbooks, capacity evidence, and
operational ownership. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: SQL Server version and edition, compatibility
  level, collation, topology, isolation options, migration tooling, maintenance
  jobs, and backup or recovery objectives.
- Review doctrine for: Types, collations, indexes, locking and row versioning,
  execution plans, statistics, temporal features, availability groups,
  migrations, and restore.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product, version, edition, hosting, instances,
  databases, availability groups, isolation, storage, tempdb, migration,
  backup, restore, failover, and driver behavior.

## Ask only when materially unresolved

- Which SQL Server or Azure SQL product, exact version, edition, compatibility
  level, and availability model apply?
- What lock, statistics, online-operation, transaction, replication, and restore
  behavior applies to the change?
- Align existing domain questions with this deployment guidance when it is
  material: Product, version, edition, hosting, instances, databases,
  availability groups, isolation, storage, tempdb, migration, backup, restore,
  failover, and driver behavior. Do not repeat the core profile confirmation.

## Record in .grump

Record SQL Server answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing SQL Server survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable SQL Server
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey SQL Server when product version or provider, topology, engine,
consistency policy, scale class, schema authority, migration tooling,
replication or failover, security, or recovery objectives materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
