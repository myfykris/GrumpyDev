# R survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with R code, artifacts, or runtime behavior.

## Inspect

- Read package metadata, lockfiles, session information, data schemas,
  statistical assumptions, native dependencies, pipeline definitions, and
  representative tests.

## Ask when unresolved

- Which R version, package snapshot, operating system, locale, and data-size
  assumptions apply?

- How are missing values, factors, copy behavior, randomness, encoding, and
  statistical assumptions validated?

- Which runtime or deployment differences materially change future reviews: R
  version, package snapshot, native libraries, batch or interactive runtime,
  scheduler, worker topology, memory limits, compute platform, and
  reproducibility environment?

## Record

Map durable R version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
