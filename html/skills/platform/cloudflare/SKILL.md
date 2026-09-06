---
name: cloudflare
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Cloudflare engineering work for Workers runtime limits, isolate lifecycle, bindings, KV consistency, Durable Objects, D1, queues, caching, networking, and deployment."
---

# Cloudflare developer platform GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `serverless`,
`distributed-systems` and `observability` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read compatibility date and flags, Workers runtime, bindings, routes, regions, limits,
  deployment configuration, and account settings.

- Classify state across request memory, Cache API, KV, Durable Objects, D1, R2, queues,
  external stores, and browser caches.

Watch especially for mutable global state treated as durable, KV used for
coordination despite eventual consistency, Durable Object in-memory values lost
after hibernation, queue or alarm delivery assumed exactly once, and local
emulation treated as proof of production limits.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-tenant cache leakage, exposed bindings or secrets, lost authoritative writes, or
  unbounded retry effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Cloudflare developer platform evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State product choices, state and consistency owners, effective limits, cache policy, delivery
semantics, security boundaries, and migration evidence.
