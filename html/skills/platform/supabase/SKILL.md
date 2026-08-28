---
name: supabase
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Supabase plans and other engineering artifacts for PostgreSQL ownership, Row Level Security, Auth, Data API exposure, Edge Functions, Realtime, Storage, connection pooling, migrations, backups, and deployment. Project applicability: the project uses or materially depends on Supabase services."
---

# Supabase GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `postgresql`,
`application-security` and `schema-evolution` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read Supabase services, client versions, project configuration, migrations, schema, policies,
  functions, grants, and generated types.

- Trace anon, authenticated, service-role, secret, publishable, database, and user JWT
  identities through every access path.

Watch especially for tables exposed without RLS, policies that check only one
operation, security-definer functions widening access, service keys reaching
clients, Edge Functions accepting unverified callers, pool mode mismatched to
prepared statements, and database backups mistaken for Storage backups.

Lean mode is insufficient when this material severity condition may apply:

- Treat missing tenant RLS, client-exposed privileged keys, unprotected RPC or functions, or
  unrecoverable authoritative data as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Supabase evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State projects, access paths and identities, policy proof, privileged boundaries, pooling,
service behavior, backup scope, and recovery evidence.
