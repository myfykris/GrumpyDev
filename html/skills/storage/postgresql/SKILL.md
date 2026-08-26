---
name: postgresql
description: Review PostgreSQL engineering plans for schema migration, locking, transaction, indexing, query, concurrency, backup, replication, and data-integrity risks. Use when a plan changes PostgreSQL schemas, data access, queries, migrations, replication, or database operations.
---

# PostgreSQL plan review

Apply this guidance alongside the core GrumpyDev review and the `sql` skill. Add
the application framework, migration tool, infrastructure, and backup
specialists that own adjacent behavior. Treat PostgreSQL behavior as
version-specific and verify material claims against the supported server
versions rather than relying on generic SQL assumptions.

## Inspect evidence

- Read the actual schema, constraints, indexes, triggers, generated columns,
  row-level security policies, grants, extensions, and representative data
  distributions. A model definition or ORM migration is not necessarily the
  database's current state.
- Read migration files in deployment order and identify which tool executes
  them, whether each migration is transactional, what timeouts apply, and
  whether multiple application versions can run during the change.
- Establish supported PostgreSQL versions, managed-service restrictions, table
  and index sizes, row counts and growth, write rates, connection limits, pool
  topology, replication, failover, backup, and restore behavior.
- Inspect transaction boundaries, isolation levels, explicit locks, retry loops,
  advisory locks, and every read-modify-write sequence that protects a business
  invariant.
- For query or capacity claims, inspect representative `EXPLAIN (ANALYZE,
  BUFFERS)` evidence in a safe environment with realistic statistics and data
  shape. Do not accept a query plan captured from an empty development table.
- Trace who owns schema changes, data backfills, database credentials, routine
  maintenance, extension installation, replication monitoring, point-in-time
  recovery, and incident decisions.

## Establish the operating model

State the database versions and topology, including primary and replicas,
synchronous or asynchronous replication, failover authority, and whether reads
may be routed to lagging replicas. State the connection-pool mode and limits
because transaction, session, prepared-statement, temporary-object,
notification, and advisory-lock behavior can depend on them.

For each affected table, record approximate scale, write load, availability
requirement, retention, and the old/new application overlap window. Define the
required consistency and durability for every changed invariant. Identify the
system of record, the owners of writes, and whether jobs, scripts, imports, or
other services bypass application validation.

Describe the release sequence as expand, migrate, validate, switch, and contract
where mixed versions or large data sets make a single atomic change unsafe. Name
the recovery mechanism for data as well as code. A down migration that drops or
transforms data is not a rollback plan.

## Challenge the plan

### Recurring traps

Watch especially for long transactions preventing vacuum progress, misunderstood
lock levels, failed concurrent indexes left invalid, serializable transactions
without retry logic, NULL and collation surprises, extension dependencies,
replicas used beyond their lag tolerance, and enum changes coupled to rollback.

### Schema changes and locks

- Analyze the lock mode, lock acquisition risk, table or index rewrite,
  validation scan, transaction duration, WAL generation, replica lag, disk
  headroom, and cancellation behavior for every material DDL operation.
- Require explicit `lock_timeout` and `statement_timeout` decisions for online
  changes. A short operation can still wait behind a long transaction and then
  block everything queued behind it.
- Separate adding a constraint from validating existing rows when scale or
  uptime requires it. Verify which PostgreSQL versions support the planned
  low-lock sequence.
- Treat index creation mode as an operational decision. Concurrent index builds
  avoid the ordinary write lock but take longer, have restrictions, can leave
  invalid indexes after failure, and still require monitoring and cleanup.
- Check default changes, type conversions, generated values, column rewrites,
  partition operations, and extension changes for version-specific behavior. Do
  not infer current behavior from an older PostgreSQL release.

### Data migration and coexistence

- Require backfills to be bounded, restartable, observable, rate-limited, and
  safe under concurrent writes. Define batch selection, progress markers, retry
  behavior, failure quarantine, and how rows changed during the backfill reach
  the new representation.
- Define old-reader/new-writer and new-reader/old-writer behavior. Dual writes
  need an authority rule, ordering semantics, repair path, and a date when they
  end. They are not automatically safer than a database-side transition.
- Require post-backfill validation that checks business invariants, not merely
  row counts. Define the acceptable mismatch threshold and remediation path.
- Preserve the original value until the transformed value is proven when the
  conversion is lossy, hard to reverse, or affected by encoding, time zone,
  locale, precision, or collation.

### Transactions and concurrency

- Prove that transaction boundaries cover the invariant. Framework helpers can
  accidentally perform work outside the transaction or hold transactions open
  across remote calls.
- Analyze isolation behavior, predicate races, lost updates, write skew,
  deadlocks, serialization failures, uniqueness conflicts, and retry safety. A
  transaction alone does not serialize a read-modify-write sequence.
- Prefer database constraints for invariants that must survive concurrency and
  multiple writers. If application code owns an invariant, identify every writer
  and explain why database enforcement is impractical.
- When using row locks, advisory locks, leases, queues, or leader election,
  specify lock identity, acquisition order, timeout, disconnect behavior, and
  fencing against a stale owner.
- Retried transactions must repeat the complete decision from fresh reads and
  must not duplicate non-transactional side effects such as messages, files, or
  external calls. Require an outbox or equivalent boundary when needed.

### Queries and indexes

- Match indexes to actual predicates, join keys, ordering, selectivity,
  cardinality, null behavior, and access patterns. Include write amplification,
  storage, vacuum, and cache cost in the decision.
- Challenge redundant, speculative, or low-selectivity indexes and indexes whose
  column order cannot serve the query. Check partial-index predicates and
  expression-index equivalence exactly.
- Examine N+1 access, unbounded result sets, offset pagination at depth,
  unstable ordering, parameter-sensitive plans, stale statistics, and queries
  that depend on implicit casts or collation behavior.
- State the performance envelope and the fallback if a chosen plan changes as
  data grows. A single favorable plan is evidence, not a permanent guarantee.

### Operations, security, and recovery

- Budget connections across every process, deployment replica, worker, admin
  tool, migration, and failover state. Account for connection storms and pool
  queues rather than setting pools independently.
- Verify vacuum and analyze expectations, transaction age, bloat, WAL volume,
  replica lag, disk alarms, long transactions, and maintenance ownership.
- Enforce least-privilege roles and separate application, migration, read-only,
  replication, and operator authority where the threat model warrants it. Review
  row-level security with the actual session identity and bypass rules.
- Require tested backups and restores with stated recovery point and recovery
  time objectives. Include encryption, retention, deletion, point-in-time
  recovery, extension availability, and the procedure for restoring dependent
  services consistently.
- Define failover behavior for clients, pools, DNS or endpoints, read routing,
  in-flight transactions, and promotion-induced data loss. A managed database
  does not remove application recovery decisions.

## Verify the claims

- Rehearse migrations and backfills against production-shaped data while
  observing locks, duration, WAL, disk, CPU, replicas, and application errors.
- Test the complete mixed-version deployment sequence and the point at which
  rollback becomes data recovery rather than code rollback.
- Exercise concurrent operations that target the same invariant. Verify expected
  conflicts and safe whole-transaction retries.
- Capture representative query plans before and after the change and validate
  response-time and resource budgets under concurrent load.
- Restore a backup into an isolated environment and verify data, roles,
  extensions, sequences, large objects, and application startup.
- Inject failed migrations, canceled index builds, replica lag, connection
  exhaustion, primary failover, and worker interruption during a backfill.

## Ask when evidence is missing

Ask only questions that can change the verdict or plan. Typical material gaps
include the supported PostgreSQL versions, deployment topology, table scale,
write rate, availability target, pool mode, migration executor, mixed-version
window, replication lag tolerance, backup objectives, and owners of non-app
writes. For a specific change, ask what locks, rewrites, transaction behavior,
backfill concurrency, retry rule, validation, rollback, and restore path apply.

Do not ask the user to repeat durable facts already present in `.grump`, the
repository, rendered configuration, migration history, or project documents. If
a claim can be proven safely by inspecting those sources, inspect first.

## Calibrate findings

- Treat plausible destructive data loss, prolonged write or availability
  blocking, broken concurrent invariants, unrecoverable mixed-version changes,
  credential exposure, or an untested recovery path for critical data as
  critical or high according to blast radius and likelihood.
- Treat missing scale evidence, weak backfill observability, avoidable query
  degradation, excessive authority, or unowned maintenance as material when it
  threatens a stated requirement.
- Downgrade or close a finding when version-specific documentation,
  production-shaped rehearsals, constraints, online migration steps, query
  plans, concurrency tests, and restore evidence support the plan.
- Do not manufacture a finding merely because a safer-sounding technique exists.
  Tie every finding to a requirement, invariant, failure mode, or unsupported
  claim.

## Add to the verdict

State the supported PostgreSQL versions and topology, changed invariants,
lock/rewrite exposure, mixed-version behavior, backfill and retry rules, index
and query evidence, connection and replication risks, recovery limits, and
remaining assumptions. Name the exact step that makes the plan irreversible and
the evidence still required before execution.
