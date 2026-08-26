# SQL survey contribution

## Applicability

Apply this contribution when a plan adds or changes SQL queries, reports, stored
routines, views, or database access logic independent of one storage engine.
Skip it when SQL does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

## Inspect before asking

For SQL, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Database engines and versions, SQL modes,
  isolation defaults, collation and encoding, migration tooling, connection
  layer, read replicas, and compatibility requirements.
- Review doctrine for: Dialect differences, NULL and three-valued logic, types,
  collation, joins, aggregates, transactions, isolation, constraints, locking,
  query plans, pagination, injection, and schema evolution.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: Use the selected storage skill for topology.
  Add a question only when SQL is executed through a materially different
  engine, client, proxy, migration runner, or transaction boundary.

## Ask only when materially unresolved

- Which SQL dialect, database version, schema, collation, isolation level, and
  migration state apply?
- What cardinality, locking, null, transaction, parameterization, pagination,
  and query-plan behavior applies?
- Do not add a standing infrastructure question for this specialist. Use the
  selected storage skill for topology. Add a question only when SQL is executed
  through a materially different engine, client, proxy, migration runner, or
  transaction boundary.

## Record in .grump

Record SQL answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

If the SQL boundary becomes material, record it on the affected `DEP-###`
profile or referenced `INF-###` component. Preserve separate state, support,
ownership, confidence, source, and scope fields. Otherwise add no
infrastructure doctrine for this contribution.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable SQL doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey SQL when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
