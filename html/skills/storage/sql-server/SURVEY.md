# SQL Server survey contribution

## Applicability

Apply this contribution when the project stores or queries data in Microsoft SQL Server
or Azure SQL.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

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

Keep one-off execution plans, current session or transaction IDs, transient wait
and replica-lag readings, temporary migration batches, and copied row data out
of durable SQL Server doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey SQL Server when its version, edition or Azure service, compatibility
level, collation, isolation model, storage layout, schema authority, migration
tool, authentication, availability-group or replication topology, backup chain,
or recovery objective materially changes. Also re-survey when evidence
conflicts with saved doctrine or the user requests a context refresh.
