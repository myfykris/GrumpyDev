# C survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with C code, artifacts, or runtime behavior.

## Inspect

- Read build files, compiler flags, target platforms, public headers, allocation
  conventions, sanitizer settings, and representative tests.

## Ask when unresolved

- Which C standard, compiler, target ABI, operating system, and build flags
  define the program?

- What ownership rules apply to allocations, buffers, file descriptors,
  threads, and error handling at project interfaces?

- Which runtime or deployment differences materially change future reviews:
  Target OS, architecture, ABI, libc, compiler, dynamic libraries, privilege,
  packaging, and process or embedded environment?

## Record

Map durable C version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
