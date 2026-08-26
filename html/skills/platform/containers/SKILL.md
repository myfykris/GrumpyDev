---
name: containers
description: Review container plans for image provenance, build context, runtime privilege, filesystem assumptions, signals, health, resources, and reproducibility. Use when an application is built or run as an OCI container image.
---

# Container plan review

Apply this guidance alongside the core GrumpyDev review, the
`dependency-supply-chain` skill, and the applicable `kubernetes` or `aws-ecs`
skill.

## Inspect evidence

- Read containerfiles, build context, base images, stages, package locks,
  entrypoints, user settings, mounts, health checks, and runtime limits.
- Trace build, secret use, startup, signal delivery, shutdown, filesystem
  writes, dependency loss, and image replacement.

## Establish the operating model

Establish the project target: Container runtime, base-image policy, target
architectures, registry, user and privilege requirements, filesystem policy,
resource limits, and orchestration platform. The changed boundary must define:
Image construction, user and privilege, filesystem, signals, PID 1, health
checks, resources, architecture, networking, secrets, immutability, and supply
chain.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Image construction, user and privilege, filesystem,
signals, PID 1, health checks. Prove resources, architecture, networking,
secrets, immutability, supply chain through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for mutable image tags, PID 1 and signal behavior, build
secrets retained in layers, root or excessive capabilities, writable filesystem
assumptions, architecture mismatches, health checks that do not represent
service readiness, and shutdown deadlines shorter than cleanup.

- Pin and verify base images and dependencies; a mutable tag is not a
  reproducible or reviewable input.
- Keep credentials out of layers, history, build arguments, caches, logs, and
  copied context.
- Run as a non-root user when the service can operate without privilege. For an
  exception, require the exact privilege, why it cannot be dropped, the smallest
  capability and writable surface, and runtime evidence that the boundary holds.
- Require correct PID 1 behavior, signal forwarding, graceful termination,
  readiness, liveness, and startup semantics.
- Set CPU, memory, file, process, and temporary-storage expectations, then test
  behavior when each limit is reached.

## Verify the claims

- Verify these behaviors through the effective Container configuration and
  runtime topology: Image construction, user and privilege, filesystem, signals,
  PID 1, health checks. Use effective rendered configuration and deployable
  artifacts in a representative identity, topology, capacity, and policy
  boundary.
- Exercise failure and edge behavior for: resources, architecture, networking,
  secrets, immutability, supply chain. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which runtime privileges, capabilities, writable paths, and host resources
  does the container actually require?
- How does the process handle signals, health transitions, resource exhaustion,
  and read-only filesystems?

## Calibrate findings

- Treat unnecessary host access, broad privilege, or a lifecycle failure that
  can corrupt state or prevent shutdown as critical.
- Downgrade when each exception is narrowly justified and runtime tests prove
  the intended boundary.

## Add to the verdict

State image provenance, secret boundaries, runtime privilege, process lifecycle,
resource limits, and reproducibility evidence.
