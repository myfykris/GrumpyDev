# MariaDB schema, locking, and query plans

Read this reference when the reviewed work directly or indirectly changes MariaDB or
MySQL compatibility, engines,
types, JSON behavior, SQL modes, character sets, collations, indexes, query plans,
isolation, record or gap locks, deadlock retries, DDL, online algorithms, table
rebuilds, temporary space, migrations, or mixed application versions.

## Review requirements

- Verify every behavior against MariaDB rather than assuming current MySQL
  compatibility. Check syntax, data types, JSON behavior, optimizer features,
  replication, authentication, connectors, system variables, and migration
  tooling for the declared versions.

- Analyze storage-engine boundaries, transactions, foreign keys, crash recovery,
  full text, locking, and backup behavior. A server-wide transaction does not
  make nontransactional tables atomic.

- Preserve character set and collation explicitly across server, database,
  table, column, connection, client, dump, and restore. Test uniqueness and
  ordering after any collation conversion.

- For DDL, determine lock mode, algorithm, table copy or rebuild, temporary
  space, transaction-log impact, replica/Galera behavior, cancellation, and
  old/new application compatibility.

- Trace isolation, gap and record locks, deadlocks, optimistic conditions,
  retries, auto-increment behavior, and multi-writer conflicts. Re-run the whole
  decision safely after retry.

- Match indexes and query plans to production-shaped data, parameter
  distributions, predicates, ordering, and write cost. Include statistics and
  plan changes after upgrades.

## Verify the claims

- Rehearse migrations under representative scale while observing locks,
  temporary space, replication, flow control, and application errors.

- Capture query plans and load evidence before and after schema, data,
  configuration, or version changes.
