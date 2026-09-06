---
name: ci-cd
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review CI/CD engineering work for reproducibility, untrusted input, credentials, artifact provenance, test gates, promotion, rollback, and deployment concurrency."
---

# CI/CD GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review, the
`dependency-supply-chain` skill, and the applicable installed
deployment-platform specialist.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat release credentials exposed to untrusted code or an unreviewed path to
  production as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete CI/CD evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State trigger trust, runner isolation, short-lived permissions,
reproducibility, artifact provenance, promotion verification, release gates,
deployment concurrency, and rollback evidence.
