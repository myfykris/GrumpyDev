---
name: gd-aspnet-core
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review ASP.NET Core engineering work for middleware order, dependency lifetimes, request cancellation, model binding, authorization, hosting, serialization, and deployment risks."
---

# ASP.NET Core GrumpyDev review

## Quick checks

- Establish the exact .NET, C#, ASP.NET Core, server, and hosting versions or
  modes.

- Read host construction, middleware and endpoint order, service registrations,
  authentication and authorization policies, model binding, options, hosting,
  and tests.

Watch especially for middleware in the wrong order, scoped services captured by
singletons, sync-over-async thread-pool starvation, untrusted forwarded headers,
and startup migrations that make every application instance race for schema
ownership.

- Assess authorization bypass, captive dependencies, lost cancellation, or unsafe
  shutdown on a critical service under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the ASP.NET Core
specialist.

## Verdict context

State middleware and DI contracts, request and background-work ownership,
binding and authorization boundaries, hosting assumptions, and deployed
evidence.
