# Data pipelines full-review guidance

## Operating conditions

Establish the project target: Pipeline engine, batch or stream modes, source and
sink ownership, delivery guarantees, retention, schema governance, lateness
policy, and backfill limits. The changed boundary must define: Batch and stream
semantics, schemas, event time, ordering, deduplication, replay, checkpoints,
backfills, late data, lineage, quality, and recovery.

## Failure patterns

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

## Verification to run or specify in the plan

- Replay duplicate, late, out-of-order, and malformed records through the real
  source-to-sink path. Interrupt a batch between sink writes and checkpoint
  updates, then verify restart does not lose or double-count data.
- Compare incremental output and backfills with a clean rebuild using the same
  source range. Verify reconciliation detects missing records and operators
  can quarantine poison records without silently skipping valid work.
