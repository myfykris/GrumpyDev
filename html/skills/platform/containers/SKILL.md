---
name: containers
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review container plans and other engineering artifacts for image provenance, build context, runtime privilege, filesystem assumptions, signals, health, resources, and reproducibility. Project applicability: an application is built or run as an OCI container image."
---

# Container GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the
`dependency-supply-chain` skill, and the applicable `kubernetes` or `aws-ecs`
skill.

## Lean review

- Read containerfiles, build context, base images, stages, package locks,
  entrypoints, user settings, mounts, health checks, and runtime limits.

- Trace build, secret use, startup, signal delivery, shutdown, filesystem
  writes, dependency loss, and image replacement.

Watch especially for mutable image tags, PID 1 and signal behavior, build
secrets retained in layers, root or excessive capabilities, writable filesystem
assumptions, architecture mismatches, health checks that do not represent
service readiness, and shutdown deadlines shorter than cleanup.

Lean mode is insufficient when this material severity condition may apply:

- Treat unnecessary host access, broad privilege, or a lifecycle failure that
  can corrupt state or prevent shutdown as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Container evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State image provenance, secret boundaries, runtime privilege, process lifecycle,
resource limits, and reproducibility evidence.
