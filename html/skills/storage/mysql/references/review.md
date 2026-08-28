# MySQL standard review

## Establish the operating model

Establish the project target: MySQL or compatible product and version, storage
engine, SQL modes, character set and collation, topology, isolation, migration
tooling, and backup or restore process. The changed boundary must define: Engine
behavior, types, collations, indexes, locking, isolation, replication, online
DDL, SQL modes, migrations, query plans, and restore.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Engine behavior, types, collations, indexes, locking,
isolation. Prove replication, online DDL, SQL modes, migrations, query plans,
restore under concurrent access, mixed versions, failover, interrupted
migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared MySQL topology and workload:
  Engine behavior, types, collations, indexes, locking, isolation. Use
  production-shaped scale and workload while observing latency, resource use,
  locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: replication, online DDL, SQL modes,
  migrations, query plans, restore. Exercise concurrent writers, retries,
  duplicate operations, failover, interrupted migration, and mixed application
  versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which MySQL-compatible product, exact version, storage engine, SQL mode,
  replication, and hosting model apply?
- What lock, rewrite, collation, transaction, index, and
  mixed-application-version behavior applies to the change?

## Calibrate findings

- Downgrade when product-specific migration evidence, constraints,
  representative queries, and restore behavior are proven.
