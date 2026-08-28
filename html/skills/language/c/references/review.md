# C standard review

## Establish the operating model

Establish the project target: C standard and extensions, compilers and versions,
targets and architectures, ABI and libc, build profiles, required warnings,
sanitizers, and supported operating systems. The changed boundary must define:
Language standard, compiler behavior, undefined behavior, object lifetime,
memory ownership, integer rules, ABI, linkage, FFI, concurrency, signals, build
flags, sanitizers, and platform portability.

Define ownership, errors, cancellation, and concurrency for Language standard,
compiler behavior, undefined behavior, object lifetime, memory ownership,
integer rules, ABI. Verify version, package, native, serialization, and artifact
compatibility for linkage, FFI, concurrency, signals, build flags, sanitizers,
platform portability across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

- Require one explicit owner and cleanup path for every allocation, descriptor,
  handle, lock, and callback context.
- Check integer conversion, pointer arithmetic, alignment, aliasing, signed
  overflow, initialization, and buffer-length assumptions for undefined
  behavior.
- Verify public struct layout, calling convention, symbol visibility, and
  versioning across every supported compiler and consumer.
- Reject error handling that loses the original failure, leaks partial state, or
  continues after an invariant is broken.
- Require sanitizer, static-analysis, fuzz, and target-specific tests
  proportional to the input and memory risk.

## Verify the claims

- Verify these behaviors through the declared C compiler and runtime targets:
  Language standard, compiler behavior, undefined behavior, object lifetime,
  memory ownership, integer rules, ABI. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: linkage, FFI, concurrency, signals,
  build flags, sanitizers, platform portability. Exercise boundary values,
  encoding, cancellation, resource exhaustion, concurrency, dependency failure,
  and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which C standard, compiler, target ABI, operating system, and build flags
  define the program?
- Who owns each allocation, buffer, file descriptor, thread, and error path
  across the changed boundary?

## Calibrate findings

- Downgrade when inputs and lifetimes are bounded and sanitizers, static
  analysis, and target-specific tests cover the path.
