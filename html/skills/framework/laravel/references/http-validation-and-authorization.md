# Laravel HTTP, validation, and authorization

Read this reference when the reviewed work directly or indirectly changes routes,
middleware, request validation, route
model binding, guards, providers, policies, gates, CSRF, signed URLs, rate limits,
trusted proxies, API resources, JSON output, pagination, or HTTP error behavior.

## HTTP, validation, and authorization

- Require input validation at the request boundary and domain invariants at the
  operation that changes state. Form requests and DTOs do not replace
  authorization or database constraints.
- Verify middleware ordering, route model binding, implicit scoping, guard and
  provider selection, authentication state, CSRF behavior, signed URLs, rate
  limits, and trusted proxy configuration for the actual route group.
- Require policies, gates, or an equivalent explicit authorization decision for
  the specific object and action. Hidden fields, route middleware, tenant query
  scopes, and controller placement are not sufficient authorization by
  themselves.
- Check API resources, JSON serialization, appended attributes, relations,
  visibility, pagination, and error responses for accidental data exposure or
  unstable contracts.

## Verify the claims

- Use feature tests that cross real middleware, route binding, validation,
  authorization, container, database, event, and serialization boundaries. Unit
  tests around controller methods do not prove the framework pipeline.
