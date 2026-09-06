---
name: aws-ecs
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review AWS ECS engineering work for task lifecycle, deployment, capacity, networking, IAM, secrets, observability, scaling, and recovery risks."
---

# AWS ECS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read infrastructure as code, task definitions, service deployment settings,
  capacity providers, load balancer configuration, autoscaling policies,
  security groups, IAM roles, logging, and alarms.

- Establish whether tasks use Fargate or EC2, their network mode, placement
  constraints, persistent dependencies, health checks, and expected traffic.

Watch especially for task and service lifecycle being confused, load-balancer
draining shorter than process shutdown, execution and task roles granting the
wrong access, secret rotation without process refresh, architecture or Fargate
constraints, and rollout rollback assumed to reverse data changes.

Lean mode is insufficient when this material severity condition may apply:

- Treat lost traffic, broad task or execution roles, unrecoverable deployment
  state, or capacity exhaustion as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete AWS ECS evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the capacity calculation, health and drain model, IAM boundary, network
path, scaling signal, and exact rollback trigger and mechanism.
