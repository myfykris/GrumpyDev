# AWS ECS standard review

## Inspect additional evidence

- Trace image build/tagging, secret delivery, deployment promotion, and
  rollback.

## Establish the operating model

Establish the project target: ECS launch type, regions and clusters, networking,
IAM model, registry, secret stores, load balancers, deployment strategy,
autoscaling, and observability. The changed boundary must define: Task and
service lifecycle, networking, IAM, secrets, images, health checks, deployment
controllers, autoscaling, capacity providers, logs, and rollback.

Identify the owners and sources of truth for task definitions, services,
images, execution and task roles, secrets, networking, target groups, deployment
controllers, capacity providers, autoscaling, alarms, logs, and rollback. Show
that placement capacity, health transitions, deregistration, stop timeouts, and
mixed task revisions permit the selected deployment and a failed deployment's
recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Render and inspect the task definition, service, target groups, IAM policies,
  secrets, networking, alarms, autoscaling and capacity-provider settings that
  will actually be deployed.
- Deploy representative old and new task revisions under constrained capacity.
  Exercise failed image pulls, slow startup, failed readiness, load-balancer
  deregistration, SIGTERM, forced stop, dependency loss and rollback.
- Load test scale-out and scale-in against downstream quotas, and verify logs
  and alarms make a stuck or failed deployment actionable.

## Ask when evidence is missing

- Which ECS launch type, platform version, deployment controller, capacity
  provider, and network mode will run the service?
- What health, drain, rollback, and IAM behavior applies during a failed or
  mixed-task deployment?

## Calibrate findings

- Downgrade when the change is isolated, least-privileged, capacity-tested, and
  has a verified rollback path.
