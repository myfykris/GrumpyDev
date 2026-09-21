# SQL Server survey contribution

## Applies when

Apply this contribution when the project stores or queries data in Microsoft SQL Server
or Azure SQL.

## Inspect

- Establish the exact SQL Server or Azure SQL product, version, edition,
  compatibility level, hosting mode, and feature set.

## Ask when unresolved

- Which SQL Server or Azure SQL product, exact version, edition, compatibility
  level, and availability model apply?

- What locking limits, statistics maintenance, online-operation requirements,
  transaction guarantees, replication, and restore objectives must be preserved?

- Which runtime or deployment differences are material for future reviews:
  Product, version, edition, hosting, instances, databases, availability
  groups, isolation, storage, tempdb, migration, backup, restore, failover, and
  driver behavior?

## Record

Map SQL Server data guarantees to `Requirements`, accepted tradeoffs to
`Accepted decisions`, topology and recovery facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
