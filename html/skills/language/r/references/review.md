# R full-review guidance

## Operating conditions

Establish the project target: R version and distribution, package snapshot or
lock approach, operating systems, BLAS and native libraries, locale and
encoding, execution environment, and data-volume expectations. The changed
boundary must define: Vectorization and recycling, missing values, type
coercion, environments, lazy evaluation, package resolution, reproducibility,
native libraries, numerical behavior, parallelism, and data size.

## Failure patterns

- Require a reproducible package environment and declared R, system-library,
  locale, and time-zone assumptions.
- Check vector recycling, implicit coercion, non-standard evaluation, copy
  behavior, and missing-value propagation for silent errors.
- Separate exploratory evidence from production invariants and require tests for
  data shape, ranges, and schema drift.
- Verify statistical claims against sampling, leakage, multiple testing,
  calibration, and out-of-sample behavior where relevant.
- Demand deterministic seeds, artifact versioning, memory bounds, and
  restartable pipelines for scheduled or production work.

## Verification to run or specify in the plan

- Run the analysis in a clean R session using the declared package and
  system-library environment. Vary input lengths, missing values, factor
  levels, locale, and schema; check results for silent recycling or coercion.
- Repeat stochastic or parallel work using the project's reproducibility
  policy. Compare numerical results within justified tolerances and measure
  memory on representative data before accepting scale claims.
