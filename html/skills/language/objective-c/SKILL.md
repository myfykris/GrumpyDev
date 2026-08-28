---
name: objective-c
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Objective-C plans and other engineering artifacts for runtime dispatch, object ownership, nullability, blocks, categories, KVO, interoperability, ABI, and concurrency risks. Project applicability: the project contains or builds Objective-C or Objective-C++ source, exposes an Objective-C ABI, or has generated bindings or a bridge whose correctness depends on Objective-C runtime semantics. Apple frameworks or a Swift-only Apple application do not make this specialist applicable by themselves."
---

# Objective-C GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `c`, `cpp`,
`swift`, `macos`, and applicable Apple UI framework skills. Every installed
companion that remains applicable to the project participates; the reviewed
target does not select the roster. Verify behavior against the project's
declared targets; do not silently substitute the newest version, a development
default, or a neighboring product's semantics.

## Lean review

- Inspect compiler and target settings, headers, module maps, ownership
  annotations, bridging headers, categories, blocks, observers, native
  boundaries, and build products.

- Read the declarations and produced binaries in addition to source. Compiler
  defaults, language modes, optimization, architecture, linker behavior, and
  foreign dependencies are part of the program.

Watch especially for messages to nil masking missing work, selector-based
behavior escaping compiler checks, retain cycles through blocks or delegates,
KVO and notification teardown, Core Foundation bridging ownership, exceptions
crossing language boundaries, and Objective-C++ ABI assumptions.

Lean mode is insufficient when this material severity condition may apply:

- Treat memory corruption, use-after-free, ABI breakage, cross-thread UI access,
  or an ownership error that can corrupt persistent state as critical or high
  according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/dynamic-runtime-kvo-and-notifications.md):
  Read when the reviewed work directly or indirectly changes selectors, forwarding,
  swizzling, categories, associated
  objects, runtime registration, KVO, notifications, observer lifetime, reentrancy, or
  dynamic callback ordering.
- [Focused rules](references/swift-c-cpp-and-abi-interop.md):
  Read when the reviewed work directly or indirectly crosses Core Foundation, Swift, C,
  C++, Objective-C++, native
  callbacks, exception boundaries, modules, symbols, method signatures, architecture
  slices, or ABI and binary compatibility.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
runtime messaging, ARC and manual ownership boundaries, nullability, categories,
blocks, KVO and notifications, Swift bridging, C and C++ interoperability,
exceptions, ABI, and concurrency, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
