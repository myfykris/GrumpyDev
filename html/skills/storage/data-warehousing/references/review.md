# Data warehousing full-review guidance

## Operating conditions

Establish the project target: Warehouse product and version, modeling
conventions, ingestion and transformation tools, refresh SLAs, data volumes,
lineage, access model, and cost constraints. The changed boundary must define:
Dimensional models, facts and dimensions, grain, slowly changing dimensions,
ingestion, transformations, late data, lineage, quality, cost, and
reproducibility.

## Failure patterns

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

## Verification to run or specify in the plan

- Load duplicate keys, late facts, changed dimensions, corrections, and
  deletions. Compare incremental results with a clean rebuild at the declared
  fact grain and verify joins do not multiply totals.
- Run backfills alongside scheduled reporting with representative data. Check
  pruning, scan cost, freshness, access controls, and the ability to
  reconstruct results from retained source data.
