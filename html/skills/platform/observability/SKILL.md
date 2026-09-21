---
name: gd-observability
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review observability engineering work for actionable telemetry, correlation, cardinality, privacy, service-level objectives, alerting, retention, and incident use."
---

# Observability GrumpyDev review

## Quick checks

- Read service objectives, telemetry schemas, instrumentation, sampling,
  correlation, dashboards, alerts, retention, access controls, and incident
  examples.

- Trace one user-visible failure from symptom through alert, triage, dependency
  correlation, diagnosis, and verification of recovery.

Watch especially for unbounded label cardinality, personal data or secrets in
telemetry, sampling that hides rare failures, traces and logs that cannot
correlate, alerts with no owner or action, dashboards built only for healthy
traffic, untrusted values forging log records, security controls with no
detection path, and clock skew presented as causal ordering.

- Assess missing detection for a high-impact failure or telemetry that exposes
  sensitive data or exhausts the system under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Observability
specialist.

## Verdict context

State service objectives, diagnostic and security-event coverage, correlation
contract, log-injection controls, record protection, cost and privacy bounds,
alert quality, and incident evidence.
