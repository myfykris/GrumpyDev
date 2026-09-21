# MariaDB survey contribution

## Applies when

Apply this contribution when the project uses MariaDB or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect server and compatibility settings, engines, schemas, migrations,
  indexes, constraints, queries and plans, transaction boundaries, replication
  or Galera configuration, backups, and restore runbooks.

## Ask when unresolved

- Which of these durable facts materially change future reviews: MariaDB
  version, engine, SQL modes, character set and collation, topology, Galera or
  replication, isolation, migration tooling, and backup or restore objectives?

- Which runtime or deployment differences are material for future reviews:
  product and version, engine, SQL modes, character settings, topology, Galera
  or replication, isolation, migration, backup, restore, failover, and hosting
  coverage?

## Record

Map MariaDB data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
