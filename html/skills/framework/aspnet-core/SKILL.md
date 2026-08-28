---
name: aspnet-core
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review ASP.NET Core plans and other engineering artifacts for middleware order, dependency lifetimes, request cancellation, model binding, authorization, hosting, serialization, and deployment risks. Project applicability: the project uses or materially depends on ASP.NET Core."
---

# ASP.NET Core GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
