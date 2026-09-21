---
name: gd-data-pipelines
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review data-pipeline engineering work for source contracts, replay, idempotency, late data, schema drift, data quality, lineage, and recovery."
---

# Data pipelines GrumpyDev review

## Quick checks

- Read source and sink contracts, checkpoints, watermark rules, schemas,
  transformation code, orchestration, and quality checks.

- Trace one record from ingestion through validation, enrichment, deduplication,
  publication, replay, and deletion.

Watch especially for duplicate effects under at-least-once delivery, late data
outside watermark assumptions, schema drift, poison records blocking progress,
partial reruns that double count, backfills competing with live work, and local
event time confused with processing time.

- Assess silent data loss, unreconcilable output, or a replay that changes
  committed meaning under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Data pipelines
specialist.

## Verdict context

State delivery semantics, replay boundary, data-quality gates, schema policy,
lineage, and recovery evidence.
