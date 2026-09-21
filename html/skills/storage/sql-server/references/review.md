# SQL Server full-review guidance

## Operating conditions

Establish the project target: SQL Server version and edition, compatibility
level, collation, topology, isolation options, migration tooling, maintenance
jobs, and backup or recovery objectives. The changed boundary must define:
Types, collations, indexes, locking and row versioning, execution plans,
statistics, temporal features, availability groups, migrations, and restore.

## Failure patterns

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

## Verification to run or specify in the plan

- Capture actual execution plans for representative and skewed parameters. Run
  concurrent transactions and migrations while observing blocking, deadlocks,
  row-version storage, and transaction-log growth.
- Rehearse the supported failover path if high availability is configured.
  Restore backups and recovery logs, then verify integrity, permissions,
  compatibility level, and application behavior.
