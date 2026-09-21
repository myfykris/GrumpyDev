# MySQL full-review guidance

## Operating conditions

Establish the project target: MySQL or compatible product and version, storage
engine, SQL modes, character set and collation, topology, isolation, migration
tooling, and backup or restore process. The changed boundary must define: Engine
behavior, types, collations, indexes, locking, isolation, replication, online
DDL, SQL modes, migrations, query plans, and restore.

## Failure patterns

- Verify storage engine, SQL mode, charset, collation, timezone, and
  case-sensitivity assumptions explicitly.
- Apply only guarantees documented for the selected product, engine, and
  version; MySQL-compatible products are not interchangeable by default.
- Check online DDL behavior, table rebuilds, metadata locks, rollback limits,
  and deploy ordering on production-sized data.
- Require indexes justified by real query shapes and `EXPLAIN` evidence; include
  composite prefix order and covering tradeoffs.
- Define isolation and locking expectations for lost updates, gap locks,
  deadlocks, and retry safety.
- Treat replica lag, promotion, binlog format, backup retention, and tested
  point-in-time restore as part of correctness.

## Verification to run or specify in the plan

- Rehearse DDL and backfills on representative tables using the selected
  engine, SQL modes, and collation. Observe metadata locks, table copies,
  temporary space, and compatibility with old application code.
- Run conflicting transactions and deadlock retries, then test replica lag and
  promotion where replication is used. Restore a backup, apply the intended
  recovery logs, and verify data, grants, and application queries.
