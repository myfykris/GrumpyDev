---
name: dart
description: Review Dart engineering plans for null safety, asynchronous execution, isolates, package compatibility, serialization, platform differences, and release-build risks. Use when a plan changes Dart packages, services, command-line tools, or Flutter application code.
---

# Dart plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read pubspec files, lockfiles, SDK constraints, analyzer settings, generated
  code configuration, platform targets, and representative tests.
- Trace futures, streams, isolates, cancellation or disposal, serialization,
  platform channels, and application lifecycle boundaries.

## Establish the operating model

Establish the project target: Dart SDK range, target platforms, JIT or AOT mode,
package and code-generation tools, isolate use, native dependencies, and
deployment packaging. The changed boundary must define: Sound null safety, async
scheduling, isolates, streams, package resolution, code generation, FFI, runtime
and compilation modes, resource cleanup, and platform differences.

Define ownership, errors, cancellation, and concurrency for Sound null safety,
async scheduling, isolates, streams, package resolution. Verify version,
package, native, serialization, and artifact compatibility for code generation,
FFI, runtime and compilation modes, resource cleanup, platform differences
across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for unawaited futures, errors escaping asynchronous zones,
stream subscriptions that are never cancelled, isolate messages that cannot
serialize or preserve identity, null-safety assumptions at dynamic boundaries,
and generated code drifting from its source declarations.

- Check late initialization, nullable state, unchecked casts, dynamic values,
  and generated serializers at runtime boundaries.
- Require ownership for subscriptions, controllers, timers, isolates, and
  asynchronous work during shutdown or widget disposal.
- Verify code generation and package versions are reproducible across developer,
  CI, and release environments.
- Test behavior on every supported platform instead of assuming VM, web, and
  native runtimes are equivalent.
- Demand release-mode tests where tree shaking, minification, platform
  permissions, or native plugins can change behavior.

## Verify the claims

- Verify these behaviors through the declared Dart compiler and runtime targets:
  Sound null safety, async scheduling, isolates, streams, package resolution.
  Use the real compiler or interpreter and supported release modes rather than a
  development substitute.
- Exercise failure and edge behavior for: code generation, FFI, runtime and
  compilation modes, resource cleanup, platform differences. Exercise boundary
  values, encoding, cancellation, resource exhaustion, concurrency, dependency
  failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Dart version, target runtime, null-safety mode, package constraints, and
  isolate model apply?
- How do futures, streams, cancellation, serialization, errors, and mutable
  state cross isolates or UI lifecycles?

## Calibrate findings

- Treat lost asynchronous errors, cross-isolate contract failure, or lifecycle
  work that corrupts durable state as critical.
- Downgrade when the target is bounded and analyzer, async, stream, and
  target-runtime tests cover the behavior.

## Add to the verdict

State the Dart and platform targets, async ownership, generated-code
assumptions, serialization boundaries, and release-mode evidence.
