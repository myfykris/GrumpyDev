# Performance and capacity survey contribution

## Applicability

Apply this contribution when a plan claims or changes latency, throughput,
resource, or scale behavior. Skip it when Performance and capacity does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Performance and capacity, inspect version declarations, effective
configuration sources, rendered artifacts, infrastructure and identity policy,
build and deployment workflows, service objectives, operational runbooks, and
project documentation. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: SLOs, traffic and growth, workload mix, peak
  factors, capacity budgets, test environments, autoscaling, resource limits,
  and cost constraints.
- Review doctrine for: Workload model, latency distributions, throughput,
  concurrency, saturation, queuing, caches, load tests, profiling, limits,
  scaling, and degradation.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Instance and resource limits, replicas,
  autoscaling, quotas, downstream ceilings, network path, cold start, failure
  domains, load-test environment, and capacity owner.

## Ask only when materially unresolved

- What measured latency, throughput, concurrency, resource, and tail-percentile
  budget defines success?
- Which representative load shape, bottleneck, saturation point, and degraded
  mode support the capacity claim?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Instance and resource limits, replicas,
  autoscaling, quotas, downstream ceilings, network path, cold start, failure
  domains, load-test environment, and capacity owner? Ask only when evidence
  and the core profile confirmation do not resolve them.

## Record in .grump

Record Performance and capacity answers in project technology, runtime,
security, deployment, verification, and operational doctrine. Preserve source
and scope. Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Performance and capacity deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Performance and capacity doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey Performance and capacity when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
