# PostgreSQL survey contribution

## Applicability

Apply this contribution when PostgreSQL stores project data, supports tests or analytics
that constrain implementation, or is a deployment dependency. Combine it with SQL, the
application framework, the migration tool, backup, infrastructure, and managed-service
contributions. Deduplicate facts about versions, topology, deployment, and data
classification.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect connection and migration configuration, dependency locks, container or
infrastructure definitions, schema dumps, extension declarations, pooler
configuration, runbooks, CI services, and project documentation. Distinguish
committed defaults from environment-specific production facts. Do not connect to
or mutate a database merely to answer setup questions unless the user has
authorized that action.

## Durable project facts

Collect only facts expected to guide many future reviews:

- Supported PostgreSQL major versions and who controls upgrades.
- Self-managed or managed service, primary/replica topology, region model, read
  routing, failover authority, and permitted extensions.
- Migration framework, schema authority, migration execution owner, and whether
  old and new application versions normally overlap.
- Approximate important-table scale and growth class, uptime expectations, and
  whether routine changes must avoid blocking writes.
- Connection poolers, pool mode, total connection limits, and which workloads
  use separate pools or credentials.
- Default transaction/isolation policy and established concurrency patterns,
  such as optimistic versions, row locks, advisory locks, or an outbox.
- Backup retention, point-in-time recovery, recovery point and time objectives,
  restore-test owner, and any data-residency constraints.
- Replication-lag expectations and whether user-visible reads may come from
  replicas.
- Role boundaries for applications, migrations, operators, reporting, and
  replication, plus use of row-level security where material.
- Operational owners for vacuum health, transaction age, bloat, capacity,
  replication, backup, and incident response.
- Deployment-profile guidance: product and version, extensions,
  managed or self-hosted topology, replicas, pooling, storage, vacuum,
  migration, backup, restore, failover, and lag coverage.

## Ask only when materially unresolved

Ask about a fact only when it cannot be established from evidence and would
change future PostgreSQL reviews. Useful unresolved questions include which
server versions production must support, whether a pooler uses transaction
pooling, whether deployments overlap versions, what scale and uptime class
governs migrations, who performs restore tests, and whether replica reads may be
stale. Let the combined survey assign final sequential question numbers.

Do not turn setup into a schema-design interview. A plan-specific table size,
lock risk, query shape, backfill, or rollback question belongs to the live
evaluation unless it expresses a durable project-wide rule.
- Align existing domain questions with this deployment guidance when it is
  material: product and version, extensions, managed or self-hosted
  topology, replicas, pooling, storage, vacuum, migration, backup, restore,
  failover, and lag coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record confirmed facts under project technology, data, runtime, deployment,
security, verification, and operational conventions as appropriate. Include the
evidence source or an explicit user decision when useful. Record unknowns that
materially limit reviews as unresolved doctrine, not as guessed defaults. Mark
this contribution current in specialist survey status only after its material
durable questions are answered, deliberately deferred, or documented as unknown.

Map existing PostgreSQL survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Do not record passwords, connection strings containing secrets, private keys,
tokens, personal production data, full database dumps, transient hostnames,
current connection counts, one-off migration details, or a raw Q&A transcript.
Do not assume managed service means tested recovery, or that an ORM defines the
real schema. Do not ask for facts already established by project evidence or a
companion survey.

## Re-survey triggers

Re-survey after a PostgreSQL major-version or provider change, topology or
region redesign, pooler-mode change, migration-framework change, deployment
overlap change, extension-policy change, major scale-class shift, new replica
read policy, security or row-level-policy redesign, or backup and recovery
objective change.
