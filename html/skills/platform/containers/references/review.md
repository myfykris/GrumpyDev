# Container full-review guidance

## Operating conditions

Establish the project target: Container runtime, base-image policy, target
architectures, registry, user and privilege requirements, filesystem policy,
resource limits, and orchestration platform. The changed boundary must define:
Image construction, user and privilege, filesystem, signals, PID 1, health
checks, resources, architecture, networking, secrets, immutability, and supply
chain.

## Failure patterns

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

## Verification to run or specify in the plan

- Build from a clean context for every supported architecture and inspect image
  layers, packages, users, capabilities, writable paths and embedded material.
- Run with the production user, read-only filesystem, declared mounts,
  network and secret injection. Remove undeclared privileges and verify startup,
  readiness and application behavior.
- Send graceful and forced termination, exhaust CPU, memory, process, file and
  temporary-storage limits, and make dependencies unavailable while observing
  health transitions and required-work preservation.
