# Object storage standard review

## Inspect additional evidence

- Trace partial upload, overwrite, concurrent update, deletion, retry,
  replication lag, event delivery, credential expiry, archive retrieval, and
  restore using the selected provider's actual API.

## Establish the operating model

Establish the exact provider and product, account, bucket or container and
region boundaries, object or blob types, key rules, API and client versions,
consistency and listing guarantees, conditional-operation semantics, version or
generation identity, integrity fields, transfer protocols, signed-access model,
retention, lifecycle, events, replication, archive behavior, cost ownership,
and recovery authority. Verify compatibility claims feature by feature rather
than accepting an `S3-compatible` label as a contract.

## Challenge the reviewed work

### Recurring traps

- Define object identity and overwrite semantics; listing and filenames are not
  a transactional metadata database.
- Apply only guarantees documented for the selected provider; S3-compatible
  services are not interchangeable by default.
- For Amazon S3 and compatible APIs, do not treat ETag as a universal content
  checksum. Verify conditional write behavior, version IDs and delete markers,
  multipart completion, and how the client handles precondition and conflict
  responses. Test compatibility services against every feature the design uses.
- For Google Cloud Storage, use generation and metageneration preconditions for
  read-modify-write behavior. Account for strong object and listing consistency
  separately from IAM propagation, cache behavior, resumable uploads, and
  composed objects.
- For Azure Blob Storage, distinguish block, page, and append blobs. Define ETag
  conditions, leases, uncommitted block cleanup and commit order, SAS or Entra
  authorization, access tiers, and the limited cases where concurrent writes
  have supported semantics.
- Require content length, media type, checksum, encryption, and encoding to be
  explicit at each producer and consumer boundary.
- Check multipart cleanup, idempotent retries, presigned URL scope and expiry,
  resumable or block-upload recovery, range requests, event deduplication, and
  untrusted content handling.
- Enforce least privilege, public-access blocking, tenant isolation, audit logs,
  retention, legal holds, and deletion verification.
- Model request, transfer, replication, and retrieval cost, then test version
  recovery and region-loss procedures.

## Verify the claims

- Exercise concurrent creation and overwrite with the provider's actual
  generation, version, ETag, lease, or conditional headers. Verify what the
  client does on precondition failures, conflicts, retries, and ambiguous
  network results.
- Interrupt multipart, resumable, compose, and block uploads before and during
  commit; verify retry identity, cleanup, visibility, metadata, and integrity.
- Test signed URL or SAS scope and expiry, credential rotation, private and
  public access, event duplication and reordering, lifecycle transition,
  retention and legal holds, replication lag, deletion, and archive retrieval.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which provider and product, namespace, region, object or blob type, client API,
  and exact compatibility guarantees apply?
- Which version, generation, ETag, lease, or conditional-operation rules prevent
  overwrite races, and how do transfers commit, abort, and recover?
- How are integrity, signed access, deletion, lifecycle, events, replication,
  archive retrieval, cost, and recovery handled?

## Calibrate findings

- Downgrade when objects are reproducible or versioning, boundary metadata,
  access controls, and restore are demonstrated.
