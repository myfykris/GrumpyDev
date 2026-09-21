# Data pipelines survey contribution

## Applies when

Apply this contribution when the project ingests, transforms, moves, or aggregates data
in batches or streams.

## Inspect

- Read source and sink contracts, checkpoints, watermark rules, schemas,
  transformation code, orchestration, and quality checks.

## Ask when unresolved

- What source-of-truth, delivery, ordering, watermark, and replay contract
  applies at each stage?

- How are duplicates, late data, schema changes, partial reruns,
  reconciliation, and bad records handled?

- Which runtime or deployment differences materially change future reviews:
  Orchestrator, execution engine, batch or streaming mode, partitions,
  checkpoints, object or table storage, regions, backfill capacity, and
  recovery ownership?

## Record

Map accepted Data pipelines architecture choices to `Accepted decisions`,
binding boundaries to `Requirements` or `Constraints`, and material gaps to
`Unknowns`.
