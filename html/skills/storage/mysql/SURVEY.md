# MySQL survey contribution

## Applicability

Apply this contribution when the project stores or queries data in MySQL or a compatible
relational database.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

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

Keep one-off EXPLAIN output, current connection or transaction IDs, transient
replica lag and load readings, temporary migration batches, and copied row data
out of durable MySQL doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey MySQL when its version or provider, storage engine, SQL mode,
collation, isolation level, schema authority, migration tool, replication or
group-replication topology, read routing, authentication, backup chain, or
recovery objective materially changes. Also re-survey when evidence conflicts
with saved doctrine or the user requests a context refresh.
