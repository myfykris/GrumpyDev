---
name: aws-ecs
description: Review AWS ECS engineering plans for task lifecycle, deployment, capacity, networking, IAM, secrets, observability, scaling, and recovery risks. Use when a plan changes ECS services, task definitions, Fargate or EC2 capacity, load balancing, or container deployment operations.
---

# AWS ECS plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read infrastructure as code, task definitions, service deployment settings,
  capacity providers, load balancer configuration, autoscaling policies,
  security groups, IAM roles, logging, and alarms.
- Establish whether tasks use Fargate or EC2, their network mode, placement
  constraints, persistent dependencies, health checks, and expected traffic.
- Trace image build/tagging, secret delivery, deployment promotion, and
  rollback.

## Establish the operating model

Establish the project target: ECS launch type, regions and clusters, networking,
IAM model, registry, secret stores, load balancers, deployment strategy,
autoscaling, and observability. The changed boundary must define: Task and
service lifecycle, networking, IAM, secrets, images, health checks, deployment
controllers, autoscaling, capacity providers, logs, and rollback.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Task and service lifecycle, networking, IAM, secrets,
images, health checks. Prove deployment controllers, autoscaling, capacity
providers, logs, rollback through rotation, overload, partial rollout, drain,
forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for task and service lifecycle being confused, load-balancer
draining shorter than process shutdown, execution and task roles granting the
wrong access, secret rotation without process refresh, architecture or Fargate
constraints, and rollout rollback assumed to reverse data changes.

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

- Verify these behaviors through the effective AWS ECS configuration and runtime
  topology: Task and service lifecycle, networking, IAM, secrets, images, health
  checks. Use effective rendered configuration and deployable artifacts in a
  representative identity, topology, capacity, and policy boundary.
- Exercise failure and edge behavior for: deployment controllers, autoscaling,
  capacity providers, logs, rollback. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which ECS launch type, platform version, deployment controller, capacity
  provider, and network mode will run the service?
- What health, drain, rollback, and IAM behavior applies during a failed or
  mixed-task deployment?

## Calibrate findings

- Treat lost traffic, broad task or execution roles, unrecoverable deployment
  state, or capacity exhaustion as critical.
- Downgrade when the change is isolated, least-privileged, capacity-tested, and
  has a verified rollback path.

## Add to the verdict

State the capacity calculation, health and drain model, IAM boundary, network
path, scaling signal, and exact rollback trigger and mechanism.
