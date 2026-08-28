---
name: redis
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Redis plans and other engineering artifacts for data structures, eviction, persistence, atomicity, clustering, hot keys, cache consistency, and recovery. Project applicability: Redis holds cache, coordination, queue, session, or primary application state."
---

# Redis GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed storage or messaging specialist for the role Redis serves.

## Lean review

- Establish the exact Redis-compatible product, version, deployment mode,
  persistence mode, and failover implementation.

- Read key design, value sizes, TTLs, commands, scripts, transactions, memory
  policy, persistence, topology, failover, and load tests.

Watch especially for a cache silently becoming authoritative, hot or oversized
keys, eviction removing required state, multi-key operations crossing cluster
slots, distributed locks without fencing, failover losing acknowledged writes,
scripts blocking the server, and cache fills stampeding dependencies.

Lean mode is insufficient when this material severity condition may apply:

- Treat loss of non-reconstructible state, unsafe distributed coordination, or
  unbounded hot-key impact as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Redis evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State Redis's authority, memory bounds, atomicity scope, cache-consistency
behavior, topology, and recovery evidence.
