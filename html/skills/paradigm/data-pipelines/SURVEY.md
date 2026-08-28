# Data pipelines survey contribution

## Applicability

Apply this contribution when the project ingests, transforms, moves, or aggregates data
in batches or streams.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Data pipelines, inspect architecture records, module or service maps,
dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Pipeline engine, batch or stream modes, source and
  sink ownership, delivery guarantees, retention, schema governance, lateness
  policy, and backfill limits.
- Review doctrine for: Batch and stream semantics, schemas, event time,
  ordering, deduplication, replay, checkpoints, backfills, late data, lineage,
  quality, and recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Orchestrator, execution engine, batch or streaming
  mode, partitions, checkpoints, object or table storage, regions, backfill
  capacity, and recovery ownership.

## Ask only when materially unresolved

- What source-of-truth, delivery, ordering, watermark, and replay contract
  applies at each stage?
- How are duplicates, late data, schema changes, partial reruns, reconciliation,
  and bad records handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Orchestrator, execution engine, batch or
  streaming mode, partitions, checkpoints, object or table storage, regions,
  backfill capacity, and recovery ownership? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Data pipelines answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Data pipelines deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Data pipelines doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Data pipelines when business invariants, ownership boundaries, data
authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
