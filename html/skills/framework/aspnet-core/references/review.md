# ASP.NET Core standard review

## Inspect additional evidence

- Trace request cancellation, scoped resources, background services, streaming,
  exception handling, forwarded headers, and shutdown.

## Establish the operating model

Establish the project target: .NET and ASP.NET Core versions, hosting model,
reverse proxy, authentication scheme, data providers, deployment mode, trimming
or AOT, and worker services. The changed boundary must define: Middleware
ordering, DI lifetimes, async and cancellation, model binding, authentication
and authorization, configuration, EF boundaries, hosted services, Kestrel, and
graceful shutdown.

Assign lifecycle, state, dependency, persistence, and security ownership for
Middleware ordering, DI lifetimes, async and cancellation, model binding,
authentication and authorization. Prove configuration, EF boundaries, hosted
services, Kestrel, graceful shutdown through startup, invalid or denied work,
cancellation, background execution, mixed versions, shutdown, rollback, and
recovery.

## Challenge the reviewed work

### Recurring traps

- Verify middleware order for routing, forwarded headers, authentication,
  authorization, CORS, exceptions, and response transforms.
- Reject singleton capture of scoped services and require correct disposal and
  cancellation across requests and hosted work.
- Check over-posting, validation, serializer defaults, body limits, antiforgery,
  authorization policies, and error-detail exposure.
- Require bounded background queues and explicit ownership instead of starting
  untracked work from request handlers.
- Test behind the real reverse proxy and deployment model for path base, scheme,
  client address, draining, health, and rolling upgrades.

## Verify the claims

- Verify these behaviors through the actual ASP.NET Core lifecycle and
  production pipeline: Middleware ordering, DI lifetimes, async and
  cancellation, model binding, authentication and authorization. Use the actual
  framework pipeline and production build with representative services and
  configuration.
- Exercise failure and edge behavior for: configuration, EF boundaries, hosted
  services, Kestrel, graceful shutdown. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which .NET, C#, ASP.NET Core, hosting, server, and deployment versions or
  modes apply?
- How are middleware order, dependency lifetimes, authentication, cancellation,
  errors, and shutdown handled?

## Calibrate findings

- Downgrade when pipeline order, lifetimes, policies, and hosted-service
  behavior are proven by integration tests.
