---
name: r
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review R engineering work for package reproducibility, vectorized semantics, missing data, statistical validity, memory behavior, native dependencies, and productionization risks."
---

# R GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read package metadata, lockfiles, session information, data schemas,
  statistical assumptions, native dependencies, pipeline definitions, and
  representative tests.

- Trace missing values, factor and date handling, joins, grouping, random seeds,
  model artifacts, serialization, and memory-intensive operations.

Watch especially for vector recycling, NA and NaN handled as ordinary values,
factor or string conversions, copy-on-modify memory spikes, nonstandard
evaluation selecting the wrong names, uncontrolled random seeds, and
package-version drift changing numerical results.

Lean mode is insufficient when this material severity condition may apply:

- Treat silently incorrect analysis, unreproducible regulated output, or memory
  failure on required data scale as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete R evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State environment reproducibility, data assumptions, statistical validity
limits, memory and execution model, and evidence from representative data.
