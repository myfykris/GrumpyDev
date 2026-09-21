# React server rendering and hydration

Read this reference when the reviewed work directly or indirectly changes server
rendering, server components,
hydration, streaming, Suspense across a server boundary, serialized initial data, or
browser and server execution differences.

## Review requirements

- Check hydration and serialization assumptions when server rendering or server
  components apply. Identify browser-only APIs and time/randomness differences.

## Verify the claims

- Hydrate the server-rendered output with different time zones, delayed data,
  and browser-only dependencies where relevant. Check mismatches, fallback
  transitions, and early user input during hydration.
- Inspect serialized initial data and streamed output for unintended
  disclosure. Verify interrupted or failed server rendering leaves usable
  error or retry behavior in the actual framework build.

## Ask when evidence is missing

- Who owns server data, URL state, form state, effects, hydration, errors, and
  accessibility behavior?
