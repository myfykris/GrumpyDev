# MariaDB full-review guidance

## Operating conditions

Establish the project target: MariaDB version, engine, SQL modes, character set
and collation, topology, Galera or replication, isolation, migration tooling,
and backup or restore objectives. The changed boundary must define: MariaDB and
MySQL divergence, engines, types, collations, indexes, locking, isolation,
replication, Galera, online DDL, SQL modes, migrations, query plans, and
recovery.

## Failure patterns

- Verify every material claim against the selected MariaDB product, version,
  storage engine, SQL mode, connector, and hosting restrictions. Do not infer
  current MariaDB behavior from MySQL compatibility labels.

## Verification to run or specify in the plan

- Exercise concurrent writes, deadlocks, retry paths, primary failover or Galera
  partition, and client reconnection.
- Restore backups into an isolated environment and verify schema, data, users,
  routines, events, encodings, and application startup.
