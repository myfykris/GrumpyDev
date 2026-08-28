# Data warehousing survey contribution

## Applicability

Apply this contribution when the project builds analytical models or operates a columnar
cloud data warehouse.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Data warehousing, inspect product and client declarations, migration
configuration, schema sources, indexes or key definitions, topology and
infrastructure files, backup and restore runbooks, capacity evidence, and
operational ownership. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Warehouse product and version, modeling
  conventions, ingestion and transformation tools, refresh SLAs, data volumes,
  lineage, access model, and cost constraints.
- Review doctrine for: Dimensional models, facts and dimensions, grain, slowly
  changing dimensions, ingestion, transformations, late data, lineage, quality,
  cost, and reproducibility.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Product, compute and storage separation, regions,
  ingestion and transformation runtimes, workload isolation, schedules,
  semantic layer, backfill capacity, retention, and recovery.

## Ask only when materially unresolved

- Which warehouse product, ingestion cadence, source-of-truth boundary, and
  freshness contract apply?
- How are late data, duplicates, schema drift, backfills, reconciliation, and
  metric ownership handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Product, compute and storage separation,
  regions, ingestion and transformation runtimes, workload isolation,
  schedules, semantic layer, backfill capacity, retention, and recovery? Ask
  only when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Data warehousing answers in project technology, data, schema,
consistency, deployment, and recovery doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Data warehousing deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep one-off query profiles, current warehouse or slot assignments, transient
job and load readings, temporary backfill batches, and copied business data out
of durable data-warehousing doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey data warehousing when the platform or provider, compute and storage
model, workload ownership, dimensional model, partitioning or clustering,
ingestion and transformation tools, materialization policy, concurrency and
cost controls, governance, retention, or recovery objectives materially change.
Also re-survey when evidence conflicts with saved doctrine or the user requests
a context refresh.
