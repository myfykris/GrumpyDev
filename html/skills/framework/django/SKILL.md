---
name: django
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Django engineering work for model and migration behavior, transactions, ORM queries, request security, caching, background work, settings, and deployment risks."
---

# Django GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `python` skill.

## Lean review

- Read settings, URL and middleware order, models and migrations, managers and
  querysets, authentication, templates or API layers, caching, tasks, and tests.

- Trace requests and jobs through transactions, permissions, ORM queries,
  signals, files, caching, and deployment or migration order.

Watch especially for generated migrations assumed to be operationally safe, N+1
query regressions, business behavior hidden in signals, transaction scopes that
do not cover deferred work, sync and async crossings, and development settings
presented as deployment evidence.

Lean mode is insufficient when this material severity condition may apply:

- Treat authorization bypass, blocking migration, or async-unsafe state on a
  critical path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Django evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State migration and transaction safety, query behavior, authorization controls,
signal or task ownership, settings assumptions, and deployment evidence.
