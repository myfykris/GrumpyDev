# ASP.NET Core full-review guidance

## Operating conditions

Establish the project target: .NET and ASP.NET Core versions, hosting model,
reverse proxy, authentication scheme, data providers, deployment mode, trimming
or AOT, and worker services. The changed boundary must define: Middleware
ordering, DI lifetimes, async and cancellation, model binding, authentication
and authorization, configuration, EF boundaries, hosted services, Kestrel, and
graceful shutdown.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise protected endpoints through the configured routing, proxy-header,
  authentication, and authorization middleware. Send privileged extra fields
  and malformed input to check model binding and error disclosure.
- Cancel requests and stop the host with scoped services and background work
  active. Verify disposal, bounded queues, readiness changes, and draining
  under the deployed Kestrel and proxy settings.
