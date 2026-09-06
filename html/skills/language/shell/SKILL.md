---
name: shell
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review POSIX shell and Bash engineering work for quoting, expansion, pipelines, error propagation, portability, idempotency, filesystem safety, and automation risks."
---

# Shell GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
