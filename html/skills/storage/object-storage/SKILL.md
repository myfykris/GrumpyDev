---
name: object-storage
description: Review object-storage plans for key design, consistency, integrity, metadata, access control, lifecycle, multipart operations, and recovery. Use when a system stores files, blobs, artifacts, or backups in S3-compatible object storage.
---

# Object storage plan review

Apply this guidance alongside the core GrumpyDev review and the
`application-security` or `data-pipelines` skill.

## Inspect evidence

- Establish the exact provider, API version, hosting region, enabled features,
  and claimed S3-compatibility boundary.
- Read bucket and key design, metadata, checksums, upload and download flows,
  credentials, policies, versioning, lifecycle, replication, and inventory.
- Trace partial upload, overwrite, concurrent update, deletion, retry,
  replication lag, credential expiry, and restore.

## Establish the operating model

Establish the project target: Provider and API compatibility, buckets and
regions, consistency, versioning, lifecycle and retention, encryption, access
model, size limits, and replication. The changed boundary must define: Key
design, consistency, multipart uploads, metadata, versioning, lifecycle,
retention, encryption, signed access, replication, events, and orphan cleanup.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Key design, consistency, multipart uploads, metadata,
versioning, lifecycle. Prove retention, encryption, signed access, replication,
events, orphan cleanup under concurrent access, mixed versions, failover,
interrupted migration, rollback, and restore.

## Challenge the plan

### Recurring traps

Watch especially for orphaned multipart uploads, overwrites without a version or
recovery policy, unsafe key normalization, metadata and media types trusted as
validation, presigned access broader or longer than intended, retention blocking
deletion, and archive tiers treated as immediately readable.

- Define object identity and overwrite semantics; listing and filenames are not
  a transactional metadata database.
- Apply only guarantees documented for the selected provider; S3-compatible
  services are not interchangeable by default.
- Require content length, media type, checksum, encryption, and encoding to be
  explicit at each producer and consumer boundary.
- Check multipart cleanup, idempotent retries, presigned URL scope and expiry,
  range requests, and untrusted content handling.
- Enforce least privilege, public-access blocking, tenant isolation, audit logs,
  retention, legal holds, and deletion verification.
- Model request, transfer, replication, and retrieval cost, then test version
  recovery and region-loss procedures.

## Verify the claims

- Verify these behaviors through the declared Object storage topology and
  workload: Key design, consistency, multipart uploads, metadata, versioning,
  lifecycle. Use production-shaped scale and workload while observing latency,
  resource use, locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: retention, encryption, signed access,
  replication, events, orphan cleanup. Exercise concurrent writers, retries,
  duplicate operations, failover, interrupted migration, and mixed application
  versions where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which object-store provider and exact compatibility guarantees apply to
  versioning, conditional writes, metadata, and listing?
- How are partial uploads, overwrite races, deletion, lifecycle, replication,
  encoding, and recovery handled?

## Calibrate findings

- Treat silent object corruption, cross-tenant access, or lifecycle deletion
  without a recovery path as critical.
- Downgrade when objects are reproducible or versioning, boundary metadata,
  access controls, and restore are demonstrated.

## Add to the verdict

State object identity, integrity and encoding contract, access boundary,
lifecycle behavior, cost risks, and recovery evidence.
