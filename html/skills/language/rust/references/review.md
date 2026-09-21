# Rust full-review guidance

## Operating conditions

Establish the project target: Rust edition, MSRV and toolchain channel, targets,
async runtime, feature sets, panic strategy, unsafe policy, FFI and native
dependencies, allocator, and no_std use. The changed boundary must define:
Ownership and lifetime boundaries, unsafe code, pinning, async runtimes, Send
and Sync, atomics, panic behavior, feature flags, MSRV, FFI, allocators, no_std,
and cross-compilation.

## Failure patterns

- Require every unsafe block or unsafe impl to state and preserve the invariant
  that makes it sound.
- Check async task ownership, cancellation safety, blocking calls, runtime
  nesting, channel bounds, and graceful shutdown.
- Verify feature unification, optional dependencies, build scripts, and
  target-specific code across every supported build combination.
- Define panic policy and prevent unwinding across FFI or process boundaries
  where it is unsupported.
- Demand Miri, sanitizer, loom, fuzz, or target tests when ordinary unit tests
  cannot exercise memory or concurrency invariants.

## Verification to run or specify in the plan

- Build the declared MSRV, targets, and supported feature combinations,
  including no_std or native dependencies where used. Exercise the selected
  panic strategy at FFI boundaries without relying on unsupported unwinding.
- Cancel futures while they own resources or have partially changed state. Use
  Miri, sanitizers, concurrency modeling, or fuzzing where supported to
  challenge the specific unsafe or synchronization invariant.
