# Blazor standard review

## Inspect additional evidence

- Trace component lifecycle, prerendering, hydration, circuits, cancellation,
  reconnection, user state, and server or browser boundaries.

## Establish the operating model

Establish the project target: .NET and Blazor versions, render modes by route,
hosting and proxy, browser targets, authentication, trimming and AOT, CDN
prohibition or asset policy, and offline needs. The changed boundary must
define: Server, WebAssembly, auto and hybrid modes, circuit lifecycle,
prerendering, hydration, state persistence, JS interop, authentication,
payloads, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Server, WebAssembly, auto and hybrid modes, circuit lifecycle, prerendering,
hydration. Prove state persistence, JS interop, authentication, payloads,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Require one declared rendering mode per route or component and account for
  code that runs during prerender and again after activation.
- Check circuit lifetime, scoped-service semantics, reconnection, stale state,
  concurrent events, and server memory limits.
- Treat browser and server authorization separately; never rely on hidden UI or
  client state as access control.
- Require disposal for timers, subscriptions, cancellation sources, and
  JavaScript references across component teardown.
- Test published output, navigation reloads, offline or disconnected states,
  accessibility, trimming, and supported browsers.

## Verify the claims

- Verify these behaviors through the actual Blazor lifecycle and production
  pipeline: Server, WebAssembly, auto and hybrid modes, circuit lifecycle,
  prerendering, hydration. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: state persistence, JS interop,
  authentication, payloads, deployment. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which .NET and Blazor versions and hosting mode, rendering mode, and
  deployment target apply?
- How are circuit lifetime, reconnection, state, authorization, prerendering,
  errors, and browser interop handled?

## Calibrate findings

- Downgrade when the hosting mode and lifecycle are explicit and auth,
  reconnect, state, and rendering tests cover them.
