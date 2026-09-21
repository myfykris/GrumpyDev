# Observability survey contribution

## Applies when

Apply this contribution when the project uses logs, metrics, traces, monitoring,
alerting, or operational diagnostics.

## Inspect

- Read service objectives, telemetry schemas, instrumentation, sampling,
  correlation, dashboards, alerts, retention, access controls, and incident
  examples.

## Ask when unresolved

- Which user or operator decision will each signal support, and what service
  objective or failure condition triggers action?

- What cardinality, sampling, sensitive-data, retention, and correlation limits
  apply?

- Which runtime or deployment differences materially change future reviews:
  Collector and backend placement, network path, tenancy, regions, retention,
  sampling, cardinality limits, outage behavior, access, redaction, and
  incident ownership?

## Record

Map durable Observability requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
