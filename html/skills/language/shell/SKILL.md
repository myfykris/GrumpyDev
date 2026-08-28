---
name: shell
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review POSIX shell and Bash plans and other engineering artifacts for quoting, expansion, pipelines, error propagation, portability, idempotency, filesystem safety, and automation risks. Project applicability: the project contains or executes POSIX shell or Bash scripts, build steps, deployment scripts, or operational automation."
---

# Shell GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read the declared shell, shebangs, strict-mode settings, target operating
  systems, command dependencies, environment assumptions, and tests.

- Trace expansions, pipelines, temporary files, signals, cleanup traps,
  privilege boundaries, retries, and every destructive target.

Watch especially for word splitting and glob expansion, set -e providing false
confidence, pipeline failures being discarded, unsafe temporary-file patterns,
traps that do not cover every termination path, utility differences across
systems, and bytes interpreted under an assumed locale.

Lean mode is insufficient when this material severity condition may apply:

- Treat command injection, destructive expansion, credential leakage, or ignored
  partial failure as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Shell evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the shell and platform contract, quoting and encoding assumptions,
mutation safeguards, error propagation, and realistic execution evidence.
