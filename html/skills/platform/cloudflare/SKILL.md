---
name: cloudflare
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Cloudflare plans and other engineering artifacts for Workers runtime limits, isolate lifecycle, bindings, KV consistency, Durable Objects, D1, queues, caching, networking, and deployment. Project applicability: applications run on Cloudflare Workers or related developer-platform services."
---

# Cloudflare developer platform GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `serverless`,
`distributed-systems` and `observability` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
