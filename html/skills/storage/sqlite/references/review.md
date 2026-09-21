# SQLite full-review guidance

## Operating conditions

Establish the project target: SQLite library versions, bindings, file location,
filesystem semantics, journal mode, connection and process topology, foreign-key
policy, backup, and data size. The changed boundary must define: File and
connection model, locking, WAL, transactions, foreign keys, type affinity,
migrations, corruption boundaries, backups, threading, and deployment.

## Failure patterns

- Confirm one process or coordinated hosts own the file; a network filesystem is
  not a transparent database server.
- Define journal mode, busy timeout, transaction mode, synchronous setting,
  foreign-key enforcement, and their durability tradeoffs.
- Account for single-writer contention, long reads, checkpoint behavior, and
  retry handling under actual workload concurrency.
- Check type affinity, nulls, timestamps, collations, row identifiers, and
  constraint behavior rather than assuming another SQL engine's semantics.
- Require migration and online-backup procedures that preserve file integrity
  and are tested against crash interruption.

## Verification to run or specify in the plan

- Run concurrent connections or processes against the actual filesystem and
  journal mode. Check busy handling, long readers, checkpoints, and
  foreign-key enforcement on each new connection.
- Interrupt transactions and table-rebuild migrations, then reopen the
  database and verify invariants. Restore using the selected backup method and
  check WAL handling, schema metadata, and application startup.
