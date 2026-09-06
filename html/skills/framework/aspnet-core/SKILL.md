---
name: aspnet-core
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review ASP.NET Core engineering work for middleware order, dependency lifetimes, request cancellation, model binding, authorization, hosting, serialization, and deployment risks."
---

# ASP.NET Core GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `csharp` skill.

## Lean review

- Establish the exact .NET, C#, ASP.NET Core, server, and hosting versions or
  modes.

- Read host construction, middleware and endpoint order, service registrations,
  authentication and authorization policies, model binding, options, hosting,
  and tests.

Watch especially for middleware in the wrong order, scoped services captured by
singletons, sync-over-async thread-pool starvation, untrusted forwarded headers,
and startup migrations that make every application instance race for schema
ownership.

Lean mode is insufficient when this material severity condition may apply:

- Treat authorization bypass, captive dependencies, lost cancellation, or unsafe
  shutdown on a critical service as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete ASP.NET Core evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State middleware and DI contracts, request and background-work ownership,
binding and authorization boundaries, hosting assumptions, and deployed
evidence.
