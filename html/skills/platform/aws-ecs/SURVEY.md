# AWS ECS survey contribution

## Applicability

Apply this contribution when the project deploys or operates workloads with Amazon ECS,
Fargate, or ECS on EC2.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For AWS ECS, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: ECS launch type, regions and clusters, networking,
  IAM model, registry, secret stores, load balancers, deployment strategy,
  autoscaling, and observability.
- Review doctrine for: Task and service lifecycle, networking, IAM, secrets,
  images, health checks, deployment controllers, autoscaling, capacity
  providers, logs, and rollback.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Cluster and launch type, task and service
  definitions, regions and zones, IAM roles, load balancer, networking,
  storage, secrets, scaling, rollout, drain, and recovery.

## Ask only when materially unresolved

- Which ECS launch type, platform version, deployment controller, capacity
  provider, and network mode will run the service?
- What health, drain, rollback, and IAM behavior applies during a failed or
  mixed-task deployment?
- Align existing domain questions with this deployment guidance when it is
  material: Cluster and launch type, task and service definitions, regions and
  zones, IAM roles, load balancer, networking, storage, secrets, scaling,
  rollout, drain, and recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record AWS ECS answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing AWS ECS survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable AWS ECS
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey AWS ECS when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
