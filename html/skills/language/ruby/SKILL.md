---
name: ruby
description: Review Ruby engineering plans for runtime compatibility, metaprogramming, object mutability, concurrency, dependency resolution, resource lifecycle, serialization, and deployment risks. Use when a plan changes Ruby applications, gems, workers, scripts, or services.
---

# Ruby plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read gem metadata, lockfiles, Ruby version files, native extensions, autoload
  configuration, process and worker settings, and representative tests.
- Trace threads or fibers, global and class state, callbacks, transactions,
  resources, serialization, and application boot or reload behavior.

## Establish the operating model

Establish the project target: Ruby implementation and version, web and job
servers, concurrency model, Bundler and lock policy, native extensions, OS
targets, preload and worker model, and deployment packaging. The changed
boundary must define: Object model, blocks, exceptions, fibers, threads and
Ractors, GVL implications, metaprogramming, autoloading, gems, serialization,
GC, web and job lifecycles, and native extensions.

Define ownership, errors, cancellation, and concurrency for Object model,
blocks, exceptions, fibers, threads and Ractors, GVL implications,
metaprogramming. Verify version, package, native, serialization, and artifact
compatibility for autoloading, gems, serialization, GC, web and job lifecycles,
native extensions across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for nil and truthiness assumptions, broad monkey patches,
blocks or fibers outliving captured state, enumerators evaluated later than
expected, autoload differences between development and production, mutable
objects used as stable identity, unsafe object loading, dynamic constant or
method selection, shell interpolation, and thread safety hidden by one runtime.

- Check monkey patches, callbacks, dynamic dispatch, autoloading, and constant
  resolution for order-dependent behavior.
- Require explicit ownership for threads, fibers, connections, files, and
  background work across shutdown and reload.
- Verify mutable default objects, shared class state, thread safety, and request
  assumptions under the actual server and worker model.
- Check gem and native-extension compatibility across development, CI, build
  images, and production Ruby versions.
- Reject `Marshal.load`, unrestricted YAML object loading, and equivalent object
  deserialization for untrusted data. Use explicit data schemas and allow only
  the scalar and collection types the boundary requires.
- Keep untrusted values out of `eval`, dynamic constant lookup, unrestricted
  method dispatch, template source, and shell command strings. Use fixed
  operations and separated arguments with explicit option policy.
- Constrain paths, temporary files, symlinks, archives, decompression, parser
  depth, collection size, and regular-expression work before allocation or
  execution.
- Demand tests for transactions, retries, partial callbacks, serialization
  changes, time zones, and deployed boot behavior.

## Verify the claims

- Verify these behaviors through the declared Ruby compiler and runtime targets:
  Object model, blocks, exceptions, fibers, threads and Ractors, GVL
  implications, metaprogramming. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: autoloading, gems, serialization, GC,
  web and job lifecycles, native extensions. Exercise boundary values, encoding,
  cancellation, resource exhaustion, concurrency, dependency failure, and
  termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise malicious YAML and Marshal data, dynamic names, command options,
  archive traversal, symlink swaps, expensive regular expressions, and parser
  limits where those boundaries exist.

## Ask when evidence is missing

- Which Ruby version and implementation, thread and process model, native
  extensions, and gem versions apply?
- How do mutable state, blocks, exceptions, fibers, threads, resources, and
  serialization cross the boundary?

## Calibrate findings

- Treat unsafe shared state, swallowed critical exceptions, unsafe
  deserialization, or runtime incompatibility as critical.
- Downgrade when the process model is bounded and concurrency, exception,
  resource, and version tests cover the path.

## Add to the verdict

State Ruby and process targets, concurrency model, dynamic behavior risks,
dependency compatibility, lifecycle guarantees, and deployment evidence.
