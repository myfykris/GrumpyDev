# Observability survey contribution

## Applicability

Apply this contribution when a plan changes logs, metrics, traces, monitoring,
or operational diagnostics. Skip it when Observability does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Observability, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Telemetry stack and versions, signal ownership,
  SLOs, sampling, retention, cardinality and cost limits, incident workflows,
  and data sensitivity.
- Review doctrine for: Signals, semantic conventions, context propagation,
  sampling, cardinality, privacy, SLOs, alerting, dashboards, retention, cost,
  and degraded telemetry.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Collector and backend placement, network path,
  tenancy, regions, retention, sampling, cardinality limits, outage behavior,
  access, redaction, and incident ownership.

## Ask only when materially unresolved

- Which user or operator decision will each signal support, and what service
  objective or failure condition triggers action?
- What cardinality, sampling, sensitive-data, retention, and correlation limits
  apply?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Collector and backend placement, network
  path, tenancy, regions, retention, sampling, cardinality limits, outage
  behavior, access, redaction, and incident ownership? Ask only when evidence
  and the core profile confirmation do not resolve them.

## Record in .grump

Record Observability answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Observability deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Observability doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Observability when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
