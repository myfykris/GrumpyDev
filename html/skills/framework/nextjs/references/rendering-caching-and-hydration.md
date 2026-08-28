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

- Verify these behaviors through the actual Next.js lifecycle and production
  pipeline: App and pages routers, server and client components, rendering and
  caching modes, actions, middleware. Use the actual framework pipeline and
  production build with representative services and configuration.


## Ask when evidence is missing

- Which Next.js, React, router, rendering mode, cache mode, and deployment
  runtime apply?
