# Container survey contribution

## Applicability

Apply this contribution when an application is built or run as an OCI container image.
Skip it when Container does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Container, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Container runtime, base-image policy, target
  architectures, registry, user and privilege requirements, filesystem policy,
  resource limits, and orchestration platform.
- Review doctrine for: Image construction, user and privilege, filesystem,
  signals, PID 1, health checks, resources, architecture, networking, secrets,
  immutability, and supply chain.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Runtime, base image, architecture, user,
  capabilities, filesystem, mounts, network, secrets, resource limits, signals,
  health checks, image rollout, and recovery.

## Ask only when materially unresolved

- Which runtime privileges, capabilities, writable paths, and host resources
  does the container actually require?
- How does the process handle signals, health transitions, resource exhaustion,
  and read-only filesystems?
- Align existing domain questions with this deployment guidance when it is
  material: Runtime, base image, architecture, user, capabilities, filesystem,
  mounts, network, secrets, resource limits, signals, health checks, image
  rollout, and recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record Container answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Container survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Container doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Container when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
