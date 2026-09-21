# PostgreSQL full-review guidance

## Operating conditions

State the database versions and topology, including primary and replicas,
synchronous or asynchronous replication, failover authority, and whether reads
may be routed to lagging replicas. State the connection-pool mode and limits
because transaction, session, prepared-statement, temporary-object,
notification, and advisory-lock behavior can depend on them.

## Failure patterns

Watch especially for long transactions preventing vacuum progress, misunderstood
lock levels, failed concurrent indexes left invalid, serializable transactions
without retry logic, NULL and collation surprises, extension dependencies,
replicas used beyond their lag tolerance, and enum changes coupled to rollback.

## Verification to run or specify in the plan

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
