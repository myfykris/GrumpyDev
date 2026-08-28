# CI/CD survey contribution

## Applicability

Apply this contribution when the project uses automation to build, test, release,
promote, or deploy software.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For CI/CD, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: CI/CD platform, runner trust and OS, branch and
  approval policy, artifact flow, environments, credential model, deployment
  ownership, and retention.
- Review doctrine for: Trigger and trust boundaries, reproducibility, artifacts,
  credentials, environments, approvals, concurrency, caching, provenance,
  rollback, and failure recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Runner location and trust, identities,
  environments, artifact flow, caches, approvals, concurrency, secret
  boundaries, deployment method, rollback, and ownership.

## Ask only when materially unresolved

- Which triggers can run untrusted changes, and which credentials or protected
  environments can those runs reach?
- Is one verified artifact promoted across environments, and what restores
  service after a failed release?
- Align existing domain questions with this deployment guidance when it is
  material: Runner location and trust, identities, environments, artifact flow,
  caches, approvals, concurrency, secret boundaries, deployment method,
  rollback, and ownership. Do not repeat the core profile confirmation.

## Record in .grump

Record CI/CD answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing CI/CD survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable CI/CD
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey CI/CD when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
