---
name: gd-aws-ecs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review AWS ECS engineering work for task lifecycle, deployment, capacity, networking, IAM, secrets, observability, scaling, and recovery risks."
---

# AWS ECS GrumpyDev review

## Quick checks

- Read infrastructure as code, task definitions, service deployment settings,
  capacity providers, load balancer configuration, autoscaling policies,
  security groups, IAM roles, logging, and alarms.

- Establish whether tasks use Fargate or EC2, their network mode, placement
  constraints, persistent dependencies, health checks, and expected traffic.

Watch especially for task and service lifecycle being confused, load-balancer
draining shorter than process shutdown, execution and task roles granting the
wrong access, secret rotation without process refresh, architecture or Fargate
constraints, and rollout rollback assumed to reverse data changes.

- Assess lost traffic, broad task or execution roles, unrecoverable deployment
  state, or capacity exhaustion under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the AWS ECS specialist.

## Verdict context

State the capacity calculation, health and drain model, IAM boundary, network
path, scaling signal, and exact rollback trigger and mechanism.
