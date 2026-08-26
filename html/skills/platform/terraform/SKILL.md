---
name: terraform
description: Review Terraform and OpenTofu plans for state ownership, provider pinning, module boundaries, identity, drift, destructive changes, secrets, and recovery. Use when a plan provisions or changes infrastructure through Terraform-compatible configuration.
---

# Terraform and OpenTofu plan review

Apply this guidance alongside the core GrumpyDev review and the `ci-cd`,
`secrets-configuration`, and applicable installed provider-platform skills.

## Inspect evidence

- Establish the exact Terraform or OpenTofu version, provider versions, backend
  type, collaboration model, and execution environment.
- Read provider locks, modules, state backends, imports, plans, lifecycle rules,
  identities, policies, drift reports, and recovery procedures.
- Trace initialization, plan, approval, apply interruption, replacement,
  rollback, state loss, and out-of-band change.

## Establish the operating model

Establish the project target: Terraform and provider versions, state backend and
locking, workspace or environment model, module sources, apply authority, drift
process, and recovery method. The changed boundary must define: State ownership,
providers, modules, plan and apply separation, unknown values, replacement,
imports, drift, dependencies, secrets, locking, and recovery.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for State ownership, providers, modules, plan and apply
separation, unknown values, replacement. Prove imports, drift, dependencies,
secrets, locking, recovery through rotation, overload, partial rollout, drain,
forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for stale plans applied after state changes, index or key
changes causing replacement, sensitive values stored in state, ignore_changes
hiding material drift, provider upgrades changing behavior, lifecycle rules
making destroy unavoidable, and imported resources lacking a safe ownership
boundary.

- Pin providers and modules with reviewed upgrade paths; hidden latest-version
  resolution is not reproducible infrastructure.
- Match the backend to collaboration, concurrency, sensitivity, recovery, and
  automation needs. Require secure remote state with locking for shared or
  automated infrastructure. Permit local state only for a justified isolated
  workflow with explicit access, backup, and loss recovery.
- Apply only behavior supported by the selected Terraform or OpenTofu version
  and provider versions; do not assume compatible tooling has identical
  semantics.
- Reject modules that only hide resources; require a stable ownership boundary
  and a useful contract.
- Inspect replacement, deletion, ordering, eventual consistency, import, moved
  blocks, and partial-apply recovery for every material change.
- Separate plan from apply, use short-lived least-privilege identity, detect
  drift, and require explicit approval for destructive actions.

## Verify the claims

- Verify these behaviors through the effective Terraform and OpenTofu
  configuration and runtime topology: State ownership, providers, modules, plan
  and apply separation, unknown values, replacement. Use effective rendered
  configuration and deployable artifacts in a representative identity, topology,
  capacity, and policy boundary.
- Exercise failure and edge behavior for: imports, drift, dependencies, secrets,
  locking, recovery. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which Terraform or OpenTofu version, providers, backend, locking behavior, and
  execution identities apply?
- Is the workflow shared or automated, and how are drift, destructive changes,
  state loss, and recovery handled?

## Calibrate findings

- Treat exposed state secrets, concurrent state corruption, or an unreviewed
  destructive production change as critical.
- Downgrade when an isolated local workflow is justified and protected, or
  shared remote state, locking, review, and recovery are proven.

## Add to the verdict

State dependency pinning, state boundary, module justification,
destructive-change risk, identity, drift handling, and recovery evidence.
