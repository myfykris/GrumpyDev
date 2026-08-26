---
name: data-warehousing
description: Review data-warehouse plans for dimensional models, grain, slowly changing dimensions, ingestion, freshness, cost, governance, and reconciliation. Use when a plan builds analytical models or operates a columnar cloud warehouse.
---

# Data warehousing plan review

Apply this guidance alongside the core GrumpyDev review and the `data-pipelines`
skill.

## Inspect evidence

- Read source contracts, model grain, keys, dimensions and facts, incremental
  logic, partitions, quality tests, lineage, access controls, and cost reports.
- Trace a business metric from source records through late updates, backfills,
  model rebuilds, dashboards, and reconciliation.

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

## Challenge the plan

### Recurring traps

Watch especially for fact-table grain left ambiguous, slowly changing dimensions
applied inconsistently, late-arriving facts assigned to the wrong version, joins
that double count, local time mixed across sources, backfills overwhelming
shared compute, and dashboards bypassing governed semantic definitions.

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

- Treat silently incorrect business metrics, unreconcilable history, or a
  destructive backfill without recovery as critical.
- Downgrade when data is exploratory and labeled or lineage, reconciliation, and
  repeatable backfills are demonstrated.

## Add to the verdict

State model grain, metric reconciliation, history and backfill behavior,
governance boundaries, freshness, and cost evidence.
