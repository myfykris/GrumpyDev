# PostgreSQL survey contribution

## Applies when

Apply this contribution when PostgreSQL stores project data, supports tests or analytics
that constrain implementation, or is a deployment dependency.

## Inspect

- Inspect the actual schema, constraints, indexes, policies, extensions,
  migrations, transaction boundaries, and representative scale. An ORM model is
  not evidence of current database state.

## Ask when unresolved

- Which server versions, pooler mode, overlapping deployment versions, scale,
  uptime requirements, restore ownership, and replica-staleness policy govern
  PostgreSQL work?

- Which runtime or deployment differences are material for future reviews:
  product and version, extensions, managed or self-hosted topology, replicas,
  pooling, storage, vacuum, migration, backup, restore, failover, and lag
  coverage?

## Record

Map PostgreSQL data guarantees to `Requirements`, accepted tradeoffs to
`Accepted decisions`, topology and recovery facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
