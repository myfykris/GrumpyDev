# Distributed evolution, operations, and recovery

Read this reference when the reviewed work directly or indirectly changes protocols,
schemas, rolling versions,
topology, region or zone placement, data migration, observability, incident response,
rollback, disaster recovery, or restoration.

## Evolution and operations

- Prove protocol, event, schema, and behavior compatibility while old and new
  versions coexist. Include rollback after some nodes or messages have adopted
  the new representation.
- Define observability by operation identity across traces, structured logs,
  metrics, queues, and durable state without leaking sensitive data. Operators
  need to distinguish slow, failed, duplicated, stuck, and reconciled work.
- Set service objectives and alerts on user-visible outcomes, saturation,
  backlog age, error budgets, replication lag, and reconciliation debt, not
  merely process health.
- Require runbooks and authority for dependency isolation, traffic shifting,
  queue pausing, replay, failover, data repair, and degraded-mode exit.
