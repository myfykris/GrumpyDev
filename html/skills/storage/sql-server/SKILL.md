---
name: sql-server
description: Review SQL Server plans for schema changes, indexes, statistics, transactions, locking, availability, security, and restore. Use when a plan creates, changes, queries, or operates Microsoft SQL Server or Azure SQL.
---

# SQL Server plan review

Apply this guidance alongside the core GrumpyDev review and the `sql` skill.

## Inspect evidence

- Establish the exact SQL Server or Azure SQL product, version, edition,
  compatibility level, hosting mode, and feature set.
- Read compatibility level, DDL, migrations, indexes, query plans, statistics,
  isolation settings, jobs, availability topology, and restore tests.
- Trace critical queries and writes through parameterization, locking, failover,
  retries, and mixed application versions.

## Establish the operating model

Establish the project target: SQL Server version and edition, compatibility
level, collation, topology, isolation options, migration tooling, maintenance
jobs, and backup or recovery objectives. The changed boundary must define:
Types, collations, indexes, locking and row versioning, execution plans,
statistics, temporal features, availability groups, migrations, and restore.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Types, collations, indexes, locking and row versioning,
execution plans. Prove statistics, temporal features, availability groups,
migrations, restore under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the plan

### Recurring traps

Watch especially for plan-cache and parameter-sensitivity regressions, implicit
conversions disabling useful indexes, lock escalation, snapshot isolation
pressure on tempdb, identity values assumed contiguous, online operations
unavailable in the deployed edition, and availability replicas serving data
beyond acceptable lag.

- Check implicit conversions, collations, date and numeric types, identity
  behavior, and session settings at every application boundary.
- Apply only guarantees documented for the selected SQL Server or Azure SQL
  variant; deployment models are not interchangeable.
- Require actual execution-plan and workload evidence for indexes; account for
  parameter sensitivity, statistics, and write amplification.
- Define blocking, deadlock retry, snapshot isolation, lock escalation, and
  long-transaction behavior explicitly.
- Test migration locking and log growth on production-sized data, including
  rollback and availability-group consequences.
- Prove least privilege, encryption, backup retention, integrity checks, and
  point-in-time restore rather than trusting job success.

## Verify the claims

- Verify these behaviors through the declared SQL Server topology and workload:
  Types, collations, indexes, locking and row versioning, execution plans. Use
  production-shaped scale and workload while observing latency, resource use,
  locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: statistics, temporal features,
  availability groups, migrations, restore. Exercise concurrent writers,
  retries, duplicate operations, failover, interrupted migration, and mixed
  application versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which SQL Server or Azure SQL product, exact version, edition, compatibility
  level, and availability model apply?
- What lock, statistics, online-operation, transaction, replication, and restore
  behavior applies to the change?

## Calibrate findings

- Treat data loss, prolonged blocking, broken invariants, or use of unsupported
  variant behavior as critical.
- Downgrade when variant-specific migration, query, availability, and restore
  evidence covers the supported environment.

## Add to the verdict

State compatibility and encoding choices, plan evidence, locking and isolation
behavior, availability assumptions, and restore proof.
