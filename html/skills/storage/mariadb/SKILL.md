---
name: mariadb
description: Review MariaDB plans for MySQL divergence, engines, types, collations, indexes, locking, isolation, replication, Galera, online DDL, SQL modes, migrations, query plans, and recovery. Use when a plan changes MariaDB schemas, queries, topology, or operations.
---

# MariaDB plan review

Apply this guidance alongside the core GrumpyDev review and the `sql`,
application framework, deployment, and recovery skills. Select only companions
that match the plan's real boundaries. Verify behavior against the project's
declared targets; do not silently substitute the newest version, a development
default, or a neighboring product's semantics.

## Inspect evidence

- Inspect server and compatibility settings, engines, schemas, migrations,
  indexes, constraints, queries and plans, transaction boundaries, replication
  or Galera configuration, backups, and restore runbooks.
- Compare repository declarations with the effective schema and operating
  topology where safely available. Model files and migration sources are
  evidence, not proof of current state.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: MariaDB version, engine, SQL modes, character set
and collation, topology, Galera or replication, isolation, migration tooling,
and backup or restore objectives. The changed boundary must define: MariaDB and
MySQL divergence, engines, types, collations, indexes, locking, isolation,
replication, Galera, online DDL, SQL modes, migrations, query plans, and
recovery.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for MariaDB and MySQL divergence, engines, types, collations,
indexes, locking, isolation. Prove replication, Galera, online DDL, SQL modes,
migrations, query plans, recovery under concurrent access, mixed versions,
failover, interrupted migration, rollback, and restore.

## Challenge the plan

### Recurring traps

Watch especially for MySQL compatibility assumed without version evidence,
Galera certification conflicts and retry behavior, auto-increment assumptions
across nodes, collation differences, online DDL that still locks, replication
formats changing effects, and failover promoting data that is not current.

- Verify every behavior against MariaDB rather than assuming current MySQL
  compatibility. Check syntax, data types, JSON behavior, optimizer features,
  replication, authentication, connectors, system variables, and migration
  tooling for the declared versions.
- Analyze storage-engine boundaries, transactions, foreign keys, crash recovery,
  full text, locking, and backup behavior. A server-wide transaction does not
  make nontransactional tables atomic.
- Preserve character set and collation explicitly across server, database,
  table, column, connection, client, dump, and restore. Test uniqueness and
  ordering after any collation conversion.
- For DDL, determine lock mode, algorithm, table copy or rebuild, temporary
  space, transaction-log impact, replica/Galera behavior, cancellation, and
  old/new application compatibility.
- Trace isolation, gap and record locks, deadlocks, optimistic conditions,
  retries, auto-increment behavior, and multi-writer conflicts. Re-run the whole
  decision safely after retry.
- Match indexes and query plans to production-shaped data, parameter
  distributions, predicates, ordering, and write cost. Include statistics and
  plan changes after upgrades.
- For replication or Galera, define consistency, quorum, flow control, conflict,
  state transfer, failover, fencing, lag, read routing, and rejoin behavior
  under partition.
- Require tested logical and physical backups, point-in-time capability where
  needed, encryption, retention, version compatibility, and full restore
  evidence including users and server settings.

## Verify the claims

- Rehearse migrations under representative scale while observing locks,
  temporary space, replication, flow control, and application errors.
- Capture query plans and load evidence before and after schema, data,
  configuration, or version changes.
- Exercise concurrent writes, deadlocks, retry paths, primary failover or Galera
  partition, and client reconnection.
- Restore backups into an isolated environment and verify schema, data, users,
  routines, events, encodings, and application startup.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: MariaDB version,
engine, SQL modes, character set and collation, topology, Galera or replication,
isolation, migration tooling, and backup or restore objectives. For the changed
boundary, ask only about unresolved MariaDB and MySQL divergence, engines,
types, collations, indexes, locking, isolation, replication, Galera, online DDL,
SQL modes, migrations, query plans, and recovery when the answer can change the
verdict or implementation.

## Calibrate findings

- Treat data loss, prolonged blocking, split-brain writes, broken uniqueness
  after collation change, or an untested recovery path for critical data as
  critical or high according to blast radius and realistic likelihood.
- Treat data loss, corruption, prolonged unavailability, broken concurrent
  invariants, or a recovery mechanism that cannot meet the stated objective as
  material when the plan depends on it and lacks either a safe design or
  credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
MariaDB and MySQL divergence, storage engines, types, collations, indexes,
locking, isolation, replication, Galera, online DDL, SQL modes, migrations,
query plans, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
