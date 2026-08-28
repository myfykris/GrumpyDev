# Rust standard review

## Inspect additional evidence

- Trace ownership across tasks, shared state, pinning, cancellation, blocking
  work, resource cleanup, panic boundaries, and foreign calls.

## Establish the operating model

Establish the project target: Rust edition, MSRV and toolchain channel, targets,
async runtime, feature sets, panic strategy, unsafe policy, FFI and native
dependencies, allocator, and no_std use. The changed boundary must define:
Ownership and lifetime boundaries, unsafe code, pinning, async runtimes, Send
and Sync, atomics, panic behavior, feature flags, MSRV, FFI, allocators, no_std,
and cross-compilation.

Define ownership, errors, cancellation, and concurrency for Ownership and
lifetime boundaries, unsafe code, pinning, async runtimes, Send and Sync,
atomics, panic behavior. Verify version, package, native, serialization, and
artifact compatibility for feature flags, MSRV, FFI, allocators, no_std,
cross-compilation across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared Rust compiler and runtime targets:
  Ownership and lifetime boundaries, unsafe code, pinning, async runtimes, Send
  and Sync, atomics, panic behavior. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: feature flags, MSRV, FFI, allocators,
  no_std, cross-compilation. Exercise boundary values, encoding, cancellation,
  resource exhaustion, concurrency, dependency failure, and termination where
  they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Rust edition, minimum supported Rust version, Cargo version, target
  toolchain, and feature set apply?
- Where do unsafe code, FFI, pinning, async cancellation, shared state, and
  resource lifetime cross the boundary?

## Calibrate findings

- Downgrade when the path is safe Rust or unsafe boundaries, features, MSRV,
  targets, and concurrency are tested.
