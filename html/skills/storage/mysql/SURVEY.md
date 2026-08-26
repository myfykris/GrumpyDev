# MySQL survey contribution

## Applicability

Apply this contribution when a plan creates, changes, queries, or operates MySQL
or compatible relational databases. Skip it when MySQL does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For MySQL, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: MySQL or compatible product and version, storage
  engine, SQL modes, character set and collation, topology, isolation, migration
  tooling, and backup or restore process.
- Review doctrine for: Engine behavior, types, collations, indexes, locking,
  isolation, replication, online DDL, SQL modes, migrations, query plans, and
  restore.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Hosting model, managed service, nodes, primary
  and replicas, read routing, network and TLS, connection pooling, storage,
  failover, backup, restore, capacity, and operational ownership.

## Ask only when materially unresolved

- Which MySQL-compatible product, exact version, storage engine, SQL mode,
  replication, and hosting model apply?
- What lock, rewrite, collation, transaction, index, and
  mixed-application-version behavior applies to the change?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Hosting model, managed service,
  nodes, primary and replicas, read routing, network and TLS, connection
  pooling, storage, failover, backup, restore, capacity, and operational
  ownership? Ask only when evidence and the core profile confirmation do not
  resolve them.

## Record in .grump

Record MySQL answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Record confirmed MySQL deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable MySQL
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey MySQL when product version or provider, topology, engine, consistency
policy, scale class, schema authority, migration tooling, replication or
failover, security, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
