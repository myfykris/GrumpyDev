# Elasticsearch and OpenSearch full-review guidance

## Operating conditions

Establish the project target: Product and version, cluster topology, shard
policy, mappings and analyzers, index lifecycle, ingestion rate, query SLAs,
security, and snapshot process. The changed boundary must define: Mappings,
analyzers, shards, segments, refresh, indexing, queries, relevance, aliases,
reindexing, snapshots, cluster state, and version compatibility.

## Failure patterns

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

## Verification to run or specify in the plan

- Index representative documents and check expected matches and ranking for
  the chosen analyzers and mappings. Measure expensive aggregations,
  pagination, and bulk ingestion with the actual shard layout.
- Reindex while writes continue, switch aliases, and interrupt a node or
  ingestion worker. Check missing or duplicate documents, partial search
  failures, and recovery from a snapshot on the supported product version.
