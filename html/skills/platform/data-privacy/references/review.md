# Data privacy standard review

## Establish the operating model

Establish the project target: Data classes, jurisdictions, retention rules,
residency, subject-right workflows, subprocessors, encryption, audit needs, and
responsible owners. The changed boundary must define: Data inventory, purpose
and minimization, consent, retention, deletion, export, residency,
subprocessors, logging, backups, and breach response.

For each personal-data class, identify its purpose, lawful or user-granted
basis, owner, source, recipients, residency, copies, retention clock, deletion
authority, export path, subprocessors, backup behavior, and breach-response
owner. Prove subject requests and retention rules reach derived stores, logs,
indexes, queues, analytics, vendors, and restored backups without creating new
unauthorized copies.

## Challenge the reviewed work

### Recurring traps

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

- Trace representative personal data from collection through every primary,
  derived, cached, logged, analytical, exported, vendor and backup copy. Verify
  purpose, minimization, residency, access and retention at each location.
- Exercise access, correction, export and deletion for ordinary, delegated,
  cross-tenant, unverifiable and partially failed requests, including data that
  later returns from a queue, retry, replica or backup restore.
- Rehearse subprocessor failure and removal, retention enforcement, consent
  withdrawal and breach investigation with complete but access-controlled audit
  evidence.

## Ask when evidence is missing

- Which personal or sensitive data categories are collected, for what purpose,
  and under which retention and residency rules?
- How do deletion, export, consent changes, vendor transfer, and incident
  scoping work across every copy?

## Calibrate findings

- Downgrade when the data is demonstrably non-sensitive or minimization,
  lifecycle, and access controls cover every copy.
