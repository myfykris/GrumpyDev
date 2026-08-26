---
name: blazor
description: Review Blazor plans for rendering mode, circuit or WebAssembly state, dependency lifetimes, JavaScript interop, navigation, security, accessibility, and deployment risks. Use when a plan changes Blazor components, routes, services, or hosting models.
---

# Blazor plan review

Apply this guidance alongside the core GrumpyDev review and the `csharp` skill.

## Inspect evidence

- Establish the exact .NET, Blazor, hosting, rendering, and deployment versions
  or modes.
- Read rendering-mode configuration, component routes, service lifetimes,
  authentication state, persistence, JavaScript interop, publish settings, and
  browser tests.
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

## Challenge the plan

### Recurring traps

Watch especially for server-circuit state surviving longer than intended,
WebAssembly and server execution assumptions being mixed, prerendering that runs
initialization twice, JavaScript interop after component disposal, and UI
visibility mistaken for authorization.

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

- Treat server-only authorization missing, cross-circuit state leakage, or
  unrecoverable core interaction loss as critical.
- Downgrade when the hosting mode and lifecycle are explicit and auth,
  reconnect, state, and rendering tests cover them.

## Add to the verdict

State rendering mode, state and service lifetimes, authorization boundary,
interop lifecycle, reconnection behavior, and published-browser evidence.
