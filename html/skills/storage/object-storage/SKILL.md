---
name: gd-object-storage
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review object-storage engineering work for object identity, consistency, conditional operations, integrity, metadata, access control, lifecycle, multipart or resumable transfers, events, cost, and recovery."
---

# Object storage GrumpyDev review

## Quick checks

- Establish the exact provider and product, API and client versions, account,
  namespace and region boundaries, object or blob types, enabled features, and
  any claimed compatibility with another provider.

- Read container, bucket, and key design; version, generation, or ETag use;
  conditional requests; metadata and integrity fields; transfer flows;
  credentials and signed access; retention and lifecycle; events; replication;
  archive tiers; recovery; and inventory.

Watch especially for provider semantics assumed portable, ETags treated as
universal content checksums, writes without generation or version preconditions,
orphaned multipart or uncommitted block uploads, unsafe key normalization,
metadata and media types trusted as validation, signed access broader or longer
than intended, retention blocking deletion, event delivery treated as exactly
once, and archive tiers treated as immediately readable.

- Assess silent object corruption, cross-tenant access, or lifecycle deletion
  without a recovery path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Object storage
specialist.

## Verdict context

State the exact provider semantics, object identity and concurrency contract,
integrity and encoding contract, access boundary, lifecycle and event behavior,
cost risks, and recovery evidence.
