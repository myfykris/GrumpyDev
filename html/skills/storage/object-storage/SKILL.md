---
name: object-storage
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review object-storage engineering work for object identity, consistency, conditional operations, integrity, metadata, access control, lifecycle, multipart or resumable transfers, events, cost, and recovery."
---

# Object storage GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
