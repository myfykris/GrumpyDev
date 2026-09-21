# Svelte and SvelteKit full-review guidance

## Operating conditions

Establish the project target: Svelte and SvelteKit versions, reactivity mode, adapter and host,
route rendering and prerender policy, load and action conventions, session and authorization
boundary, environment sources, service worker, and browser targets.

## Failure patterns

- Require explicit ownership for reactive state and avoid duplicated derived values or effects
  that hide data flow.
- Keep secrets and privileged data in server-only modules and validate every server action,
  endpoint, and remote operation.
- Define load invalidation, action results, optimistic state, redirects, errors, progressive
  enhancement, and no-JavaScript behavior.
- Verify prerender eligibility, dynamic routes, cookies, streaming, service workers, and
  adapter support against the selected host.
- Test hydration, navigation, direct requests, form resubmission, offline caches, denied
  access, and mixed old and new assets.

## Verification to run or specify in the plan

- Build the selected adapter output and inspect server, client, prerendered, and service-worker
  artifacts.
- Exercise direct route loads, client navigation, form actions with and without JavaScript,
  invalidation, redirects, and late errors.
- Run production output with representative cookies, proxy headers, environment values, caches,
  and host limits.
