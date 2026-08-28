# DynamoDB survey contribution

## Applicability

Apply this contribution when the project stores or queries application data in Amazon
DynamoDB.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For DynamoDB, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Regions and table topology, capacity mode,
  consistency needs, key conventions, indexes, global tables, TTL, streams,
  backup, and workload limits.
- Review doctrine for: Keys and access patterns, indexes, capacity, partitions,
  consistency, transactions, condition expressions, streams, TTL, global tables,
  retries, and hot keys.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Region and account, table and index design,
  capacity mode, partitions, global tables, consistency, streams, TTL, backup,
  restore, IAM, endpoints, and limits.

## Ask only when materially unresolved

- Which access patterns, key distributions, consistency needs, table mode,
  regions, and transaction boundaries apply?
- How are conditional writes, hot keys, retries, streams, indexes, and item
  growth bounded?
- Align existing domain questions with this deployment guidance when it is
  material: Region and account, table and index design, capacity mode,
  partitions, global tables, consistency, streams, TTL, backup, restore, IAM,
  endpoints, and limits. Do not repeat the core profile confirmation.

## Record in .grump

Record DynamoDB answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing DynamoDB survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep item contents, current consumed-capacity readings, temporary provisioned
capacity, backfill execution IDs, stream sequence numbers, and copied production
data out of durable DynamoDB doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey DynamoDB when a table, partition or sort key, secondary index, access
pattern, capacity mode, consistency requirement, global-table region, stream or
DAX use, item size strategy, encryption or identity boundary, point-in-time
recovery, or restore objective materially changes. Also re-survey when evidence
conflicts with saved doctrine or the user requests a context refresh.
