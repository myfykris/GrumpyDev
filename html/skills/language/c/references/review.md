# C full-review guidance

## Operating conditions

Establish the project target: C standard and extensions, compilers and versions,
targets and architectures, ABI and libc, build profiles, required warnings,
sanitizers, and supported operating systems. The changed boundary must define:
Language standard, compiler behavior, undefined behavior, object lifetime,
memory ownership, integer rules, ABI, linkage, FFI, concurrency, signals, build
flags, sanitizers, and platform portability.

## Failure patterns

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

## Verification to run or specify in the plan

- Compile with the supported standards, warnings, optimization levels, and
  target ABIs. Exercise allocation failure, integer boundaries, partial
  cleanup, and malformed buffers with suitable sanitizers or fuzzing.
- For a changed public binary interface, link and run a consumer against the
  built library on each supported ABI; check struct layout, calling
  convention, and exported symbols.
