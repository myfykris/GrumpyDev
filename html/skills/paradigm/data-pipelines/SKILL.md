---
name: data-pipelines
description: Review data-pipeline plans for source contracts, replay, idempotency, late data, schema drift, data quality, lineage, and recovery. Use when a plan ingests, transforms, moves, or aggregates data in batches or streams.
---

# Data pipelines plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed storage and platform specialists for the pipeline boundaries in use.

## Inspect evidence

- Read source and sink contracts, checkpoints, watermark rules, schemas,
  transformation code, orchestration, and quality checks.
- Trace one record from ingestion through validation, enrichment, deduplication,
  publication, replay, and deletion.

## Establish the operating model

Establish the project target: Pipeline engine, batch or stream modes, source and
sink ownership, delivery guarantees, retention, schema governance, lateness
policy, and backfill limits. The changed boundary must define: Batch and stream
semantics, schemas, event time, ordering, deduplication, replay, checkpoints,
backfills, late data, lineage, quality, and recovery.

Name the invariants, authorities, owners, and enforcement for Batch and stream
semantics, schemas, event time, ordering, deduplication, replay. Prove
checkpoints, backfills, late data, lineage, quality, recovery under concurrency,
partial failure, incompatible versions, operational response, rollback, and
repair, and justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for duplicate effects under at-least-once delivery, late data
outside watermark assumptions, schema drift, poison records blocking progress,
partial reruns that double count, backfills competing with live work, and local
event time confused with processing time.

- Define delivery semantics at each boundary; "exactly once" is not credible
  without the storage and commit mechanism.
- Check replay safety, stable event identity, partial-batch recovery, poison
  records, and side effects outside transactional sinks.
- Require explicit handling for late, missing, duplicated, malformed, and
  out-of-order data.
- Treat schema evolution, timezone, precision, null semantics, and source
  backfills as compatibility work.
- Demand freshness, completeness, volume, and reconciliation signals that detect
  plausible but wrong output.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Batch and stream semantics, schemas, event time, ordering,
  deduplication, replay. Use dependency, architecture, contract, schema, or
  ownership tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: checkpoints, backfills, late data,
  lineage, quality, recovery. Exercise the material invariant under concurrency,
  delay, duplication, partial failure, incompatible versions, rollback, and
  repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- What source-of-truth, delivery, ordering, watermark, and replay contract
  applies at each stage?
- How are duplicates, late data, schema changes, partial reruns, reconciliation,
  and bad records handled?

## Calibrate findings

- Treat silent data loss, unreconcilable output, or a replay that changes
  committed meaning as critical.
- Downgrade when outputs are disposable or lineage, idempotent replay, quality
  checks, and reconciliation are proven.

## Add to the verdict

State delivery semantics, replay boundary, data-quality gates, schema policy,
lineage, and recovery evidence.
