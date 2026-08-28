# Objective-C Swift, C, C++, and ABI interop

Read this reference when the reviewed work directly or indirectly crosses Core
Foundation, Swift, C, C++, Objective-C++,
native callbacks, exception boundaries, modules, symbols, method signatures,
architecture slices, or ABI and binary compatibility.

## Review requirements

- Follow ownership across Core Foundation, Objective-C, C++, blocks, callbacks,
  autorelease pools, weak references, and asynchronous work. Bridging syntax
  does not by itself prove which side owns a value.

- Keep Objective-C exceptions out of ordinary recoverable control flow and
  define how C++, Swift, C callbacks, and error-return conventions cross the
  boundary without unwinding through an incompatible ABI.

- Validate method signatures, lightweight generics, modules, symbols, deployment
  availability, architecture slices, and Swift import names across every shipped
  binary.

## Verify the claims

- Inspect the produced symbols, modules, architecture slices, entitlements, and
  minimum operating-system metadata.
