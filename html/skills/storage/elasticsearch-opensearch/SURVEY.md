# Elasticsearch and OpenSearch survey contribution

## Applicability

Apply this contribution when the project implements search, analytics, or log storage
with Elasticsearch or OpenSearch.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

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

Keep one-off query profiles, current node identities, hot-thread and shard
allocation snapshots, temporary reindex task IDs, and copied documents out of
durable Elasticsearch and OpenSearch doctrine. Do not duplicate facts owned by
another applicable contribution.

## Re-survey triggers

Re-survey Elasticsearch and OpenSearch when the product, version or provider,
cluster topology, mappings or analyzers, shard and replica strategy, refresh and
indexing model, index lifecycle, search or vector workload, security boundary,
snapshot policy, or migration approach materially changes. Also re-survey when
evidence conflicts with saved doctrine or the user requests a context refresh.
