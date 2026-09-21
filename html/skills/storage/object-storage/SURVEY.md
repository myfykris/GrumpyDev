# Object storage survey contribution

## Applies when

Apply this contribution when a system stores files, blobs, artifacts, media, or
backups in provider-managed or self-hosted object storage, including Amazon S3,
S3-compatible services, Google Cloud Storage, and Azure Blob Storage.

## Inspect

- Establish the exact provider and product, API and client versions, account,
  namespace and region boundaries, object or blob types, enabled features, and
  any claimed compatibility with another provider.

## Ask when unresolved

- Which provider and product, namespace, region, object or blob type, client
  API, and exact compatibility guarantees apply?

- Which version, generation, ETag, lease, or conditional-operation rules
  prevent overwrite races, and how do multipart, resumable, block, or compose
  operations commit, abort, and recover?

- How are integrity, metadata, signed access, deletion, retention, lifecycle,
  events, replication, archive retrieval, cost, and recovery handled?

- Which runtime or deployment differences materially change future reviews:
  Provider or product, region, account and bucket boundary, versioning,
  replication, access identity, endpoint, encryption, lifecycle, multipart
  behavior, archive retrieval, and recovery?

## Record

Map Object storage data guarantees to `Requirements`, accepted tradeoffs to
`Accepted decisions`, topology and recovery facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
