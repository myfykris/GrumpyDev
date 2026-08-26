# SQLite survey contribution

## Applicability

Apply this contribution when an application embeds SQLite or shares a SQLite
database file. Skip it when SQLite does not constrain a supported build,
runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For SQLite, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: SQLite library versions, bindings, file location,
  filesystem semantics, journal mode, connection and process topology,
  foreign-key policy, backup, and data size.
- Review doctrine for: File and connection model, locking, WAL, transactions,
  foreign keys, type affinity, migrations, corruption boundaries, backups,
  threading, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Library version, process and connection
  topology, filesystem and mount, WAL behavior, write concurrency, packaging,
  backup, restore, encryption if used, and network-filesystem exclusions.

## Ask only when materially unresolved

- Which SQLite library version, build options, filesystem, process model,
  journal mode, and connection ownership apply?
- How are writer contention, busy handling, migrations, type affinity, backup,
  and file replacement coordinated?
- Align existing domain questions with this deployment guidance when it is
  material: Library version, process and connection topology, filesystem and
  mount, WAL behavior, write concurrency, packaging, backup, restore,
  encryption if used, and network-filesystem exclusions. Do not repeat the core
  profile confirmation.

## Record in .grump

Record SQLite answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing SQLite survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable SQLite
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey SQLite when product version or provider, topology, engine, consistency
policy, scale class, schema authority, migration tooling, replication or
failover, security, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
