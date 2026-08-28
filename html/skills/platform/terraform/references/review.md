# Terraform and OpenTofu standard review

## Inspect additional evidence

- Trace initialization, plan, approval, apply interruption, replacement,
  rollback, state loss, and out-of-band change.

## Establish the operating model

Establish the project target: Terraform and provider versions, state backend and
locking, workspace or environment model, module sources, apply authority, drift
process, and recovery method. The changed boundary must define: State ownership,
providers, modules, plan and apply separation, unknown values, replacement,
imports, drift, dependencies, secrets, locking, and recovery.

Identify the state and backend owner, locking rules, provider and module sources,
workspace or environment mapping, planning and applying identities, approval
boundary, drift response, import authority, secret exposure, replacement and
deletion policy, and state-recovery owner. Prove concurrent apply is excluded
and interrupted or partial apply, provider failure and state loss have a
specific reconciliation path.

## Challenge the reviewed work

### Recurring traps

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

- Initialize from a clean environment with pinned tooling and providers, then
  inspect the saved plan for unknown values, replacements, deletions, sensitive
  output and dependencies before applying with the intended identity.
- Attempt concurrent apply, inject provider failure and interrupt apply between
  dependent resources. Re-plan to distinguish safe continuation from drift,
  import or manual repair.
- Restore state in isolation, reconcile an out-of-band change, rotate applying
  credentials and exercise the documented recovery for lock and state loss.

## Ask when evidence is missing

- Which Terraform or OpenTofu version, providers, backend, locking behavior, and
  execution identities apply?
- Is the workflow shared or automated, and how are drift, destructive changes,
  state loss, and recovery handled?

## Calibrate findings

- Downgrade when an isolated local workflow is justified and protected, or
  shared remote state, locking, review, and recovery are proven.
