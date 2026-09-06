---
name: elixir
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Elixir engineering work for supervision, process ownership, message ordering, backpressure, fault recovery, distribution, state, and release risks."
---

# Elixir GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Establish the exact Elixir, Erlang/OTP, release-target, and dependency
  versions.

- Read mix files, supervision trees, process registries, GenServer state, queue
  or stream configuration, clustering, release configuration, and tests.

Watch especially for unbounded mailboxes, GenServer callbacks doing slow work,
incorrect links or monitors, supervision restart loops that amplify failure,
dynamically created atoms from external input, ETS tables whose owner dies, and
retries that repeat side effects.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsupervised critical work, mailbox exhaustion, or incompatible rolling
  release behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Elixir evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the supervision and state model, overload controls, delivery guarantees,
cluster assumptions, release sequence, and recovery evidence.
