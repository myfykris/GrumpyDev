---
name: r
description: Review R engineering plans for package reproducibility, vectorized semantics, missing data, statistical validity, memory behavior, native dependencies, and productionization risks. Use when a plan changes R packages, analyses, data pipelines, reports, models, or services.
---

# R plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read package metadata, lockfiles, session information, data schemas,
  statistical assumptions, native dependencies, pipeline definitions, and
  representative tests.
- Trace missing values, factor and date handling, joins, grouping, random seeds,
  model artifacts, serialization, and memory-intensive operations.

## Establish the operating model

Establish the project target: R version and distribution, package snapshot or
lock approach, operating systems, BLAS and native libraries, locale and
encoding, execution environment, and data-volume expectations. The changed
boundary must define: Vectorization and recycling, missing values, type
coercion, environments, lazy evaluation, package resolution, reproducibility,
native libraries, numerical behavior, parallelism, and data size.

Define ownership, errors, cancellation, and concurrency for Vectorization and
recycling, missing values, type coercion, environments, lazy evaluation, package
resolution. Verify version, package, native, serialization, and artifact
compatibility for reproducibility, native libraries, numerical behavior,
parallelism, data size across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for vector recycling, NA and NaN handled as ordinary values,
factor or string conversions, copy-on-modify memory spikes, nonstandard
evaluation selecting the wrong names, uncontrolled random seeds, and
package-version drift changing numerical results.

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

## Verify the claims

- Verify these behaviors through the declared R compiler and runtime targets:
  Vectorization and recycling, missing values, type coercion, environments, lazy
  evaluation, package resolution. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: reproducibility, native libraries,
  numerical behavior, parallelism, data size. Exercise boundary values,
  encoding, cancellation, resource exhaustion, concurrency, dependency failure,
  and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which R version, package snapshot, operating system, locale, and data-size
  assumptions apply?
- How are missing values, factors, copy behavior, randomness, encoding, and
  statistical assumptions validated?

## Calibrate findings

- Treat silently incorrect analysis, unreproducible regulated output, or memory
  failure on required data scale as critical.
- Downgrade when output is exploratory and labeled or package, seed, locale,
  data-quality, and scale evidence are complete.

## Add to the verdict

State environment reproducibility, data assumptions, statistical validity
limits, memory and execution model, and evidence from representative data.
