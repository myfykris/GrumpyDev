# Secrets and configuration survey contribution

## Applicability

Apply this contribution when a plan changes runtime configuration, credentials,
keys, certificates, or feature controls. Skip it when Secrets and configuration
does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

For Secrets and configuration, inspect version declarations, effective
configuration sources, rendered artifacts, infrastructure and identity policy,
build and deployment workflows, service objectives, operational runbooks, and
project documentation. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Configuration systems, secret stores, environment
  hierarchy, identity and access, rotation cadence, reload behavior, audit
  requirements, and ownership.
- Review doctrine for: Source and precedence, validation, secret lifecycle,
  rotation, reload, redaction, least privilege, environment drift, emergency
  access, and failure modes.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Secret and configuration sources, injection path,
  process scope, identity, rotation, reload, environment differences,
  redaction, fallback behavior, and owner.

## Ask only when materially unresolved

- Who owns each configuration value or secret, where is it sourced, and how is
  it validated before use?
- How do rotation, revocation, version skew, startup failure, and accidental
  exposure behave?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Secret and configuration sources,
  injection path, process scope, identity, rotation, reload, environment
  differences, redaction, fallback behavior, and owner? Ask only when evidence
  and the core profile confirmation do not resolve them.

## Record in .grump

Record Secrets and configuration answers in project technology, runtime,
security, deployment, verification, and operational doctrine. Preserve source
and scope. Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Secrets and configuration deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Secrets
and configuration doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Secrets and configuration when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
