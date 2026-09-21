# Next.js rendering, caching, and hydration

Read this reference when the reviewed work directly or indirectly changes server or
client components, App or Pages
Router rendering, static or dynamic rendering, streaming, Suspense, hydration, fetch
caching, cache keys, tags, revalidation, personalization, or stale behavior.

## Review requirements

- Define cache scope, key, lifetime, invalidation, personalization, and stale
  behavior for every cached read or rendered route.

- Keep cache keys, tags, revalidation paths, and rendered output within the
  current identity and tenant boundary. Do not let user input invalidate
  arbitrary content or let privileged fetch results enter a public cache.

- Check Node versus edge runtime APIs, streaming, dynamic rendering triggers,
  middleware limits, and deployment-specific behavior.

## Verify the claims

- Serve the production build and request the same route as different users,
  tenants, and anonymous visitors. Verify cache hits, expiration, and
  revalidation preserve the declared identity boundary.
- Exercise direct loads and client navigation with slow data and stale
  content. Check streaming, hydration, and cache behavior under the actual
  router, runtime, and deployment settings.

## Ask when evidence is missing

- Which Next.js, React, router, rendering mode, cache mode, and deployment
  runtime apply?
