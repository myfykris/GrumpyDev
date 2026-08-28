# PostgreSQL operations, replication, and recovery

Read this reference when the reviewed work directly or indirectly changes connection
pools, pool modes, maintenance,
vacuum, bloat, WAL, roles, row-level security, replicas, lag, read routing, failover,
backup, retention, point-in-time recovery, restore, recovery objectives, or operator
ownership.

## Operations, security, and recovery

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
