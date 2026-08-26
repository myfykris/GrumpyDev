# Data privacy survey contribution

## Applicability

Apply this contribution when a plan collects, derives, stores, shares, or
deletes personal or sensitive data. Skip it when Data privacy does not constrain
a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Data privacy, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Data classes, jurisdictions, retention rules,
  residency, subject-right workflows, subprocessors, encryption, audit needs,
  and responsible owners.
- Review doctrine for: Data inventory, purpose and minimization, consent,
  retention, deletion, export, residency, subprocessors, logging, backups, and
  breach response.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Processing and storage regions, subprocessors,
  tenant boundaries, backups, logs, analytics, retention, deletion propagation,
  access ownership, and disaster recovery copies.

## Ask only when materially unresolved

- Which personal or sensitive data categories are collected, for what purpose,
  and under which retention and residency rules?
- How do deletion, export, consent changes, vendor transfer, and incident
  scoping work across every copy?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Processing and storage regions,
  subprocessors, tenant boundaries, backups, logs, analytics, retention,
  deletion propagation, access ownership, and disaster recovery copies? Ask
  only when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Data privacy answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Data privacy deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Data
privacy doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Data privacy when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
