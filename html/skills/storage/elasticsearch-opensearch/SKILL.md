---
name: elasticsearch-opensearch
description: Review Elasticsearch and OpenSearch plans for mappings, analyzers, shards, queries, ingestion, cluster capacity, security, and recovery. Use when a plan implements search, analytics, or logs on Elasticsearch or OpenSearch.
---

# Elasticsearch and OpenSearch plan review

Apply this guidance alongside the core GrumpyDev review and the `data-pipelines`
or `observability` skill.

## Inspect evidence

- Establish the exact Elasticsearch or OpenSearch product, version,
  distribution, plugins, hosting mode, and compatibility boundary.
- Read index templates, mappings, analyzers, queries, ingest pipelines, shard
  topology, lifecycle policies, security, snapshots, and benchmarks.
- Trace document creation, update, refresh, search, reindex, rollover, node
  loss, and snapshot restore.

## Establish the operating model

Establish the project target: Product and version, cluster topology, shard
policy, mappings and analyzers, index lifecycle, ingestion rate, query SLAs,
security, and snapshot process. The changed boundary must define: Mappings,
analyzers, shards, segments, refresh, indexing, queries, relevance, aliases,
reindexing, snapshots, cluster state, and version compatibility.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Mappings, analyzers, shards, segments, refresh, indexing,
queries. Prove relevance, aliases, reindexing, snapshots, cluster state, version
compatibility under concurrent access, mixed versions, failover, interrupted
migration, rollback, and restore.

## Challenge the plan

### Recurring traps

Watch especially for dynamic mappings causing field explosion, analyzed and
exact fields confused, deep pagination, shard counts chosen by habit, refresh
and merge cost ignored, aliases switched before reindex verification, partial
search results accepted silently, and snapshots mistaken for
application-consistent backups.

- Define relevance and correctness tests; plausible search results are not proof
  that analysis and scoring work.
- Apply only guarantees documented for the selected product and version;
  Elasticsearch and OpenSearch behavior can diverge.
- Prevent dynamic mapping explosions, accidental text versus keyword fields,
  incompatible analyzers, and unbounded nested documents.
- Size shard count and shard size for growth, recovery, heap, merge load, and
  cluster-state overhead instead of using fixed folklore.
- Check deep pagination, aggregations, wildcard or script queries, refresh
  intervals, bulk sizing, and backpressure under representative data.
- Treat reindexing, mapping evolution, lifecycle deletion, access control,
  snapshots, and restore drills as required operations.

## Verify the claims

- Verify these behaviors through the declared Elasticsearch and OpenSearch
  topology and workload: Mappings, analyzers, shards, segments, refresh,
  indexing, queries. Use production-shaped scale and workload while observing
  latency, resource use, locks or conflicts, replication, and application
  errors.
- Exercise failure and edge behavior for: relevance, aliases, reindexing,
  snapshots, cluster state, version compatibility. Exercise concurrent writers,
  retries, duplicate operations, failover, interrupted migration, and mixed
  application versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which Elasticsearch or OpenSearch product, exact version, deployment mode,
  plugins, and compatibility promises apply?
- How are mappings, aliases, refresh behavior, reindexing, shard size, and
  failed-node recovery handled?

## Calibrate findings

- Treat irreversible mapping conflict, cluster instability, or search
  authorization leakage as critical.
- Downgrade when product-specific behavior, bounded shard sizing, alias rollout,
  and rebuild paths are proven.

## Add to the verdict

State mapping and relevance evidence, shard model, expensive-query controls,
ingestion bounds, and recovery proof.
