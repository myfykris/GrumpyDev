# Object storage survey contribution

## Applicability

Apply this contribution when a system stores files, blobs, artifacts, or backups
in S3-compatible object storage. Skip it when Object storage does not constrain
a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Object storage, inspect product and client declarations, migration
configuration, schema sources, indexes or key definitions, topology and
infrastructure files, backup and restore runbooks, capacity evidence, and
operational ownership. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Provider and API compatibility, buckets and
  regions, consistency, versioning, lifecycle and retention, encryption, access
  model, size limits, and replication.
- Review doctrine for: Key design, consistency, multipart uploads, metadata,
  versioning, lifecycle, retention, encryption, signed access, replication,
  events, and orphan cleanup.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Provider or product, region, account and bucket
  boundary, versioning, replication, access identity, endpoint, encryption,
  lifecycle, multipart behavior, archive retrieval, and recovery.

## Ask only when materially unresolved

- Which object-store provider and exact compatibility guarantees apply to
  versioning, conditional writes, metadata, and listing?
- How are partial uploads, overwrite races, deletion, lifecycle, replication,
  encoding, and recovery handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Provider or product, region, account and
  bucket boundary, versioning, replication, access identity, endpoint,
  encryption, lifecycle, multipart behavior, archive retrieval, and recovery?
  Ask only when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Object storage answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Record confirmed Object storage deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable Object
storage doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Object storage when product version or provider, topology, engine,
consistency policy, scale class, schema authority, migration tooling,
replication or failover, security, or recovery objectives materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
