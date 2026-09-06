---
name: rails
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Rails engineering work for Active Record behavior, migrations, callbacks, jobs, caching, authorization, request security, and zero-downtime deployment risks."
---

# Ruby on Rails GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
