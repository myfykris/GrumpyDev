# Data privacy full-review guidance

## Operating conditions

Establish the project target: Data classes, jurisdictions, retention rules,
residency, subject-right workflows, subprocessors, encryption, audit needs, and
responsible owners. The changed boundary must define: Data inventory, purpose
and minimization, consent, retention, deletion, export, residency,
subprocessors, logging, backups, and breach response.

## Failure patterns

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

## Verification to run or specify in the plan

- Trace representative personal data from collection through every primary,
  derived, cached, logged, analytical, exported, vendor and backup copy. Verify
  purpose, minimization, residency, access and retention at each location.
- Exercise access, correction, export and deletion for ordinary, delegated,
  cross-tenant, unverifiable and partially failed requests, including data that
  later returns from a queue, retry, replica or backup restore.
- Rehearse subprocessor failure and removal, retention enforcement, consent
  withdrawal and breach investigation with complete but access-controlled audit
  evidence.
