# GraphQL API design survey contribution

## Applicability

Apply this contribution when the project exposes, consumes, or operates GraphQL schemas,
resolvers, clients, or gateways.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For GraphQL API design, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: GraphQL implementation and version, schema
  ownership, clients, authentication, federation, query limits, persisted
  operations, subscriptions, and deprecation policy.
- Review doctrine for: Schema ownership, nullability, evolution, resolvers,
  field and object authorization, mutation properties, batching, query cost,
  pagination, errors, subscriptions, cache scope, production exposure, and
  persisted operations.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Gateway and service topology, resolver placement,
  batching scope, cache, subscription transport, proxy limits, authorization
  boundary, scaling, and persisted-operation deployment.

## Ask only when materially unresolved

- Where is authorization enforced for each changed field, object, and resolver
  path?
- What query depth, breadth, alias, batching, subscription, result, and
  downstream-cost limits apply to untrusted clients?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Gateway and service topology, resolver
  placement, batching scope, cache, subscription transport, proxy limits,
  authorization boundary, scaling, and persisted-operation deployment? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record GraphQL API design answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed GraphQL API design deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable GraphQL
API design doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey GraphQL API design when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
