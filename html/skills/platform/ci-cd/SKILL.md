---
name: gd-ci-cd
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review CI/CD engineering work for reproducibility, untrusted input, credentials, artifact provenance, test gates, promotion, rollback, and deployment concurrency."
---

# CI/CD GrumpyDev review

## Quick checks

- Read workflow definitions, triggers, permissions, runners, caches, artifacts,
  environments, gates, deployment strategy, and rollback procedures.

- Trace code from an untrusted change through dependency install, build, test,
  artifact signing, promotion, deployment, and rollback.

Watch especially for untrusted changes reaching secrets, mutable or unpinned
build dependencies, caches crossing trust boundaries, concurrent pipelines
racing over one environment, artifacts rebuilt differently for release, flaky
retries hiding failures, self-hosted runners retaining hostile state, workflow
output parsed as commands, and rollback stopping at code while data remains
changed.

- Assess release credentials exposed to untrusted code or an unreviewed path to
  production under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the CI/CD specialist.

## Verdict context

State trigger trust, runner isolation, short-lived permissions,
reproducibility, artifact provenance, promotion verification, release gates,
deployment concurrency, and rollback evidence.
