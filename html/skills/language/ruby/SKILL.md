---
name: ruby
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Ruby plans and other engineering artifacts for runtime compatibility, metaprogramming, object mutability, concurrency, dependency resolution, resource lifecycle, serialization, and deployment risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Ruby code, artifacts, or runtime behavior."
---

# Ruby GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read gem metadata, lockfiles, Ruby version files, native extensions, autoload
  configuration, process and worker settings, and representative tests.

- Trace threads or fibers, global and class state, callbacks, transactions,
  resources, serialization, and application boot or reload behavior.

Watch especially for nil and truthiness assumptions, broad monkey patches,
blocks or fibers outliving captured state, enumerators evaluated later than
expected, autoload differences between development and production, mutable
objects used as stable identity, unsafe object loading, dynamic constant or
method selection, shell interpolation, and thread safety hidden by one runtime.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsafe shared state, swallowed critical exceptions, unsafe
  deserialization, or runtime incompatibility as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Ruby evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State Ruby and process targets, concurrency model, dynamic behavior risks,
dependency compatibility, lifecycle guarantees, and deployment evidence.
