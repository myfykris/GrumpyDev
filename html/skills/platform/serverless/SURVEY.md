# Serverless survey contribution

## Applicability

Apply this contribution when the project runs application work on functions or managed
event-driven compute.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Serverless, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Provider and runtimes, regions, triggers,
  concurrency and timeout limits, network attachment, identity, packaging,
  deployment tool, and local-test limits.
- Review doctrine for: Invocation lifecycle, concurrency, cold starts, timeouts,
  retries, events, idempotency, state, networking, IAM, packaging,
  observability, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: provider, region, runtime, trigger,
  concurrency, timeout, ephemeral storage, identity, networking, cold start,
  retries, destinations, limits, and deployment coverage.

## Ask only when materially unresolved

- Which provider, service, runtime version, deployment mode, trigger, and
  regional limits apply?
- What delivery, concurrency, timeout, retry, state, networking, permission, and
  cost behavior follows from that platform?
- Align existing domain questions with this deployment guidance when it is
  material: provider, region, runtime, trigger, concurrency, timeout,
  ephemeral storage, identity, networking, cold start, retries, destinations,
  limits, and deployment coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record Serverless answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Serverless survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Serverless doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Serverless when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
