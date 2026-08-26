---
name: ci-cd
description: Review CI/CD plans for reproducibility, untrusted input, credentials, artifact provenance, test gates, promotion, rollback, and deployment concurrency. Use when a plan changes build, test, release, or deployment automation.
---

# CI/CD plan review

Apply this guidance alongside the core GrumpyDev review, the
`dependency-supply-chain` skill, and the applicable installed
deployment-platform specialist.

## Inspect evidence

- Read workflow definitions, triggers, permissions, runners, caches, artifacts,
  environments, gates, deployment strategy, and rollback procedures.
- Trace code from an untrusted change through dependency install, build, test,
  artifact signing, promotion, deployment, and rollback.

## Establish the operating model

Establish the project target: CI/CD platform, runner trust and OS, branch and
approval policy, artifact flow, environments, credential model, deployment
ownership, and retention. The changed boundary must define: Trigger and trust
boundaries, reproducibility, artifacts, credentials, environments, approvals,
concurrency, caching, provenance, rollback, and failure recovery.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Trigger and trust boundaries, reproducibility,
artifacts, credentials, environments, approvals. Prove concurrency, caching,
provenance, rollback, failure recovery through rotation, overload, partial
rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for untrusted changes reaching secrets, mutable or unpinned
build dependencies, caches crossing trust boundaries, concurrent pipelines
racing over one environment, artifacts rebuilt differently for release, flaky
retries hiding failures, self-hosted runners retaining hostile state, workflow
output parsed as commands, and rollback stopping at code while data remains
changed.

- Minimize token and runner permissions by job; forked or pull-request code must
  not inherit release credentials.
- Prefer short-lived workload identity bound to repository, workflow,
  environment, and job over stored broad credentials. Prevent untrusted code,
  dependencies, test output, or generated artifacts from influencing credential
  requests or protected approvals.
- Require pinned toolchains and reproducible artifacts; do not rebuild different
  bytes for each environment.
- Treat caches and artifacts as integrity boundaries with explicit keys,
  retention, access, and poisoning controls.
- Separate verification from promotion, protect production environments,
  serialize conflicting deploys, and preserve an auditable approval trail.
- Protect workflow definitions, reusable automation, runner images, release
  metadata, signing authority, and deployment configuration with review and
  least privilege. Treat logs, annotations, environment files, and command
  outputs from builds as untrusted data.
- Isolate or reset self-hosted runners between trust domains. Do not let an
  untrusted change leave processes, files, credentials, containers, caches, or
  network access for a later privileged job.
- Attach provenance or signatures to the verified artifact when supported, and
  verify that identity at promotion. Build once, then promote that exact
  artifact through protected environments.
- Prove rollback or roll-forward against schema changes, background jobs,
  feature flags, and mixed-version traffic.

## Verify the claims

- Verify these behaviors through the effective CI/CD configuration and runtime
  topology: Trigger and trust boundaries, reproducibility, artifacts,
  credentials, environments, approvals. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: concurrency, caching, provenance,
  rollback, failure recovery. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Exercise untrusted pull requests, changed workflow files, malicious test
  output, poisoned caches, persistent runner state, expired identities,
  concurrent deploys, rejected promotion, signature failure, and rollback.

## Ask when evidence is missing

- Which triggers can run untrusted changes, and which credentials or protected
  environments can those runs reach?
- Is one verified artifact promoted across environments, and what restores
  service after a failed release?

## Calibrate findings

- Treat release credentials exposed to untrusted code or an unreviewed path to
  production as critical.
- Downgrade when triggers, permissions, promotion, and rollback are isolated and
  demonstrated by the workflow evidence.

## Add to the verdict

State trigger trust, runner isolation, short-lived permissions,
reproducibility, artifact provenance, promotion verification, release gates,
deployment concurrency, and rollback evidence.
