# htmx standard review

## Inspect additional evidence

- Trace full-page versus fragment rendering, direct navigation, redirects, history restore,
  caching, and progressive enhancement.
- Inspect HTML sanitization, CSP, CSRF controls, response headers, focus behavior,
  announcements, and disabled states.

## Establish the operating model

Establish the project target: htmx version, server and template stack, extensions, request and
response conventions, fragment detection, history policy, cache variation, CSRF transport, CSP,
and accessibility behavior.

The URL and server-rendered HTML remain authoritative. Any URL placed in history must return a
complete navigable page outside an htmx request.

## Challenge the reviewed work

### Recurring traps

- Require server responses to define full-page and fragment behavior without trusting a
  forgeable client header for authorization.
- Use synchronization or cancellation where concurrent requests can return out of order and
  corrupt visible state.
- Vary caches correctly for fragment responses or choose distinct URLs; test browser back,
  refresh, copied links, and history misses.
- Disable history storage for sensitive content and validate CSRF, CSP, origin, and HTML
  sanitization controls.
- Preserve focus, validation messages, busy state, keyboard behavior, and live announcements
  across swaps.

## Verify the claims

- Exercise requests with and without htmx headers, direct navigation, refresh, back and
  forward, cache hits, and history misses.
- Delay and reorder responses to prove synchronization, stale-response handling, disabled
  controls, and error recovery.
- Test injected content, CSRF failure, script policy, sensitive history, and
  assistive-technology behavior.

## Ask when evidence is missing

- Which htmx version, extensions, server templates, fragment convention, swap targets, and
  cache behavior apply?
- How are request races, direct navigation, history storage, CSRF, injected HTML, focus, and
  errors handled?

## Calibrate findings

- Downgrade when URLs, fragment contracts, caching, ordering, security, and accessible swap
  behavior are tested.
