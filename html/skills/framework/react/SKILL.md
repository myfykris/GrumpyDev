---
name: react
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review React engineering work for state ownership, effect lifecycle, rendering, accessibility, performance, hydration, and user-experience failure risks."
---

# React GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review, the `javascript` or
`typescript` skill, and `application-security` when untrusted content,
authentication, or sensitive browser state changes.

## Lean review

- Identify the React and framework versions, rendering mode, routing, data
  library, form approach, styling system, tests, and supported browsers.

- Trace ownership for server data, URL state, form state, local interaction
  state, cached state, and cross-page state.

Watch especially for stale closures and incomplete effect dependencies,
duplicated derived state, unstable list keys, asynchronous results applied after
ownership changes, Strict Mode exposing non-idempotent effects, and client-side
checks mistaken for authorization. Also watch for unsafe HTML or URL sinks,
secrets in browser state or bundles, and server-rendered data crossing users
through caches or hydration.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user hydration leakage, missing authorization at the server
  boundary, or an inaccessible core flow as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/server-rendering-and-hydration.md):
  Read when the reviewed work directly or indirectly changes server rendering, server
  components, hydration, streaming,
  Suspense across a server boundary, serialized initial data, or browser and server
  execution differences.
- [Focused rules](references/untrusted-content-and-browser-security.md):
  Read when the reviewed work directly or indirectly handles untrusted HTML, Markdown,
  URLs, styles, iframes, widgets,
  direct DOM sinks, browser storage, client-side secrets, source maps, CSP, framing, or
  cross-origin behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the state owner for each changed flow, the server/client and trust
boundaries, untrusted rendering and browser-storage policy, all user-visible
failure states, accessibility evidence, and the test that proves the interaction
works.
