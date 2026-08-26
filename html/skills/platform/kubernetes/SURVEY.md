# Kubernetes survey contribution

## Applicability

Apply this contribution when the project deploys workloads to Kubernetes or
depends on Kubernetes-specific behavior in development, testing, or operations.
Combine it with containers, CI/CD, observability, security, secrets, cloud,
network, storage, and application contributions. Deduplicate shared runtime,
identity, environment, and deployment questions.

## Inspect before asking

Inspect manifests, Helm or Kustomize configuration, rendered examples,
infrastructure code, GitOps definitions, policy files, CI workflows, runbooks,
and project documentation. Identify committed facts separately from
environment-specific facts. Do not access or change a cluster just to complete
the survey without explicit authority.

## Durable project facts

Collect project-wide facts likely to affect repeated reviews:

- Supported Kubernetes versions, distribution or cloud provider, cluster and
  region layout, node-pool classes, and cluster upgrade owner.
- Source of truth and rendering/deployment path for resources, including Helm,
  Kustomize, operators, GitOps, admission, and field ownership.
- Namespace and tenant boundaries, service-account and workload-identity model,
  RBAC owner, and pod-security baseline.
- Ingress or gateway, network plugin, DNS, network-policy, TLS termination, and
  proxy trust model.
- Standard workload controllers, probe conventions, graceful shutdown budget,
  rollout strategy, old/new version overlap, and migration-job convention.
- Resource measurement practice, standard requests and limits, replica and zone
  expectations, disruption policy, autoscaling mechanisms, and cluster capacity
  owner.
- Config and secret authorities, injection methods, rotation and reload model,
  and rules against sensitive data in manifests or logs.
- Persistent storage classes, backup/restore ownership, stateful workload
  policy, and regional recovery objective.
- Observability and incident tooling plus the emergency operator-access path
  when application networking or GitOps is unavailable.
- Deployment-profile guidance: cluster, provider, versions, nodes,
  namespaces, controllers, ingress, identity, network policy, storage,
  resources, scaling, rollout, drain, and failure-domain coverage.

## Ask only when materially unresolved

Ask only when repository and documentation evidence cannot establish a durable
fact that will alter future reviews. Examples include supported cluster
versions, the actual render/apply authority, tenancy boundaries, workload
identity, ingress and network-policy implementations, shutdown conventions,
capacity ownership, stateful recovery, and emergency access. Let the combined
survey assign sequential question numbers.

Keep plan-specific replica counts, probe thresholds, resource values, rollout
details, and failure scenarios in the live Grump evaluation unless they express
a durable project convention.
- Align existing domain questions with this deployment guidance when it is
  material: cluster, provider, versions, nodes, namespaces,
  controllers, ingress, identity, network policy, storage, resources, scaling,
  rollout, drain, and failure-domain coverage. Do not repeat the core profile
  confirmation.

## Record in .grump

Record confirmed facts under technology, runtime, deployment, security,
verification, and operational conventions. Identify the source of truth and
owners where those facts prevent future ambiguity. Record materially important
unknowns explicitly. Mark the specialist survey current only after relevant
durable questions are answered, deferred, or recorded as unresolved.

Map existing Kubernetes survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Do not store kubeconfigs, client certificates, tokens, secret values, private
registry credentials, sensitive manifests, live cluster dumps, transient pod
names, current node addresses, or raw survey transcripts. Do not assume a
manifest is effective merely because it exists, and do not duplicate companion
survey facts.

## Re-survey triggers

Re-survey after a Kubernetes major-version, distribution, provider, cluster,
region, or network-plugin change; adoption of a new render/GitOps/operator
model; namespace or tenancy redesign; identity or pod-security change; ingress
or gateway migration; rollout or shutdown convention change; autoscaling or
node-pool redesign; stateful storage change; or material recovery-objective
change.
