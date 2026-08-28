# React server rendering and hydration

Read this reference when the reviewed work directly or indirectly changes server
rendering, server components,
hydration, streaming, Suspense across a server boundary, serialized initial data, or
browser and server execution differences.

## Review requirements

- Check hydration and serialization assumptions when server rendering or server
  components apply. Identify browser-only APIs and time/randomness differences.

## Verify the claims

- Verify these behaviors through the actual React lifecycle and production
  pipeline: Render purity, state ownership, effects, concurrency, transitions,
  suspense, server rendering. Use the actual framework pipeline and production
  build with representative services and configuration.


## Ask when evidence is missing

- Who owns server data, URL state, form state, effects, hydration, errors, and
  accessibility behavior?
