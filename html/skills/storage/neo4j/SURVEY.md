# Neo4j survey contribution

## Applicability

Apply this contribution when a plan stores or queries connected data in Neo4j.
Skip it when Neo4j does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

## Inspect before asking

For Neo4j, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Neo4j version and edition, topology, graph size
  and density, schema and constraints, query patterns, drivers, security, and
  backup process.
- Review doctrine for: Graph model, labels and relationship types, constraints,
  indexes, Cypher plans, traversal growth, transactions, clustering, imports,
  and backup.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product and version, single or clustered
  topology, roles, regions, routing, consistency, memory and storage, backup,
  restore, failover, and driver behavior.

## Ask only when materially unresolved

- Which Neo4j version, edition, deployment topology, transaction model, and
  driver behavior apply?
- What graph size, degree distribution, index, constraint, query-plan, and
  cluster recovery evidence supports the design?
- Align existing domain questions with this deployment guidance when it is
  material: Product and version, single or clustered topology, roles, regions,
  routing, consistency, memory and storage, backup, restore, failover, and
  driver behavior. Do not repeat the core profile confirmation.

## Record in .grump

Record Neo4j answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing Neo4j survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable Neo4j
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Neo4j when product version or provider, topology, engine, consistency
policy, scale class, schema authority, migration tooling, replication or
failover, security, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
