# Event sourcing and CQRS full-review guidance

## Operating conditions

Identify CQRS, event sourcing, or their combination. Establish command
invariants, authoritative storage, read models, transaction boundaries, and
read freshness requirements. Separate read and write models may share one
database. Separate stores, asynchronous messages, and eventual consistency are
design choices, not requirements of CQRS.

For event-sourced state, also establish event-store guarantees, stream
boundaries, event versions, replay scale, and deletion constraints. Inspect
snapshots only when used; do not prescribe them as mandatory infrastructure.

## Failure patterns

- Demand a concrete need for historical reconstruction or independent read
  models; CRUD with extra steps is a bad trade.
- Enforce command invariants at the actual write boundary, including concurrent
  commands and retries. Select concurrency controls for the store in use.
- Check that read models preserve authorization and do not silently change
  business meanings. State whether a read must observe the preceding write.
- When models use separate stores, define synchronization, duplicate and missing
  update handling, freshness, and repair from the authoritative data. A shared
  database design need not invent this machinery.
- For event sourcing, verify expected-version checks or equivalent conflict
  protection at append, and how old events remain readable as code and schemas
  change. Replay must reconstruct state without repeating live side effects.
- For event-sourced projections, verify restartable rebuilds and checkpoints.
  Address corrections, privacy deletion, storage growth, and snapshot
  invalidation when snapshots are used.

## Verification to run or specify in the plan

- Submit competing and repeated commands, then query through the real read
  model. Check invariants, authorization, and the promised read-after-write
  behavior.
- With separate stores, delay, duplicate, and interrupt updates; verify the
  consumer can resume or repair from the actual source of truth.
- With event sourcing, replay retained event versions, interrupt a rebuild, and
  compare reconstructed state with expected results. Verify corrections and
  deletion policies without sending live external effects during replay.
