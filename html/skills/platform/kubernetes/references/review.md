# Kubernetes standard review

Apply this guidance alongside the core GrumpyDev review and the `containers`,
`observability`, `application-security`, and deployment specialists. Add the
cloud, ingress, storage, queue, and database skills that own actual
dependencies. Review rendered resources and live operating assumptions, not only
the friendly abstraction used to generate them.

## Inspect evidence

- Read manifests, rendered templates, overlays, admission results, custom
  resources, controllers, and generated objects. Trace each field to the tool or
  operator that owns it so the plan does not edit an overwritten resource.
- Establish supported Kubernetes versions, distribution or provider, node pools,
  runtime classes, cluster and namespace boundaries, regional topology, upgrade
  policy, and control-plane responsibilities.
- Inspect workload controllers, pod templates, service accounts, security
  contexts, volumes, services, ingress or gateway configuration, network
  policies, disruption budgets, topology rules, requests, limits, autoscaling,
  probes, lifecycle hooks, and termination settings.
- Trace image construction and identity, config and secret injection, rollout,
  rollback, database migration, background worker, scheduled job, and operator
  access paths.
- Use observed startup, latency, resource, scaling, eviction, and shutdown
  behavior for capacity claims. Default values and small development clusters
  are not production evidence.

## Establish the operating model

State which team owns the cluster, namespaces, add-ons, workload resources,
deployments, and incidents. Identify the controllers that reconcile each
resource and the source of truth used to render it. State tenancy and trust
boundaries among namespaces, service accounts, nodes, clusters, and cloud
identities.

For every workload, define startup phases, readiness semantics, steady-state
capacity, graceful drain behavior, termination deadline, disruption tolerance,
placement requirements, and dependency behavior. Distinguish Deployments,
StatefulSets, DaemonSets, Jobs, CronJobs, and operator-managed resources because
their replacement and completion rules are materially different.

Describe rollout order, mixed-version compatibility, migration ownership,
rollback limits, secret/config rotation, and what happens during node drain,
zone loss, cluster upgrade, dependency outage, and control-plane unavailability.

## Challenge the reviewed work

### Recurring traps

Watch especially for probes that manufacture outages, rollouts deadlocked by
capacity or disruption rules, requests and limits based on guesses, rendered
resources differing from reviewed values, broad service-account access,
controller-owned fields edited manually, and rollback assumed to reverse
migrations or messages.

### Rendering and ownership

- Require review of the exact rendered objects applied to each environment.
  Chart values, Kustomize overlays, and application manifests can combine into
  surprising selectors, privileges, images, and defaults.
- Identify field ownership and reconciliation. Manual edits to an operator- or
  GitOps-managed object are temporary and can create false recovery confidence.
- Pin resource APIs and workload behavior to supported cluster versions. Include
  removed APIs, admission policies, CRD conversion, and add-on compatibility in
  cluster upgrades.
- Ensure labels, selectors, service ports, container ports, volume names, and
  references match. Immutable-field changes may require replacement rather than
  an in-place update.

## Verify the claims

- Render and schema-validate every environment's resources, then apply them to a
  representative test cluster with the same admission and policy controls.
- Drain nodes and disrupt zones while checking disruption budgets, placement,
  rescheduling, volume attachment, DNS, and user-visible availability.
- Restore state and recover a workload with the normal controllers, then test
  the documented emergency path without assuming the main application works.

## Ask when evidence is missing

Ask only material questions: supported cluster versions and provider, workload
controller, namespace and tenancy boundaries, ownership and render pipeline,
identity model, ingress and network implementation, availability objective,
resource evidence, disruption tolerance, autoscaling source, storage class,
rollout/migration order, and rollback or regional recovery path. Ask how probes,
shutdown, retries, secrets, and operator access behave when the relevant plan
changes those boundaries.

Do not ask for durable facts already recorded in `.grump`, manifests, rendered
configuration, infrastructure code, or project documentation. Inspect first.

## Calibrate findings

- Treat cluster-wide privilege, public exposure, secret disclosure, guaranteed
  unavailability, corrupt stateful failover, or an irreversible rollout without
  recovery as critical or high according to reach and likelihood.
- Treat unschedulable policies, weak capacity evidence, probe-induced outage,
  controller ownership conflicts, or missing operational recovery as material
  when they threaten requirements.
- Downgrade when rendered output, representative cluster tests, workload
  observations, least-privilege checks, disruption exercises, and recovery
  evidence demonstrate the behavior.
- Do not report generic Kubernetes preferences. Tie findings to the actual
  cluster, controller, workload, failure mode, or unsupported assertion.

## Add to the verdict

State the cluster and controller assumptions, rendered workload behavior,
startup/readiness/shutdown semantics, resource and placement envelope, rollout
and mixed-version rules, identity and network boundaries, stateful recovery,
operator access, and remaining evidence gaps.
