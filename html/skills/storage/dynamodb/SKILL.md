---
name: dynamodb
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review DynamoDB plans and other engineering artifacts for access patterns, keys, indexes, consistency, hot partitions, transactions, capacity, streams, and recovery. Project applicability: the project stores or queries application data in Amazon DynamoDB."
---

# DynamoDB GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the
`distributed-systems` skill when cross-region behavior matters, and the
applicable installed application specialist.

## Lean review

- Establish the regions, table class and capacity mode, global-table version,
  backup settings, and client behavior.

- Read access-pattern inventory, key design, item shapes, indexes, conditions,
  transactions, capacity mode, TTL, streams, and recovery settings.

Watch especially for hot partition keys, scans hidden behind convenience APIs,
secondary-index consistency assumed to be immediate, conditional writes omitted
from read-modify-write flows, item-size growth, transaction limits, TTL deletion
treated as timely, and retries repeating non-idempotent effects.

Lean mode is insufficient when this material severity condition may apply:

- Treat a hot partition on a critical path, lost-update behavior, or
  retry-amplified side effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete DynamoDB evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State access-pattern coverage, key distribution, consistency and transaction
guarantees, capacity risk, and recovery proof.
