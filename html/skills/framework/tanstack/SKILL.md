---
name: gd-tanstack
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review TanStack engineering work across Start, Router, Query, DB, Store, Table, Form, Virtual, Pacer, AI, Charts, Hotkeys, Markdown, Highlight, Devtools, Config, CLI, Intent, and related packages for state, data, rendering, authorization, accessibility, performance, build, and deployment risks."
---

# TanStack GrumpyDev review

## Quick checks

- Identify every TanStack product and version in use. Classify it as routing or
  full stack, remote data or client state, data presentation or input,
  scheduling or virtualization, AI or content rendering, or development and
  build tooling. Do not assume one product's guarantees apply to another.

- Inspect the product-specific sources of truth: route trees, loaders, server
  functions and middleware; query clients and keys; DB collections and sync;
  stores and selectors; table, form and virtualizer state; pacer controls; AI
  streams and tools; content renderers; and generated build or configuration
  artifacts.

Watch especially for cross-user cache or dehydrated-state leakage, optimistic
effects without persistence or rollback, server functions trusted because
callers are generated, competing data owners, unstable row or item identities,
async validation races, inaccessible virtualization or table behavior,
debounced work lost on teardown, untrusted model or Markdown output rendered as
safe, development tooling exposed in production, and generated artifacts that
silently diverge from their source.

- Assess cross-user data leakage, missing server-function authorization,
  untrusted output reaching an executable or HTML sink, or unreconciled
  irreversible optimistic effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the TanStack
specialist.

## Verdict context

State the products in use, source of truth and identity model for each, data and
authorization boundaries, persistence and failure behavior, accessibility and
performance limits, generated-artifact ownership, and representative runtime
evidence.
