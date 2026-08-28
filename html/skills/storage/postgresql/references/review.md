# PostgreSQL standard review

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

## Challenge the reviewed work

### Recurring traps

Watch especially for long transactions preventing vacuum progress, misunderstood
lock levels, failed concurrent indexes left invalid, serializable transactions
without retry logic, NULL and collation surprises, extension dependencies,
replicas used beyond their lag tolerance, and enum changes coupled to rollback.

## Verify the claims

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
