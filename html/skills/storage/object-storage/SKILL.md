---
name: object-storage
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review object-storage plans and other engineering artifacts for object identity, consistency, conditional operations, integrity, metadata, access control, lifecycle, multipart or resumable transfers, events, cost, and recovery. Project applicability: a system stores files, blobs, artifacts, media, or backups in provider-managed or self-hosted object storage, including Amazon S3, S3-compatible services, Google Cloud Storage, and Azure Blob Storage."
---

# Object storage GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the
`application-security` or `data-pipelines` skill.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat silent object corruption, cross-tenant access, or lifecycle deletion
  without a recovery path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Object storage evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the exact provider semantics, object identity and concurrency contract,
integrity and encoding contract, access boundary, lifecycle and event behavior,
cost risks, and recovery evidence.
