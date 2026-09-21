---
name: gd-terraform
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Terraform and OpenTofu engineering work for state ownership, provider pinning, module boundaries, identity, drift, destructive changes, secrets, and recovery."
---

# Terraform and OpenTofu GrumpyDev review

## Quick checks

- Establish the exact Terraform or OpenTofu version, provider versions, backend
  type, collaboration model, and execution environment.

- Read provider locks, modules, state backends, imports, plans, lifecycle rules,
  identities, policies, drift reports, and recovery procedures.

Watch especially for stale plans applied after state changes, index or key
changes causing replacement, sensitive values stored in state, ignore_changes
hiding material drift, provider upgrades changing behavior, lifecycle rules
making destroy unavoidable, and imported resources lacking a safe ownership
boundary.

- Assess exposed state secrets, concurrent state corruption, or an unreviewed
  destructive production change under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Terraform and
OpenTofu specialist.

## Verdict context

State dependency pinning, state boundary, module justification,
destructive-change risk, identity, drift handling, and recovery evidence.
