# Data warehousing survey contribution

## Applies when

Apply this contribution when the project builds analytical models or operates a columnar
cloud data warehouse.

## Inspect

- Read source contracts, model grain, keys, dimensions and facts, incremental
  logic, partitions, quality tests, lineage, access controls, and cost reports.

## Ask when unresolved

- Which warehouse product, ingestion cadence, source-of-truth boundary, and
  freshness contract apply?

- How are late data, duplicates, schema drift, backfills, reconciliation, and
  metric ownership handled?

- Which runtime or deployment differences materially change future reviews:
  Product, compute and storage separation, regions, ingestion and
  transformation runtimes, workload isolation, schedules, semantic layer,
  backfill capacity, retention, and recovery?

## Record

Map Data warehousing data guarantees to `Requirements`, accepted tradeoffs to
`Accepted decisions`, topology and recovery facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
