---
name: elixir
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Elixir plans and other engineering artifacts for supervision, process ownership, message ordering, backpressure, fault recovery, distribution, state, and release risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Elixir or Erlang code, OTP applications, or runtime behavior."
---

# Elixir GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
