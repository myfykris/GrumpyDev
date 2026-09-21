# C# full-review guidance

## Operating conditions

Establish the project target: Target frameworks, runtime and SDK versions, OS
targets, nullable mode, server or desktop model, trimming or AOT, deployment
mode, and native dependencies. The changed boundary must define: Language and
.NET semantics, nullability, async and cancellation, dependency injection
lifetimes, GC, threading, reflection, serialization, interop, trimming, AOT, and
deployment.

## Failure patterns

- Reject sync-over-async, unobserved tasks, missing cancellation,
  fire-and-forget work without ownership, and scope leakage into singletons.
- Require deterministic disposal for streams, database contexts, timers,
  subscriptions, and native handles.
- Check nullable assumptions, reflection, dynamic access, source generation,
  trimming, and ahead-of-time publishing against the selected runtime.
- Verify serialization and API compatibility across rolling deployments and
  independently versioned consumers.
- Reject unsafe legacy object serializers and unrestricted polymorphic type
  activation for untrusted data. Use explicit data contracts, bounded depth and
  size, and an allowlist only when polymorphism is actually required.
- Disable XML DTD and external resource resolution where untrusted XML can
  enter. Apply equivalent restrictions to archives, images, documents,
  templates, and any parser that can access files or networks.
- Keep untrusted values out of dynamic code, reflection-based type names,
  template source, and shell command strings. Use separated process arguments,
  validate option-like values, constrain paths, and set regular-expression
  timeouts for attacker-controlled input.
- Require tests for host shutdown, dependency failures, concurrency, culture,
  time, and publish-mode behavior.

## Verification to run or specify in the plan

- Run the published application with the selected target framework and
  deployment settings. If trimming or AOT is enabled, exercise reflection,
  serializers, generated code, and native interop in that artifact.
- Cancel and fail asynchronous operations while scopes are being disposed.
  Verify task failures are observed, scoped services do not outlive their
  owners, and streams, contexts, timers, and native handles are released.

- Exercise hostile type metadata, external XML references, archive traversal,
  command options, expensive regular expressions, deep input, and parser limits
  where those boundaries exist.
