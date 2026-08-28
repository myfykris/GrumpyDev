# Next.js server actions, routes, and security

Read this reference when the reviewed work directly or indirectly changes server
actions, route handlers, middleware,
authentication, authorization, CSRF behavior, remote fetches, image or metadata URLs,
redirects, rewrites, preview access, environment exposure, or server-to-client
serialization.

## Review requirements

- Treat server actions and route handlers as public endpoints with validation,
  object and action authorization, CSRF considerations, body and work limits,
  idempotency, safe errors, and audit behavior. Validate every invocation even
  when only generated client code is expected to call it.

- Constrain server-side fetches, image or metadata URLs, preview endpoints,
  redirects, rewrites, and callback destinations to approved schemes and
  origins. Apply the full SSRF policy before following redirects or returning
  fetched content.

- Treat middleware as an early filter, not the sole authorization boundary.
  Recheck permission at the route, action, resolver, or data operation that
  performs the sensitive effect.

- Audit values exposed through public environment variables, React Server
  Component serialization, page data, source maps, errors, and build output.

## Verify the claims

- Exercise failure and edge behavior for: route handlers, hydration, runtimes,
  assets, deployment. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.

- Call route handlers and server actions directly with missing, stale,
  cross-tenant, malformed, oversized, and duplicate input. Verify denial at the
  authoritative data or effect boundary.

- Exercise personalized cache reads, revalidation, redirects, remote fetches,
  preview or draft access, production error handling, and client bundle
  inspection with the deployed runtime configuration.


## Ask when evidence is missing

- Where do authentication, server actions, route handlers, revalidation,
  serialization, and client state cross boundaries?
