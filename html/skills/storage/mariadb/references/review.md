# MariaDB standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Verify every material claim against the selected MariaDB product, version,
  storage engine, SQL mode, connector, and hosting restrictions. Do not infer
  current MariaDB behavior from MySQL compatibility labels.

## Verify the claims

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

- Treat data loss, corruption, prolonged unavailability, broken concurrent
  invariants, or a recovery mechanism that cannot meet the stated objective as
  material when the reviewed work depends on it and lacks either a safe design or
  credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
