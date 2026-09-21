---
name: gd-r
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review R engineering work for package reproducibility, vectorized semantics, missing data, statistical validity, memory behavior, native dependencies, and productionization risks."
---

# R GrumpyDev review

## Quick checks

- Read package metadata, lockfiles, session information, data schemas,
  statistical assumptions, native dependencies, pipeline definitions, and
  representative tests.

- Trace missing values, factor and date handling, joins, grouping, random seeds,
  model artifacts, serialization, and memory-intensive operations.

Watch especially for vector recycling, NA and NaN handled as ordinary values,
factor or string conversions, copy-on-modify memory spikes, nonstandard
evaluation selecting the wrong names, uncontrolled random seeds, and
package-version drift changing numerical results.

- Assess silently incorrect analysis, unreproducible regulated output, or memory
  failure on required data scale under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the R specialist.

## Verdict context

State environment reproducibility, data assumptions, statistical validity
limits, memory and execution model, and evidence from representative data.
