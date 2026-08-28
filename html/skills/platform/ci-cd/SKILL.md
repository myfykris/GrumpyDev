---
name: ci-cd
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review CI/CD plans and other engineering artifacts for reproducibility, untrusted input, credentials, artifact provenance, test gates, promotion, rollback, and deployment concurrency. Project applicability: the project uses automation to build, test, release, promote, or deploy software."
---

# CI/CD GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
