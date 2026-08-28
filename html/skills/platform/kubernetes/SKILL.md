---
name: kubernetes
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Kubernetes plans and other engineering artifacts for workload lifecycle, scheduling, networking, identity, secrets, resources, rollout safety, autoscaling, and recovery. Project applicability: the project deploys or operates workloads on Kubernetes or depends on Kubernetes-specific behavior."
---

# Kubernetes GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Coordinate findings with the active container, cloud, ingress, storage, queue,
database, security, and observability specialists for the project's Kubernetes
workloads.

## Lean review

- Inspect rendered objects, admission effects, controllers, field ownership,
  cluster versions, workload type, service accounts, security contexts,
  networking, volumes, probes, resources, scaling, disruption, and termination.
- Trace image, identity, config, secret, rollout, migration, worker, job, and
  operator paths. Do not review only chart values or another friendly source.
- Challenge probes that manufacture outages, rollout settings that deadlock on
  capacity or disruption budgets, guessed requests and limits, broad identity,
  manual edits to reconciled fields, and rollback that ignores data or messages.
- Require old/new compatibility, actual signal and drain behavior, resource
  headroom, controller ownership, and recovery under node drain, dependency
  loss, zone loss, and cluster upgrade.

Lean mode is insufficient for identity or network-policy changes, stateful
workloads, cluster upgrades, autoscaling redesign, migration-coupled rollout,
operator or CRD changes, or multi-zone recovery claims.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/health-lifecycle-and-rollouts.md):
  Read when the reviewed work directly or indirectly changes probes, startup, readiness,
  liveness, termination, pre-stop
  behavior, disruption budgets, Deployment or StatefulSet rollout strategy, draining,
  mixed versions, migration order, rollback, or controller replacement.
- [Focused rules](references/resources-placement-and-scaling.md):
  Read when the reviewed work directly or indirectly changes requests, limits, CPU or
  memory behavior, scheduling,
  affinity, topology spread, taints, priorities, quotas, autoscaling, cluster scaling,
  capacity, or overload behavior.
- [Focused rules](references/networking-identity-and-secrets.md):
  Read when the reviewed work directly or indirectly changes Services, Ingress, Gateway
  API, DNS, network policy,
  service accounts, RBAC, workload identity, pod security, secrets, certificate
  rotation, external exposure, or operator access.
- [Focused rules](references/stateful-work-and-recovery.md):
  Read when the reviewed work directly or indirectly changes persistent volumes, storage
  classes, StatefulSets,
  operators, databases, backup, restore, snapshots, fencing, failover, attachment,
  regional recovery, or stateful migration.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

Name the rendered workload, reconciling owner, cluster boundary, rollout and
drain assumptions, and any operational behavior that remains unverified.
