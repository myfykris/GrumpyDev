---
name: gd-data-warehousing
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review data-warehouse engineering work for dimensional models, grain, slowly changing dimensions, ingestion, freshness, cost, governance, and reconciliation."
---

# Data warehousing GrumpyDev review

## Quick checks

- Read source contracts, model grain, keys, dimensions and facts, incremental
  logic, partitions, quality tests, lineage, access controls, and cost reports.

- Trace a business metric from source records through late updates, backfills,
  model rebuilds, dashboards, and reconciliation.

Watch especially for fact-table grain left ambiguous, slowly changing dimensions
applied inconsistently, late-arriving facts assigned to the wrong version, joins
that double count, local time mixed across sources, backfills overwhelming
shared compute, and dashboards bypassing governed semantic definitions.

- Assess silently incorrect business metrics, unreconcilable history, or a
  destructive backfill without recovery under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Data warehousing
specialist.

## Verdict context

State model grain, metric reconciliation, history and backfill behavior,
governance boundaries, freshness, and cost evidence.
