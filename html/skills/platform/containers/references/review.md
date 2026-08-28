# Container standard review

## Establish the operating model

Establish the project target: Container runtime, base-image policy, target
architectures, registry, user and privilege requirements, filesystem policy,
resource limits, and orchestration platform. The changed boundary must define:
Image construction, user and privilege, filesystem, signals, PID 1, health
checks, resources, architecture, networking, secrets, immutability, and supply
chain.

Identify the authoritative build context, base image, dependency and registry
inputs, runtime user, capabilities, writable mounts, network, secret injection,
health contract, resource limits, and orchestrator settings. Prove the built
image for every target architecture starts without hidden build-time state,
handles signals as PID 1, remains within its privilege and filesystem boundary,
and fails predictably at each resource limit.

## Challenge the reviewed work

### Recurring traps

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

- Build from a clean context for every supported architecture and inspect image
  layers, packages, users, capabilities, writable paths and embedded material.
- Run with the production user, read-only filesystem, declared mounts,
  network and secret injection. Remove undeclared privileges and verify startup,
  readiness and application behavior.
- Send graceful and forced termination, exhaust CPU, memory, process, file and
  temporary-storage limits, and make dependencies unavailable while observing
  health transitions and required-work preservation.

## Ask when evidence is missing

- Which runtime privileges, capabilities, writable paths, and host resources
  does the container actually require?
- How does the process handle signals, health transitions, resource exhaustion,
  and read-only filesystems?

## Calibrate findings

- Downgrade when each exception is narrowly justified and runtime tests prove
  the intended boundary.
