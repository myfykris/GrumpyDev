---
name: graphql-api-design
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review GraphQL API plans and other engineering artifacts for schema ownership, authorization, resolver behavior, query cost, batching, nullability, errors, caching, and evolution. Project applicability: the project exposes, consumes, or operates GraphQL schemas, resolvers, clients, or gateways."
---

# GraphQL API design GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and applicable installed framework and storage
specialists.

## Lean review

- Read schemas, directives, resolvers, loaders, authorization, pagination, query
  limits, error conventions, persisted operations, and contract tests.

- Trace one nested query and mutation through parsing, authorization, data
  access, partial failure, retries, caching, and schema rollout.

Watch especially for N+1 resolver behavior, unbounded query depth or cost,
authorization applied only at entry points, nullable failures propagating
farther than expected, batching caches shared across users, deprecated fields
never removed, mutation input mapped directly to persistence, subscription
permissions that outlive the user role, and schema changes that break persisted
operations.

Lean mode is insufficient when this material severity condition may apply:

- Treat field-level data exposure or unbounded query work reachable by clients
  as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/subscriptions-and-persisted-operations.md):
  Read when the reviewed work directly or indirectly changes subscriptions, long-lived
  authorization, token expiry,
  revocation, reconnect, fan-out, event filtering, persisted operations, operation
  registration, allowlists, rollout, or revocation.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State schema ownership, authorization coverage, mutation property controls,
query-cost and subscription limits, cache scope, production exposure, resolver
evidence, error semantics, and evolution safety.
