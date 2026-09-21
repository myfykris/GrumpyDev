---
name: gd-kubernetes
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Kubernetes engineering work for workload lifecycle, scheduling, networking, identity, secrets, resources, rollout safety, autoscaling, and recovery."
---

# Kubernetes GrumpyDev review

## Quick checks

- Inspect rendered objects, admission effects, controllers, field ownership,
  cluster versions, workload type, identity, networking, volumes, probes,
  resources, scaling, disruption, and termination.
- Trace image, config, secret, rollout, migration, worker, job, and operator
  paths. Do not review only chart values or another friendly source.
- Challenge outage-producing probes, rollout deadlocks, guessed resources,
  broad identity, manual edits to reconciled fields, and rollback that ignores
  data or messages.
- Require old/new compatibility, real drain behavior, capacity headroom,
  controller ownership, and recovery under dependency, node, zone, or upgrade
  failure.

## References

- For a material Kubernetes effect or uncertainty in a full review, read
  [review.md](references/review.md).
- For probes, termination, disruption, rollouts, migrations, or rollback, read
  [health-lifecycle-and-rollouts.md](references/health-lifecycle-and-rollouts.md).
- For resources, placement, quotas, autoscaling, or capacity, read
  [resources-placement-and-scaling.md](references/resources-placement-and-scaling.md).
- For networking, ingress, identity, RBAC, security, or secrets, read
  [networking-identity-and-secrets.md](references/networking-identity-and-secrets.md).
- For volumes, StatefulSets, operators, backup, restore, or failover, read
  [stateful-work-and-recovery.md](references/stateful-work-and-recovery.md).

## Verdict context

Name the rendered workload, reconciling owner, cluster boundary, rollout and
drain assumptions, and unverified operational behavior.
