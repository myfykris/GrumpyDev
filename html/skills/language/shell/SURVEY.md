# Shell survey contribution

## Applies when

Apply this contribution when the project contains or executes POSIX shell or Bash
scripts, build steps, deployment scripts, or operational automation.

## Inspect

- Read the declared shell, shebangs, strict-mode settings, target operating
  systems, command dependencies, environment assumptions, and tests.

## Ask when unresolved

- Which shell implementations, operating systems, utilities, locales, and
  privilege contexts must the script support?

- How do quoting, word splitting, globbing, pipelines, temporary files,
  signals, errors, and encoding cross boundaries?

- Which runtime or deployment differences materially change future reviews:
  Exact shell and utilities, OS or container image, locale and encoding, user
  and privileges, non-interactive environment, filesystem, service manager, and
  scheduler?

## Record

Map durable Shell version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
