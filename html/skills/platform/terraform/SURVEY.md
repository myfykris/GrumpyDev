# Terraform and OpenTofu survey contribution

## Applies when

Apply this contribution when the project provisions or manages infrastructure through
Terraform or OpenTofu configuration.

## Inspect

- Establish the exact Terraform or OpenTofu version, provider versions, backend
  type, collaboration model, and execution environment.

## Ask when unresolved

- Which Terraform or OpenTofu version, providers, backend, locking behavior,
  and execution identities apply?

- Is the workflow shared or automated, and how are drift, destructive changes,
  state loss, and recovery handled?

- Which runtime or deployment differences are material for future reviews:
  State backend, workspaces, providers, execution identity, runner, environment
  and account boundaries, plan and apply separation, locking, imports,
  recovery, and ownership?

## Record

Map durable Terraform and OpenTofu requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
