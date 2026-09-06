---
name: redis
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Redis engineering work for data structures, eviction, persistence, atomicity, clustering, hot keys, cache consistency, and recovery."
---

# Redis GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
