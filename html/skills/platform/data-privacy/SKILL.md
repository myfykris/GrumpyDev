---
name: data-privacy
description: Review data-privacy plans for purpose, minimization, consent, access, retention, deletion, export, residency, vendor flow, and incident scope. Use when a plan collects, derives, stores, shares, or deletes personal or sensitive data.
---

# Data privacy plan review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and applicable installed storage or explicitly
selected integration specialists.

## Inspect evidence

- Read the data inventory, purposes, classifications, consent and notice, access
  paths, retention, deletion, exports, subprocessors, logs, and backups.
- Trace one person's data from collection through derivation, replication,
  analytics, support access, export, deletion, backup expiry, and incident
  response.

## Establish the operating model

Establish the project target: Data classes, jurisdictions, retention rules,
residency, subject-right workflows, subprocessors, encryption, audit needs, and
responsible owners. The changed boundary must define: Data inventory, purpose
and minimization, consent, retention, deletion, export, residency,
subprocessors, logging, backups, and breach response.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Data inventory, purpose and minimization, consent,
retention, deletion, export. Prove residency, subprocessors, logging, backups,
breach response through rotation, overload, partial rollout, drain, forced stop,
rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for purpose creep, collecting fields without a defined use,
retention that excludes backups or derived data, identifiers leaking through
logs, consent used where another lawful basis actually governs, deletion that
cannot reach downstream copies, and cross-border processing left implicit.

- Require a stated purpose and owner for every sensitive field; possible future
  use is not a retention policy.
- Minimize collection and precision at the source, then prevent accidental
  copies in logs, caches, events, test fixtures, and telemetry.
- Define authorization and identity verification for access, correction, export,
  deletion, and delegated requests.
- Make retention and deletion enforceable across primary stores, indexes,
  queues, warehouses, vendors, replicas, and backups.
- Record residency, cross-border flow, vendor obligations, breach blast radius,
  and evidence without pretending this skill is legal advice.

## Verify the claims

- Verify these behaviors through the effective Data privacy configuration and
  runtime topology: Data inventory, purpose and minimization, consent,
  retention, deletion, export. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: residency, subprocessors, logging,
  backups, breach response. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which personal or sensitive data categories are collected, for what purpose,
  and under which retention and residency rules?
- How do deletion, export, consent changes, vendor transfer, and incident
  scoping work across every copy?

## Calibrate findings

- Treat unlawful collection, undeletable sensitive data, uncontrolled
  disclosure, or unknown vendor propagation as critical.
- Downgrade when the data is demonstrably non-sensitive or minimization,
  lifecycle, and access controls cover every copy.

## Add to the verdict

State data purpose and minimization, access controls, retention and deletion
coverage, external flow, incident scope, and unresolved legal review.
