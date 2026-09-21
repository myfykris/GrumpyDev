# Dart full-review guidance

## Operating conditions

Establish the project target: Dart SDK range, target platforms, JIT or AOT mode,
package and code-generation tools, isolate use, native dependencies, and
deployment packaging. The changed boundary must define: Sound null safety, async
scheduling, isolates, streams, package resolution, code generation, FFI, runtime
and compilation modes, resource cleanup, and platform differences.

## Failure patterns

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

## Verification to run or specify in the plan

- Run the built output on the project's actual VM, web, or native targets.
  If serializers are generated, regenerate them and check malformed data and
  missing fields. Exercise native calls where platform behavior changes the
  contract.
- Cancel stream subscriptions and terminate owned isolates during pending
  work. Verify errors remain observable and controllers, timers, and native
  resources are released after the owner is disposed.
