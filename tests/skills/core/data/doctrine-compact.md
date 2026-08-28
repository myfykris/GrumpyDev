# Project doctrine

Doctrine format: compact

## Purpose

Create one durable customer export per accepted request; prevent duplicate
exports and cross-tenant artifact access. Evidence: `docs/product.md`,
`docs/operations.md`, `deploy/production.yaml`.

## Policies

- Plan addenda: allowed
- Review interaction: interactive
- Doctrine promotion: ask first
- Open research: blocks readiness when it can change a material decision
- Research execution: GrumpyDev may perform it after confirming scope and any
  required external access

## Profiles

- `DEP-001` Production worker: planned; required support; project-owned;
  confirmed by `deploy/production.yaml`; Node.js 22 on Linux in a container;
  queue consumer; graceful termination drain; uses `INF-001`.
- `INF-001` Primary database: PostgreSQL 17; managed vendor; point-in-time
  restore; 15-minute recovery point objective; evidence `docs/operations.md`.

## Decisions

- [CON-001] Tenant-scoped idempotency key for every export operation.
- [ACC-001] Completed export may take up to 15 minutes to appear.
- [DEC-001] Metadata in PostgreSQL; artifact bytes in object storage.

## Invariants and delivery

Tenant identity spans request, queue message, database row, object key,
download authorization, and audit record. Mixed-version deployment; rollback
preserves newer-version messages and metadata.

## Evidence expectations

Test duplicate delivery, worker termination, cross-tenant access, mixed-version
processing, and metadata plus artifact-reference restore.

## Unknowns

- [UNK-001] Object-storage retention is unapproved; tenant isolation is
  unaffected, but lifecycle and deletion design remain blocked.
