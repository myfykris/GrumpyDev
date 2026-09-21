---
name: gd-shell
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review POSIX shell and Bash engineering work for quoting, expansion, pipelines, error propagation, portability, idempotency, filesystem safety, and automation risks."
---

# Shell GrumpyDev review

## Quick checks

- Read the declared shell, shebangs, strict-mode settings, target operating
  systems, command dependencies, environment assumptions, and tests.

- Trace expansions, pipelines, temporary files, signals, cleanup traps,
  privilege boundaries, retries, and every destructive target.

Watch especially for word splitting and glob expansion, set -e providing false
confidence, pipeline failures being discarded, unsafe temporary-file patterns,
traps that do not cover every termination path, utility differences across
systems, and bytes interpreted under an assumed locale.

- Assess command injection, destructive expansion, credential leakage, or ignored
  partial failure under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Shell specialist.

## Verdict context

State the shell and platform contract, quoting and encoding assumptions,
mutation safeguards, error propagation, and realistic execution evidence.
