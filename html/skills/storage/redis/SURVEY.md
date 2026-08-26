# Redis survey contribution

## Applicability

Apply this contribution when redis holds cache, coordination, queue, session, or
primary application state. Skip it when Redis does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Redis, inspect product and client declarations, migration configuration,
schema sources, indexes or key definitions, topology and infrastructure files,
backup and restore runbooks, capacity evidence, and operational ownership. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Redis product and version, topology, persistence,
  eviction, memory limits, key ownership, cluster mode, failover, TLS and
  authentication, and workload role.
- Review doctrine for: Data structures, atomicity, Lua or functions, expiration,
  eviction, persistence, replication, cluster slots, failover, hot keys,
  caching, locks, and queues.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Product and version, cache or authority role,
  topology, cluster or sentinel, memory and eviction, persistence, replicas,
  failover, TLS and identity, backup, and reconstruction.

## Ask only when materially unresolved

- Which Redis-compatible product, exact version, deployment mode, persistence,
  eviction, and failover behavior apply?
- Is the data disposable cache, coordination state, queue state, session state,
  or primary data, and how is loss recovered?
- Align existing domain questions with this deployment guidance when it is
  material: Product and version, cache or authority role, topology, cluster or
  sentinel, memory and eviction, persistence, replicas, failover, TLS and
  identity, backup, and reconstruction. Do not repeat the core profile
  confirmation.

## Record in .grump

Record Redis answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing Redis survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable Redis
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Redis when product version or provider, topology, engine, consistency
policy, scale class, schema authority, migration tooling, replication or
failover, security, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
