# htmx full-review guidance

## Operating conditions

Establish the project target: htmx version, server and template stack, extensions, request and
response conventions, fragment detection, history policy, cache variation, CSRF transport, CSP,
and accessibility behavior.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise requests with and without htmx headers, direct navigation, refresh, back and
  forward, cache hits, and history misses.
- Delay and reorder responses to prove synchronization, stale-response handling, disabled
  controls, and error recovery.
- Test injected content, CSRF failure, script policy, sensitive history, and
  assistive-technology behavior.
