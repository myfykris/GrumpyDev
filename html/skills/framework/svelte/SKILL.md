---
name: gd-svelte
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Svelte and SvelteKit engineering work for reactivity, server and client boundaries, load functions, form actions, hooks, adapters, rendering, and deployment."
---

# Svelte and SvelteKit GrumpyDev review

## Quick checks

- Read Svelte, SvelteKit, adapter, Vite, and package versions plus route and rendering
  configuration.

- Trace runes or legacy reactivity, component state, load functions, form actions, remote
  calls, endpoints, hooks, and stores.

Watch especially for secrets imported into universal modules, browser-only
values causing hydration mismatch, form actions assumed protected by page
guards, stale data after actions, streamed promises failing late, and adapter
differences ignored.

- Assess secret leakage, missing action authorization, cross-user cache leakage, or unsafe
  offline private data under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Svelte and
SvelteKit specialist.

## Verdict context

State route modes, data and authorization boundaries, reactive ownership, adapter assumptions,
cache behavior, and production evidence.
