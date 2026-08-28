---
name: terraform
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Terraform and OpenTofu plans and other engineering artifacts for state ownership, provider pinning, module boundaries, identity, drift, destructive changes, secrets, and recovery. Project applicability: the project provisions or manages infrastructure through Terraform or OpenTofu configuration."
---

# Terraform and OpenTofu GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `ci-cd`,
`secrets-configuration`, and applicable installed provider-platform skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Establish the exact Terraform or OpenTofu version, provider versions, backend
  type, collaboration model, and execution environment.

- Read provider locks, modules, state backends, imports, plans, lifecycle rules,
  identities, policies, drift reports, and recovery procedures.

Watch especially for stale plans applied after state changes, index or key
changes causing replacement, sensitive values stored in state, ignore_changes
hiding material drift, provider upgrades changing behavior, lifecycle rules
making destroy unavoidable, and imported resources lacking a safe ownership
boundary.

Lean mode is insufficient when this material severity condition may apply:

- Treat exposed state secrets, concurrent state corruption, or an unreviewed
  destructive production change as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Terraform and OpenTofu evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State dependency pinning, state boundary, module justification,
destructive-change risk, identity, drift handling, and recovery evidence.
