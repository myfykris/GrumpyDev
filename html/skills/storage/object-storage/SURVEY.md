# Object storage survey contribution

## Applicability

Apply this contribution when a system stores files, blobs, artifacts, media, or
backups in provider-managed or self-hosted object storage, including Amazon S3,
S3-compatible services, Google Cloud Storage, and Azure Blob Storage. Skip it
when object storage does not constrain a supported build, runtime, client,
data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect provider and client declarations, infrastructure policy, bucket or
container configuration, key construction, version or generation handling,
conditional operations, upload and download code, signed-access generation,
event consumers, lifecycle and retention rules, replication, inventory,
recovery runbooks, cost evidence, project documentation, and existing `.grump`
doctrine before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: provider and product, API and client versions,
  compatibility claims, account, bucket or container and region boundaries,
  namespace and key rules, object or blob types, consistency, and size limits.
- Concurrency and integrity: version, generation, metageneration, ETag, lease,
  conditional-operation, checksum, multipart, resumable, block-list, compose,
  and range-request semantics that actually apply to the selected provider.
- Security and lifecycle: identities, policies, encryption, signed URL or SAS
  behavior, retention, legal holds, versioning, delete markers, lifecycle,
  replication, events, archive retrieval, inventory, orphan cleanup, and
  recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Provider or product, region, account and bucket
  boundary, versioning, replication, access identity, endpoint, encryption,
  lifecycle, multipart behavior, archive retrieval, and recovery.

## Ask only when materially unresolved

- Which provider and product, namespace, region, object or blob type, client API,
  and exact compatibility guarantees apply?
- Which version, generation, ETag, lease, or conditional-operation rules prevent
  overwrite races, and how do multipart, resumable, block, or compose operations
  commit, abort, and recover?
- How are integrity, metadata, signed access, deletion, retention, lifecycle,
  events, replication, archive retrieval, cost, and recovery handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Provider or product, region, account and
  bucket boundary, versioning, replication, access identity, endpoint,
  encryption, lifecycle, multipart behavior, archive retrieval, and recovery?
  Ask only when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record object-storage answers in project technology, data, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Record confirmed Object storage deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep object names and payloads, current upload IDs, one-time signed URLs or SAS
tokens, credentials, transient transfer readings, temporary lifecycle dates,
and plan-only choices out of durable object-storage doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey object storage when the provider or product, API compatibility,
account or region boundary, object or blob type, namespace, consistency or
conditional-operation contract, transfer method, access model, retention,
lifecycle, event delivery, replication, archive tier, or recovery objective
materially changes. Also re-survey when evidence conflicts with saved doctrine
or the user requests a context refresh.
