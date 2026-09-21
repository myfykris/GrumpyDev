---
name: gd-python
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Python engineering work for packaging, runtime, typing, concurrency, resource management, dependency, and test risks."
---

# Python GrumpyDev review

## Quick checks

- Read `pyproject.toml`, lockfiles, supported Python versions, entry points,
  framework configuration, type-checker settings, and representative tests.

- Trace sync and async boundaries, database or network clients, background work,
  process models, and shutdown behavior.

Watch especially for mutable default arguments, late-bound closures, blocking
work inside an event loop, imports with environment-dependent side effects,
typing treated as runtime enforcement, process and thread assumptions hidden by
the GIL, unsafe object deserialization, shell interpolation, archive extraction,
and packaging that imports a different project copy.

- Assess unsafe deserialization, event-loop blocking, process-unsafe state, or
  incompatible package resolution under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Python specialist.

- [Focused rules](references/async-processes-and-shutdown.md):
  Read when the work changes an event loop, async
  framework, threads, processes,
  executors, workers, GIL assumptions, task ownership, cancellation, signals, fork
  behavior, cleanup, retries, or graceful shutdown.
- [Focused rules](references/serialization-execution-and-filesystem-security.md):
  Read when the work handles untrusted pickle, marshal,
  shelve, YAML, dynamic import,
  eval, exec, templates, subprocesses, paths, symlinks, archives, decompression, XML,
  images, regexes, or other attacker-controlled parsing.
- [Focused rules](references/packaging-native-and-deployment.md):
  Read when the work changes interpreter implementation
  or version, packaging, lock or
  resolver tooling, imports, optional dependencies, virtual environments, generated
  files, native extensions, OS or architecture targets, build artifacts, or deployment
  environment behavior.

## Verdict context

State the supported Python/runtime assumptions, the concurrency model, the
resource lifecycle, and the exact checks that prove the package and deployment
remain compatible.
