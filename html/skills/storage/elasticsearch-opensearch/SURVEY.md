# Elasticsearch and OpenSearch survey contribution

## Applicability

Apply this contribution when a plan implements search, analytics, or logs on
Elasticsearch or OpenSearch. Skip it when Elasticsearch and OpenSearch does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Elasticsearch and OpenSearch, inspect product and client declarations,
migration configuration, schema sources, indexes or key definitions, topology
and infrastructure files, backup and restore runbooks, capacity evidence, and
operational ownership. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Product and version, cluster topology, shard
  policy, mappings and analyzers, index lifecycle, ingestion rate, query SLAs,
  security, and snapshot process.
- Review doctrine for: Mappings, analyzers, shards, segments, refresh, indexing,
  queries, relevance, aliases, reindexing, snapshots, cluster state, and version
  compatibility.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product and version, managed or self-hosted
  mode, nodes, roles, shards, replicas, zones, storage, snapshots, reindex
  capacity, security, and failover.

## Ask only when materially unresolved

- Which Elasticsearch or OpenSearch product, exact version, deployment mode,
  plugins, and compatibility promises apply?
- How are mappings, aliases, refresh behavior, reindexing, shard size, and
  failed-node recovery handled?
- Align existing domain questions with this deployment guidance when it is
  material: Product and version, managed or self-hosted mode, nodes, roles,
  shards, replicas, zones, storage, snapshots, reindex capacity, security, and
  failover. Do not repeat the core profile confirmation.

## Record in .grump

Record Elasticsearch and OpenSearch answers in project technology, data, schema,
consistency, deployment, and recovery doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Elasticsearch and OpenSearch survey answers to the affected
`DEP-###` profile. Reference a shared `INF-###` component rather than copying
its common contract. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable
Elasticsearch and OpenSearch doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey Elasticsearch and OpenSearch when product version or provider,
topology, engine, consistency policy, scale class, schema authority, migration
tooling, replication or failover, security, or recovery objectives materially
change, when evidence conflicts with saved doctrine, or when the user requests a
context refresh.
