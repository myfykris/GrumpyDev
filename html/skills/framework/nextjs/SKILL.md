---
name: nextjs
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Next.js plans and other engineering artifacts for server and client boundaries, caching, rendering mode, routing, data mutation, runtime selection, authentication, and deployment risks. Project applicability: the project uses or materially depends on Next.js."
---

# Next.js GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `react`,
`javascript`, and `typescript` skills.

## Lean review

- Read Next.js and React versions, app or pages router, route configuration,
  server and client components, caching directives, middleware, runtime targets,
  and tests.

- Trace data reads and mutations through rendering, caches, revalidation,
  cookies, authentication, navigation, streaming, and deployment.

Watch especially for server and client boundaries crossed accidentally, stale or
over-broad cache and revalidation behavior, route runtimes that lack required
APIs, secrets included in client bundles, hydration differences, and build-time
data assumed to remain current. Also watch for server actions treated as private
functions, user-specific results entering shared caches, and remote fetch or
redirect input becoming an SSRF or open-redirect path.

Lean mode is insufficient when this material severity condition may apply:

- Treat server-only data exposure, cache leakage across users, or unsafe
  mutation authorization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/rendering-caching-and-hydration.md):
  Read when the reviewed work directly or indirectly changes server or client
  components, App or Pages Router rendering,
  static or dynamic rendering, streaming, Suspense, hydration, fetch caching, cache
  keys, tags, revalidation, personalization, or stale behavior.
- [Focused rules](references/server-actions-routes-and-security.md):
  Read when the reviewed work directly or indirectly changes server actions, route
  handlers, middleware, authentication,
  authorization, CSRF behavior, remote fetches, image or metadata URLs, redirects,
  rewrites, preview access, environment exposure, or server-to-client serialization.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State rendering and runtime modes, server-client trust boundary, route and
action authorization, cache and revalidation scope, outbound fetch policy,
mutation contracts, authentication behavior, and production evidence.
