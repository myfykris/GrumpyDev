---
name: gd-supabase
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Supabase engineering work for PostgreSQL ownership, Row Level Security, Auth, Data API exposure, Edge Functions, Realtime, Storage, connection pooling, migrations, backups, and deployment."
---

# Supabase GrumpyDev review

## Quick checks

- Read Supabase services, client versions, project configuration, migrations, schema, policies,
  functions, grants, and generated types.

- Trace anon, authenticated, service-role, secret, publishable, database, and user JWT
  identities through every access path.

Watch especially for tables exposed without RLS, policies that check only one
operation, security-definer functions widening access, service keys reaching
clients, Edge Functions accepting unverified callers, pool mode mismatched to
prepared statements, and database backups mistaken for Storage backups.

- Assess missing tenant RLS, client-exposed privileged keys, unprotected RPC or functions, or
  unrecoverable authoritative data under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Supabase
specialist.

## Verdict context

State projects, access paths and identities, policy proof, privileged boundaries, pooling,
service behavior, backup scope, and recovery evidence.
