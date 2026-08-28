# Svelte and SvelteKit standard review

## Inspect additional evidence

- Classify code and environment values as universal, server-only, client-only, build-time, or
  prerendered.
- Inspect cookies, sessions, authorization, invalidation, streaming, error boundaries, service
  workers, and adapter output.

## Establish the operating model

Establish the project target: Svelte and SvelteKit versions, reactivity mode, adapter and host,
route rendering and prerender policy, load and action conventions, session and authorization
boundary, environment sources, service worker, and browser targets.

The plan must distinguish universal load code from server-only code and browser code. Form
actions and server routes need per-operation authorization even when page loading is protected.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Build the selected adapter output and inspect server, client, prerendered, and service-worker
  artifacts.
- Exercise direct route loads, client navigation, form actions with and without JavaScript,
  invalidation, redirects, and late errors.
- Run production output with representative cookies, proxy headers, environment values, caches,
  and host limits.

## Ask when evidence is missing

- Which Svelte, SvelteKit, reactivity mode, adapter, host, route rendering, and service-worker
  choices apply?
- Where do load data, actions, sessions, authorization, environment values, invalidation, and
  errors live?

## Calibrate findings

- Downgrade when server and client boundaries, actions, invalidation, adapter output, and
  failure behavior are tested.
