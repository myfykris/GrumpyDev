# Data pipelines standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when outputs are disposable or lineage, idempotent replay, quality
  checks, and reconciliation are proven.
