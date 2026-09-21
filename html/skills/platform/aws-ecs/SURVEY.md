# AWS ECS survey contribution

## Applies when

Apply this contribution when the project deploys or operates workloads with Amazon ECS,
Fargate, or ECS on EC2.

## Inspect

- Read infrastructure as code, task definitions, service deployment settings,
  capacity providers, load balancer configuration, autoscaling policies,
  security groups, IAM roles, logging, and alarms.

## Ask when unresolved

- Which ECS launch type, platform version, deployment controller, capacity
  provider, and network mode will run the service?

- What health, drain, rollback, and IAM behavior applies during a failed or
  mixed-task deployment?

- Which runtime or deployment differences are material for future reviews:
  Cluster and launch type, task and service definitions, regions and zones, IAM
  roles, load balancer, networking, storage, secrets, scaling, rollout, drain,
  and recovery?

## Record

Map durable AWS ECS requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
