---
name: gd-containers
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review container engineering work for image provenance, build context, runtime privilege, filesystem assumptions, signals, health, resources, and reproducibility."
---

# Container GrumpyDev review

## Quick checks

- Read containerfiles, build context, base images, stages, package locks,
  entrypoints, user settings, mounts, health checks, and runtime limits.

- Trace build, secret use, startup, signal delivery, shutdown, filesystem
  writes, dependency loss, and image replacement.

Watch especially for mutable image tags, PID 1 and signal behavior, build
secrets retained in layers, root or excessive capabilities, writable filesystem
assumptions, architecture mismatches, health checks that do not represent
service readiness, and shutdown deadlines shorter than cleanup.

- Assess unnecessary host access, broad privilege, or a lifecycle failure that
  can corrupt state or prevent shutdown under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Container
specialist.

## Verdict context

State image provenance, secret boundaries, runtime privilege, process lifecycle,
resource limits, and reproducibility evidence.
