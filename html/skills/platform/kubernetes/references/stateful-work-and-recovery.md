# Kubernetes stateful work and recovery

Read this reference when the reviewed work directly or indirectly changes persistent
volumes, storage classes,
StatefulSets, operators, databases, backup, restore, snapshots, fencing, failover,
attachment, regional recovery, or stateful migration.

## Stateful work and recovery

- Define volume class, binding, topology, expansion, snapshots, reclaim policy,
  restore procedure, and replacement behavior. A PersistentVolumeClaim does not
  by itself provide backup or multi-zone recovery.
- For Jobs and CronJobs, check idempotency, deadlines, retries, concurrency
  policy, missed schedules, history, cleanup, credentials, and what completion
  means. Avoid placing one-time schema migrations in every application pod.
- For StatefulSets and operators, review identity, quorum, ordered operations,
  disruption, storage attachment, fencing, backup, restore, and version-skew
  rules from the actual system being operated.
- Define an access path for debugging and recovery that still works when the
  application, ingress, DNS, or GitOps controller is unhealthy, without granting
  standing cluster-admin authority to every operator.
