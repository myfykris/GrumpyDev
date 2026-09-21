# Kubernetes full-review guidance

## Operating conditions

State which team owns the cluster, namespaces, add-ons, workload resources,
deployments, and incidents. Identify the controllers that reconcile each
resource and the source of truth used to render it. State tenancy and trust
boundaries among namespaces, service accounts, nodes, clusters, and cloud
identities.

## Failure patterns

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

## Verification to run or specify in the plan

- Render and schema-validate every environment's resources, then apply them to a
  representative test cluster with the same admission and policy controls.
- Drain nodes and disrupt zones while checking disruption budgets, placement,
  rescheduling, volume attachment, DNS, and user-visible availability.
- Restore state and recover a workload with the normal controllers, then test
  the documented emergency path without assuming the main application works.
