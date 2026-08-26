---
name: svelte
description: Review Svelte and SvelteKit plans for reactivity, server and client boundaries, load functions, form actions, hooks, adapters, rendering, and deployment. Use when a plan creates or changes Svelte applications.
---

# Svelte and SvelteKit plan review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
`web-accessibility` skills.

## Inspect evidence

- Read Svelte, SvelteKit, adapter, Vite, and package versions plus route and rendering
  configuration.
- Trace runes or legacy reactivity, component state, load functions, form actions, remote
  calls, endpoints, hooks, and stores.
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

## Challenge the plan

### Recurring traps

Watch especially for secrets imported into universal modules, browser-only values causing
hydration mismatch, form actions assumed protected by page guards, stale data after actions,
streamed promises failing late, and adapter differences ignored.

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

- Treat secret leakage, missing action authorization, cross-user cache leakage, or unsafe
  offline private data as critical.
- Downgrade when server and client boundaries, actions, invalidation, adapter output, and
  failure behavior are tested.

## Add to the verdict

State route modes, data and authorization boundaries, reactive ownership, adapter assumptions,
cache behavior, and production evidence.
