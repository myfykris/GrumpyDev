---
name: gd-astro
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Astro engineering work for rendering mode, islands, hydration, adapters, server endpoints, content, caching, and deployment boundaries."
---

# Astro GrumpyDev review

## Quick checks

- Read the Astro, adapter, integration, and UI framework versions plus output mode and route
  settings.

- Check whether each affected route is prerendered or rendered on demand.
  Separately identify its client and server islands; both are components and
  can coexist within a page.

Watch especially for unnecessary client hydration, on-demand routes without a
compatible adapter or required prerender override, secrets in client-visible
island props, adapter behavior treated as portable, and personalized content
cached as public HTML. Static output can include on-demand routes when the
adapter and route configuration support them.

- Assess secret disclosure, missing server authorization, or private responses stored in shared
  caches under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Astro specialist.

## Verdict context

State each changed route mode, server and client boundary, adapter assumptions, cache scope,
hydration cost, and production-build evidence.
