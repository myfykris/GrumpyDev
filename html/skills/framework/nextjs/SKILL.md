---
name: gd-nextjs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Next.js engineering work for server and client boundaries, caching, rendering mode, routing, data mutation, runtime selection, authentication, and deployment risks."
---

# Next.js GrumpyDev review

## Quick checks

- Read Next.js and React versions, app or pages router, route configuration,
  server and client components, caching directives, middleware, runtime targets,
  and tests.

- Trace data reads and mutations through rendering, caches, revalidation,
  cookies, authentication, navigation, streaming, and deployment.

Watch especially for server and client boundaries crossed accidentally, stale or
over-broad cache and revalidation behavior, route runtimes that lack required
APIs, secrets included in client bundles, hydration differences, and build-time
data assumed to remain current. Also watch for server actions treated as private
functions, user-specific results entering shared caches, and remote fetch or
redirect input becoming an SSRF or open-redirect path.

- Assess server-only data exposure, cache leakage across users, or unsafe
  mutation authorization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Next.js specialist.

- [Focused rules](references/rendering-caching-and-hydration.md):
  Read when the work changes server or client
  components, App or Pages Router rendering,
  static or dynamic rendering, streaming, Suspense, hydration, fetch caching, cache
  keys, tags, revalidation, personalization, or stale behavior.
- [Focused rules](references/server-actions-routes-and-security.md):
  Read when the work changes server actions, route
  handlers, middleware, authentication,
  authorization, CSRF behavior, remote fetches, image or metadata URLs, redirects,
  rewrites, preview access, environment exposure, or server-to-client serialization.

## Verdict context

State rendering and runtime modes, server-client trust boundary, route and
action authorization, cache and revalidation scope, outbound fetch policy,
mutation contracts, authentication behavior, and production evidence.
