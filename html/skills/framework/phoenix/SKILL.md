---
name: phoenix
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Phoenix plans and other engineering artifacts for supervision, Ecto transactions, LiveView state, channels, PubSub, authorization, background work, and deployment risks. Project applicability: the project uses or materially depends on Phoenix."
---

# Phoenix GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `elixir` skill.

## Lean review

- Read endpoint and router pipelines, plugs, contexts, Ecto schemas and
  migrations, LiveViews or channels, PubSub, supervision, releases, and tests.

- Trace HTTP and socket authentication, process state, database transactions,
  broadcasts, background jobs, reconnects, and rolling deployment.

Watch especially for processes with unclear ownership, mailbox growth, blocking
work on BEAM schedulers, Ecto operations assumed to share a transaction,
LiveView state lost or duplicated on reconnect, and PubSub delivery treated as
exactly once.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user socket state, unsupervised critical work, or incompatible
  rolling release behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Phoenix evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State process and state ownership, authorization boundary, Ecto and migration
safety, realtime delivery behavior, cluster assumptions, and release evidence.
