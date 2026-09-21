---
name: gd-nestjs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review NestJS engineering work for module boundaries, provider scope, dependency cycles, validation, guards, interceptors, asynchronous work, and deployment risks."
---

# NestJS GrumpyDev review

## Quick checks

- Establish the exact Node.js, NestJS, TypeScript, adapter, transport, and
  deployment versions.

- Read modules, imports and exports, provider scopes, controllers, pipes,
  guards, interceptors, exception filters, transport setup, and tests.

Watch especially for provider-scope mistakes, circular dependencies hidden by
forward references, guard and interceptor ordering, validation transforms that
coerce hostile input, lifecycle hooks that do not await completion, and
request-scoped providers multiplying cost.

- Assess guard bypass, request data in singleton state, or transport retries
  causing irreversible effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the NestJS specialist.

## Verdict context

State module and provider ownership, validation and authorization pipeline,
initialization and shutdown behavior, transport guarantees, and built-runtime
evidence.
