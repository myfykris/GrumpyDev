---
name: observability
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review observability plans and other engineering artifacts for actionable telemetry, correlation, cardinality, privacy, service-level objectives, alerting, retention, and incident use. Project applicability: the project uses logs, metrics, traces, monitoring, alerting, or operational diagnostics."
---

# Observability GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill when telemetry is sensitive, and the installed
runtime specialist.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
