# Astro full-review guidance

## Operating conditions

Establish the project target: Astro version, output mode, adapter and host, route rendering
choices, client frameworks, content sources, environment model, cache policy, and browser
targets.

## Failure patterns

- Check route rendering separately from component islands. Under static output,
  on-demand routes need a compatible adapter and the appropriate prerender
  override; static output alone is not evidence that those routes are invalid.
- Require an explicit hydration reason and loading directive for every client island.
- Verify that protected or personalized routes render on a trusted server boundary and
  authorize each request.
- Keep server-island inputs small and non-sensitive; account for fallback, delay, caching, and
  page URL differences.
- Require adapter-specific evidence for cookies, streaming, middleware, image handling,
  environment variables, and runtime APIs.
- Test direct navigation, history, no-JavaScript behavior, content build failures, and mixed
  static and dynamic routes.

## Verification to run or specify in the plan

- Build the actual static or server output and inspect emitted client JavaScript, routes,
  assets, and server entrypoints.
- Exercise direct requests, slow server islands, missing content, denied access, stale caches,
  and adapter-specific failures.
- Run representative production output on the selected adapter rather than treating the
  development server as evidence.
