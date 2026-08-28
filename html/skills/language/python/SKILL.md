---
name: python
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Python plans and other engineering artifacts for packaging, runtime, typing, concurrency, resource management, dependency, and test risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Python code, artifacts, or runtime behavior."
---

# Python GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read `pyproject.toml`, lockfiles, supported Python versions, entry points,
  framework configuration, type-checker settings, and representative tests.

- Trace sync and async boundaries, database or network clients, background work,
  process models, and shutdown behavior.

Watch especially for mutable default arguments, late-bound closures, blocking
work inside an event loop, imports with environment-dependent side effects,
typing treated as runtime enforcement, process and thread assumptions hidden by
the GIL, unsafe object deserialization, shell interpolation, archive extraction,
and packaging that imports a different project copy.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsafe deserialization, event-loop blocking, process-unsafe state, or
  incompatible package resolution as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/async-processes-and-shutdown.md):
  Read when the reviewed work directly or indirectly changes an event loop, async
  framework, threads, processes,
  executors, workers, GIL assumptions, task ownership, cancellation, signals, fork
  behavior, cleanup, retries, or graceful shutdown.
- [Focused rules](references/serialization-execution-and-filesystem-security.md):
  Read when the reviewed work directly or indirectly handles untrusted pickle, marshal,
  shelve, YAML, dynamic import,
  eval, exec, templates, subprocesses, paths, symlinks, archives, decompression, XML,
  images, regexes, or other attacker-controlled parsing.
- [Focused rules](references/packaging-native-and-deployment.md):
  Read when the reviewed work directly or indirectly changes interpreter implementation
  or version, packaging, lock or
  resolver tooling, imports, optional dependencies, virtual environments, generated
  files, native extensions, OS or architecture targets, build artifacts, or deployment
  environment behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the supported Python/runtime assumptions, the concurrency model, the
resource lifecycle, and the exact checks that prove the package and deployment
remain compatible.
