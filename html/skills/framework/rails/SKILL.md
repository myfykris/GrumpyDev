---
name: rails
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Rails plans and other engineering artifacts for Active Record behavior, migrations, callbacks, jobs, caching, authorization, request security, and zero-downtime deployment risks. Project applicability: the project uses or materially depends on Ruby on Rails."
---

# Ruby on Rails GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `ruby` skill.

## Lean review

- Read Rails and Ruby versions, routes, middleware, models and migrations,
  callbacks, jobs, caches, credentials, server and worker configuration, and
  tests.

- Trace requests and jobs through strong parameters, authorization,
  transactions, queries, callbacks, retries, and deployment.

Watch especially for callbacks hiding transactional side effects, N+1 query
regressions, autoload and eager-load differences, jobs enqueued before commit,
non-idempotent retries, and migrations whose locks or rewrites are invisible in
development data.

Lean mode is insufficient when this material severity condition may apply:

- Treat authorization bypass, callback-driven duplicate effects, or destructive
  migration behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Ruby on Rails evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State ORM and callback behavior, migration safety, job guarantees, authorization
boundaries, runtime configuration, and production deployment evidence.
