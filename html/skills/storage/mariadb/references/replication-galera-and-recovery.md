# MariaDB replication, Galera, and recovery

Read this reference when the reviewed work directly or indirectly changes replication,
Galera, quorum, flow control,
conflict handling, state transfer, failover, fencing, read routing, rejoin, backup,
point-in-time recovery, encryption, retention, restore, or server-setting recovery.

## Review requirements

- For replication or Galera, define consistency, quorum, flow control, conflict,
  state transfer, failover, fencing, lag, read routing, and rejoin behavior
  under partition.

- Require tested logical and physical backups, point-in-time capability where
  needed, encryption, retention, version compatibility, and full restore
  evidence including users and server settings.
