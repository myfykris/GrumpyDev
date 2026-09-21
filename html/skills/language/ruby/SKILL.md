---
name: gd-ruby
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Ruby engineering work for runtime compatibility, metaprogramming, object mutability, concurrency, dependency resolution, resource lifecycle, serialization, and deployment risks."
---

# Ruby GrumpyDev review

## Quick checks

- Read gem metadata, lockfiles, Ruby version files, native extensions, autoload
  configuration, process and worker settings, and representative tests.

- Trace threads or fibers, global and class state, callbacks, transactions,
  resources, serialization, and application boot or reload behavior.

Watch especially for nil and truthiness assumptions, broad monkey patches,
blocks or fibers outliving captured state, enumerators evaluated later than
expected, autoload differences between development and production, mutable
objects used as stable identity, unsafe object loading, dynamic constant or
method selection, shell interpolation, and thread safety hidden by one runtime.

- Assess unsafe shared state, swallowed critical exceptions, unsafe
  deserialization, or runtime incompatibility under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Ruby specialist.

## Verdict context

State Ruby and process targets, concurrency model, dynamic behavior risks,
dependency compatibility, lifecycle guarantees, and deployment evidence.
