---
name: observability
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review observability engineering work for actionable telemetry, correlation, cardinality, privacy, service-level objectives, alerting, retention, and incident use."
---

# Observability GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill when telemetry is sensitive, and the installed
runtime specialist.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat missing detection for a high-impact failure or telemetry that exposes
  sensitive data or exhausts the system as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Observability evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State service objectives, diagnostic and security-event coverage, correlation
contract, log-injection controls, record protection, cost and privacy bounds,
alert quality, and incident evidence.
