# PostgreSQL schema, migrations, and locking

Read this reference when the reviewed work directly or indirectly changes DDL,
constraints, indexes, defaults, generated
values, types, partitions, extensions, table or index rewrites, lock acquisition,
validation scans, timeouts, WAL volume, schema migration, backfills, coexistence, expand
and contract sequencing, or irreversible data conversion.

## Schema changes and locks

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

## Data migration and coexistence

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

## Verify the claims

- Rehearse migrations and backfills against production-shaped data while
  observing locks, duration, WAL, disk, CPU, replicas, and application errors.
