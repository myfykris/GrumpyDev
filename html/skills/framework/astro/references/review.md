# Astro standard review

## Inspect additional evidence

- Trace cookies, sessions, secrets, content collections, endpoint code, middleware, assets, and
  cache behavior.
- Inspect client directives, server directives, adapter configuration, environment access, and
  production output.

## Establish the operating model

Establish the project target: Astro version, output mode, adapter and host, route rendering
choices, client frameworks, content sources, environment model, cache policy, and browser
targets.

The plan must distinguish build-time code, request-time server code, isolated client code, and
public serialized props. It must name which routes require a server and which remain deployable
as static files.

## Challenge the reviewed work

### Recurring traps

- Require an explicit hydration reason and loading directive for every client island.
- Verify that protected or personalized routes render on a trusted server boundary and
  authorize each request.
- Keep server-island inputs small and non-sensitive; account for fallback, delay, caching, and
  page URL differences.
- Require adapter-specific evidence for cookies, streaming, middleware, image handling,
  environment variables, and runtime APIs.
- Test direct navigation, history, no-JavaScript behavior, content build failures, and mixed
  static and dynamic routes.

## Verify the claims

- Build the actual static or server output and inspect emitted client JavaScript, routes,
  assets, and server entrypoints.
- Exercise direct requests, slow server islands, missing content, denied access, stale caches,
  and adapter-specific failures.
- Run representative production output on the selected adapter rather than treating the
  development server as evidence.

## Ask when evidence is missing

- Which Astro version, output mode, adapter, host, routes, and client integrations apply?
- Which data is fixed at build time, rendered per request, deferred in a server island, or
  hydrated in a client island?

## Calibrate findings

- Downgrade when route modes, hydration, adapter behavior, cache scope, and production output
  are explicit and tested.
