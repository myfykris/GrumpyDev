# Data warehousing standard review

## Establish the operating model

Establish the project target: Warehouse product and version, modeling
conventions, ingestion and transformation tools, refresh SLAs, data volumes,
lineage, access model, and cost constraints. The changed boundary must define:
Dimensional models, facts and dimensions, grain, slowly changing dimensions,
ingestion, transformations, late data, lineage, quality, cost, and
reproducibility.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Dimensional models, facts and dimensions, grain, slowly
changing dimensions, ingestion, transformations. Prove late data, lineage,
quality, cost, reproducibility under concurrent access, mixed versions,
failover, interrupted migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

- Require one declared grain per fact model and tests that prevent accidental
  fan-out or double counting.
- Define surrogate keys, slowly changing dimensions, late-arriving facts,
  deletes, corrections, and source identifier reuse.
- Make incremental models replayable and compare them with clean rebuilds to
  detect silent drift.
- Specify timezone, currency, precision, null, and business-calendar semantics
  at ingestion and reporting boundaries.
- Treat workload isolation, partition pruning, scan volume, retention, row-level
  access, lineage, and cost limits as architecture.

## Verify the claims

- Verify these behaviors through the declared Data warehousing topology and
  workload: Dimensional models, facts and dimensions, grain, slowly changing
  dimensions, ingestion, transformations. Use production-shaped scale and
  workload while observing latency, resource use, locks or conflicts,
  replication, and application errors.
- Exercise failure and edge behavior for: late data, lineage, quality, cost,
  reproducibility. Exercise concurrent writers, retries, duplicate operations,
  failover, interrupted migration, and mixed application versions where
  applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which warehouse product, ingestion cadence, source-of-truth boundary, and
  freshness contract apply?
- How are late data, duplicates, schema drift, backfills, reconciliation, and
  metric ownership handled?

## Calibrate findings

- Downgrade when data is exploratory and labeled or lineage, reconciliation, and
  repeatable backfills are demonstrated.
