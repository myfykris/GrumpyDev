# Ruby full-review guidance

## Operating conditions

Establish the project target: Ruby implementation and version, web and job
servers, concurrency model, Bundler and lock policy, native extensions, OS
targets, preload and worker model, and deployment packaging. The changed
boundary must define: Object model, blocks, exceptions, fibers, threads and
Ractors, GVL implications, metaprogramming, autoloading, gems, serialization,
GC, web and job lifecycles, and native extensions.

## Failure patterns

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

## Verification to run or specify in the plan

- Boot the packaged application with its locked gems and native extensions
  under the production Ruby implementation and server model. Exercise eager
  loading, constant lookup, and worker startup without development reload
  behavior.
- Run concurrent requests or jobs that touch shared class state; fail
  callbacks and interrupt workers mid-operation. Verify resource cleanup and
  that retries do not repeat committed effects.

- Exercise malicious YAML and Marshal data, dynamic names, command options,
  archive traversal, symlink swaps, expensive regular expressions, and parser
  limits where those boundaries exist.
