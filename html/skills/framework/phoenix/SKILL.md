---
name: gd-phoenix
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Phoenix engineering work for supervision, Ecto transactions, LiveView state, channels, PubSub, authorization, background work, and deployment risks."
---

# Phoenix GrumpyDev review

## Quick checks

- Read endpoint and router pipelines, plugs, contexts, Ecto schemas and
  migrations, LiveViews or channels, PubSub, supervision, releases, and tests.

- Trace HTTP and socket authentication, process state, database transactions,
  broadcasts, background jobs, reconnects, and rolling deployment.

Watch especially for processes with unclear ownership, mailbox growth, blocking
work on BEAM schedulers, Ecto operations assumed to share a transaction,
LiveView state lost or duplicated on reconnect, and PubSub delivery treated as
exactly once.

- Assess cross-user socket state, unsupervised critical work, or incompatible
  rolling release behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Phoenix specialist.

## Verdict context

State process and state ownership, authorization boundary, Ecto and migration
safety, realtime delivery behavior, cluster assumptions, and release evidence.
