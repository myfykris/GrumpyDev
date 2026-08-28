# Project doctrine

Doctrine format: detailed

## Purpose and success

The project receives customer export requests, creates one durable export for
each accepted request, and makes the completed artifact available only to the
requesting tenant. Success means accepted work is not lost, duplicate delivery
does not create duplicate exports, and one tenant cannot read another tenant's
artifact.

## Evidence

Project purpose and runtime behavior are established by `docs/product.md`,
`docs/operations.md`, and `deploy/production.yaml`. These documents remain the
authority for details not repeated here.

## Review policies

- Plan addenda: allowed. Append each completed evaluation to the plan's
  GrumpyDev addendum without replacing earlier evaluations.
- Review interaction: interactive. Ask only material plan-scoped questions.
- Doctrine promotion: ask first. An evaluation answer becomes project doctrine
  only after the user approves promotion.
- Open research: blocks readiness when it can change a material decision.
- Research execution: GrumpyDev may perform it after confirming scope and any
  required external access.

## Deployment profiles

### DEP-001 Production worker

- Operational state: planned
- Support commitment: required
- Deployment owner: project
- Confidence: confirmed
- Evidence: `deploy/production.yaml`
- Runtime: Node.js 22 on Linux in a container
- Workload: queue consumer with graceful drain on termination
- Shared infrastructure: `INF-001`

### INF-001 Primary database

- Component: PostgreSQL 17
- Ownership: managed vendor
- Recovery: point-in-time restore with a 15-minute recovery point objective
- Evidence: `docs/operations.md`

## Project decisions

- [CON-001] Every export operation has a tenant-scoped idempotency key.
- [ACC-001] A completed export may take up to 15 minutes to appear.
- [DEC-001] Store export metadata in PostgreSQL and artifact bytes in object
  storage.

## Invariants and delivery

Tenant identity must remain attached to the request, queue message, database
row, object key, download authorization, and audit record. Deployment uses a
mixed-version window. Rollback must preserve messages and metadata written by
the newer version.

## Evidence expectations

Tests must cover duplicate delivery, worker termination, cross-tenant access,
mixed-version processing, and restore of metadata plus artifact references.

## Material unknowns

- [UNK-001] The object-storage retention period is not yet approved. This does
  not change tenant isolation but blocks final lifecycle and deletion design.
