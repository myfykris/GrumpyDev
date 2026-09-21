# Container survey contribution

## Applies when

Apply this contribution when an application is built or run as an OCI container image.

## Inspect

- Read containerfiles, build context, base images, stages, package locks,
  entrypoints, user settings, mounts, health checks, and runtime limits.

## Ask when unresolved

- Which runtime privileges, capabilities, writable paths, and host resources
  does the container actually require?

- How does the process handle signals, health transitions, resource exhaustion,
  and read-only filesystems?

- Which runtime or deployment differences are material for future reviews:
  Runtime, base image, architecture, user, capabilities, filesystem, mounts,
  network, secrets, resource limits, signals, health checks, image rollout, and
  recovery?

## Record

Map durable Container requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
