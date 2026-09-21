---
name: gd-mariadb
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review MariaDB engineering work for MySQL divergence, engines, types, collations, indexes, locking, isolation, replication, Galera, online DDL, SQL modes, migrations, query plans, and recovery."
---

# MariaDB GrumpyDev review

## Quick checks

- Inspect server and compatibility settings, engines, schemas, migrations,
  indexes, constraints, queries and plans, transaction boundaries, replication
  or Galera configuration, backups, and restore runbooks.

- Compare repository declarations with the effective schema and operating
  topology where safely available. Model files and migration sources are
  evidence, not proof of current state.

Watch especially for MySQL compatibility assumed without version evidence,
Galera certification conflicts and retry behavior, auto-increment assumptions
across nodes, collation differences, online DDL that still locks, replication
formats changing effects, and failover promoting data that is not current.

- Inspect data loss, prolonged blocking, split-brain writes, broken uniqueness
  after collation change, or an untested recovery path for critical data.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the MariaDB specialist.

- [Focused rules](references/schema-locking-and-query-plans.md):
  Read when the work changes MariaDB or MySQL
  compatibility, engines, types, JSON
  behavior, SQL modes, character sets, collations, indexes, query plans, isolation,
  record or gap locks, deadlock retries, DDL, online algorithms, table rebuilds,
  temporary space, migrations, or mixed application versions.
- [Focused rules](references/replication-galera-and-recovery.md):
  Read when the work changes replication, Galera,
  quorum, flow control, conflict
  handling, state transfer, failover, fencing, read routing, rejoin, backup,
  point-in-time recovery, encryption, retention, restore, or server-setting recovery.

## Verdict context

State the MariaDB and MySQL divergence, storage engines, types, collations,
indexes, locking, isolation, replication, Galera, online DDL, SQL modes,
migrations, query plans, and recovery, supporting evidence, deployment or
recovery limits, and unresolved material assumptions.
