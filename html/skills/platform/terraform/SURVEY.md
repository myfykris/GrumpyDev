# Terraform and OpenTofu survey contribution

## Applicability

Apply this contribution when a plan provisions or changes infrastructure through
Terraform-compatible configuration. Skip it when Terraform and OpenTofu does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Terraform and OpenTofu, inspect version declarations, effective
configuration sources, rendered artifacts, infrastructure and identity policy,
build and deployment workflows, service objectives, operational runbooks, and
project documentation. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Terraform and provider versions, state backend and
  locking, workspace or environment model, module sources, apply authority,
  drift process, and recovery method.
- Review doctrine for: State ownership, providers, modules, plan and apply
  separation, unknown values, replacement, imports, drift, dependencies,
  secrets, locking, and recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: State backend, workspaces, providers, execution
  identity, runner, environment and account boundaries, plan and apply
  separation, locking, imports, recovery, and ownership.

## Ask only when materially unresolved

- Which Terraform or OpenTofu version, providers, backend, locking behavior, and
  execution identities apply?
- Is the workflow shared or automated, and how are drift, destructive changes,
  state loss, and recovery handled?
- Align existing domain questions with this deployment guidance when it is
  material: State backend, workspaces, providers, execution identity, runner,
  environment and account boundaries, plan and apply separation, locking,
  imports, recovery, and ownership. Do not repeat the core profile
  confirmation.

## Record in .grump

Record Terraform and OpenTofu answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Terraform and OpenTofu survey answers to the affected `DEP-###`
profile. Reference a shared `INF-###` component rather than copying its common
contract. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Terraform and OpenTofu doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey Terraform and OpenTofu when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
