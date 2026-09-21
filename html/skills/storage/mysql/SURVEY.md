# MySQL survey contribution

## Applies when

Apply this contribution when the project stores or queries data in MySQL or a compatible
relational database.

## Inspect

- Read engine and version settings, DDL, migrations, constraints, indexes, query
  plans, transactions, replicas, backups, and restore tests.

## Ask when unresolved

- Which MySQL-compatible product, exact version, storage engine, SQL mode,
  replication, and hosting model apply?

- What locking limits, collation rules, transaction guarantees, index needs,
  migration restrictions, and mixed-version compatibility must be preserved?

- Which runtime or deployment differences materially change future reviews:
  Hosting model, managed service, nodes, primary and replicas, read routing,
  network and TLS, connection pooling, storage, failover, backup, restore,
  capacity, and operational ownership?

## Record

Map MySQL data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
