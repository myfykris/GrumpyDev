# AWS ECS full-review guidance

## Operating conditions

Establish the project target: ECS launch type, regions and clusters, networking,
IAM model, registry, secret stores, load balancers, deployment strategy,
autoscaling, and observability. The changed boundary must define: Task and
service lifecycle, networking, IAM, secrets, images, health checks, deployment
controllers, autoscaling, capacity providers, logs, and rollback.

## Failure patterns

- Calculate whether minimum/maximum healthy percentages and available capacity
  permit the proposed rolling deployment. Account for image pull, startup,
  health-check grace, and deregistration time.
- Distinguish container health, target-group health, application readiness, and
  dependency availability. Reject circular or shallow health checks.
- Check SIGTERM handling, stop timeout, connection draining, background work,
  queue visibility, and safe task replacement.
- Separate execution-role permissions from task-role permissions. Demand least
  privilege and identify cross-account, secret, and KMS boundaries.
- Trace public/private subnet routing, NAT or endpoint dependencies, DNS,
  security-group direction, load balancer ports, and ephemeral outbound needs.
- Test autoscaling metrics against the actual bottleneck and account for cold
  start, downstream capacity, quotas, and scale-in data loss.
- Require immutable image identity, deployment visibility, actionable alarms,
  log retention, and a rollback that works when the new task cannot become
  healthy.

## Verification to run or specify in the plan

- Render and inspect the task definition, service, target groups, IAM policies,
  secrets, networking, alarms, autoscaling and capacity-provider settings that
  will actually be deployed.
- Deploy representative old and new task revisions under constrained capacity.
  Exercise failed image pulls, slow startup, failed readiness, load-balancer
  deregistration, SIGTERM, forced stop, dependency loss and rollback.
- Load test scale-out and scale-in against downstream quotas, and verify logs
  and alarms make a stuck or failed deployment actionable.
