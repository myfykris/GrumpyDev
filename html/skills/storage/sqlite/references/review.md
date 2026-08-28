# SQLite standard review

## Inspect additional evidence

- Trace readers and writers across threads, processes, containers, crashes,
  upgrades, and file replacement.

## Establish the operating model

Establish the project target: SQLite library versions, bindings, file location,
filesystem semantics, journal mode, connection and process topology, foreign-key
policy, backup, and data size. The changed boundary must define: File and
connection model, locking, WAL, transactions, foreign keys, type affinity,
migrations, corruption boundaries, backups, threading, and deployment.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for File and connection model, locking, WAL, transactions,
foreign keys, type affinity. Prove migrations, corruption boundaries, backups,
threading, deployment under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared SQLite topology and workload: File
  and connection model, locking, WAL, transactions, foreign keys, type affinity.
  Use production-shaped scale and workload while observing latency, resource
  use, locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: migrations, corruption boundaries,
  backups, threading, deployment. Exercise concurrent writers, retries,
  duplicate operations, failover, interrupted migration, and mixed application
  versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which SQLite library version, build options, filesystem, process model,
  journal mode, and connection ownership apply?
- How are writer contention, busy handling, migrations, type affinity, backup,
  and file replacement coordinated?

## Calibrate findings

- Downgrade when ownership is single-process and bounded or exact runtime,
  transaction, backup, and contention behavior are proven.
