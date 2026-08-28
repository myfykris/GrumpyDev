# C# standard review

## Establish the operating model

Establish the project target: Target frameworks, runtime and SDK versions, OS
targets, nullable mode, server or desktop model, trimming or AOT, deployment
mode, and native dependencies. The changed boundary must define: Language and
.NET semantics, nullability, async and cancellation, dependency injection
lifetimes, GC, threading, reflection, serialization, interop, trimming, AOT, and
deployment.

Define ownership, errors, cancellation, and concurrency for Language and .NET
semantics, nullability, async and cancellation, dependency injection lifetimes,
GC, threading. Verify version, package, native, serialization, and artifact
compatibility for reflection, serialization, interop, trimming, AOT, deployment
across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared C# compiler and runtime targets:
  Language and .NET semantics, nullability, async and cancellation, dependency
  injection lifetimes, GC, threading. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: reflection, serialization, interop,
  trimming, AOT, deployment. Exercise boundary values, encoding, cancellation,
  resource exhaustion, concurrency, dependency failure, and termination where
  they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise hostile type metadata, external XML references, archive traversal,
  command options, expensive regular expressions, deep input, and parser limits
  where those boundaries exist.

## Ask when evidence is missing

- Which C# language, .NET runtime, nullable context, target framework, and
  deployment versions apply?
- How do async cancellation, disposal, dependency lifetime, serialization, and
  concurrency cross the changed boundary?

## Calibrate findings

- Downgrade when lifetimes are bounded and nullable, cancellation, disposal, and
  runtime-version tests cover the path.
