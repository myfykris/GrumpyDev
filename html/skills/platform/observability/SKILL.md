---
name: observability
description: Review observability plans for actionable telemetry, correlation, cardinality, privacy, service-level objectives, alerting, retention, and incident use. Use when a plan changes logs, metrics, traces, monitoring, or operational diagnostics.
---

# Observability plan review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill when telemetry is sensitive, and the installed
runtime specialist.

## Inspect evidence

- Read service objectives, telemetry schemas, instrumentation, sampling,
  correlation, dashboards, alerts, retention, access controls, and incident
  examples.
- Trace one user-visible failure from symptom through alert, triage, dependency
  correlation, diagnosis, and verification of recovery.

## Establish the operating model

Establish the project target: Telemetry stack and versions, signal ownership,
SLOs, sampling, retention, cardinality and cost limits, incident workflows, and
data sensitivity. The changed boundary must define: Signals, semantic
conventions, context propagation, sampling, cardinality, privacy, SLOs,
alerting, dashboards, retention, cost, and degraded telemetry.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Signals, semantic conventions, context propagation,
sampling, cardinality, privacy. Prove SLOs, alerting, dashboards, retention,
cost, degraded telemetry through rotation, overload, partial rollout, drain,
forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for unbounded label cardinality, personal data or secrets in
telemetry, sampling that hides rare failures, traces and logs that cannot
correlate, alerts with no owner or action, dashboards built only for healthy
traffic, untrusted values forging log records, security controls with no
detection path, and clock skew presented as causal ordering.

- Start from decisions operators must make; collecting everything is expensive
  noise, not observability.
- Require stable event and metric names, units, labels, trace propagation, clock
  handling, and deployment version context.
- Bound label cardinality, log volume, trace sampling, storage cost, and
  telemetry behavior during an outage.
- Exclude secrets and unnecessary personal data, define redaction at the source,
  and restrict operational access.
- Encode untrusted values as data in structured records so control characters,
  delimiters, markup, and forged fields cannot create false events or executable
  dashboards. Bound event size and cardinality before telemetry leaves the app.
- Define and alert on security-relevant outcomes such as repeated authentication
  failure, authorization denial, account recovery, privilege or role change,
  admin action, secret access, configuration change, webhook rejection,
  suspicious business-flow automation, and security-control failure.
- Protect audit records and alert routes from unauthorized read, modification,
  deletion, and silent disablement. Define retention, clock, correlation,
  identity, tenant, and evidence-access rules for investigations.
- Tie alerts to user impact or exhausted error budgets, then test that runbooks
  and telemetry diagnose real injected failures.

## Verify the claims

- Verify these behaviors through the effective Observability configuration and
  runtime topology: Signals, semantic conventions, context propagation,
  sampling, cardinality, privacy. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: SLOs, alerting, dashboards, retention,
  cost, degraded telemetry. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Inject representative security failures and attempted log injection. Prove
  the event is recorded without secrets, correlated to the actor and affected
  object, delivered to an owned alert when required, and usable in the runbook.

## Ask when evidence is missing

- Which user or operator decision will each signal support, and what service
  objective or failure condition triggers action?
- What cardinality, sampling, sensitive-data, retention, and correlation limits
  apply?

## Calibrate findings

- Treat missing detection for a high-impact failure or telemetry that exposes
  sensitive data or exhausts the system as critical.
- Downgrade when existing signals already support the decision with bounded cost
  and incident-tested routing.

## Add to the verdict

State service objectives, diagnostic and security-event coverage, correlation
contract, log-injection controls, record protection, cost and privacy bounds,
alert quality, and incident evidence.
