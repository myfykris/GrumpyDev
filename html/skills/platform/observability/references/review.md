# Observability standard review

## Establish the operating model

Establish the project target: Telemetry stack and versions, signal ownership,
SLOs, sampling, retention, cardinality and cost limits, incident workflows, and
data sensitivity. The changed boundary must define: Signals, semantic
conventions, context propagation, sampling, cardinality, privacy, SLOs,
alerting, dashboards, retention, cost, and degraded telemetry.

Identify owners for instrumentation, semantic conventions, context propagation,
collectors, sampling, cardinality budgets, privacy filtering, storage,
retention, SLOs, alerts, dashboards, cost, and incident response. Prove the
critical signals survive representative load and partial telemetry failure,
that alerts correspond to user-visible objectives, and that missing telemetry
is itself visible rather than mistaken for health.

## Challenge the reviewed work

### Recurring traps

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

- Generate representative success, user-visible failure, dependency failure,
  retry, partial result and saturation paths and trace them across service and
  asynchronous boundaries.
- Exceed sampling and cardinality budgets, lose a collector or backend, delay
  ingestion, rotate credentials and exhaust retention or cost limits. Verify
  critical alerts remain accurate and telemetry failure is visible.
- Deploy old and new instrumentation and semantic conventions together, then
  verify dashboards, SLO calculations and alert runbooks remain interpretable.
- Inject representative security failures and attempted log injection. Prove
  the event is recorded without secrets, correlated to the actor and affected
  object, delivered to an owned alert when required, and usable in the runbook.

## Ask when evidence is missing

- Which user or operator decision will each signal support, and what service
  objective or failure condition triggers action?
- What cardinality, sampling, sensitive-data, retention, and correlation limits
  apply?

## Calibrate findings

- Downgrade when existing signals already support the decision with bounded cost
  and incident-tested routing.
