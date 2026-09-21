# Supabase full-review guidance

## Operating conditions

Establish the project target: Supabase projects and regions, PostgreSQL version and extensions,
exposed schemas, Data API and direct connection paths, RLS and grant ownership, Auth providers
and token policy, Edge Function verification, Realtime, Storage, pooling mode, migrations,
backups, and environment separation.

## Failure patterns

- Enable and test deny-by-default RLS on every exposed table and cover select, insert, update,
  delete, ownership, and tenant isolation.
- Review grants, views, function security, search paths, RPC exposure, triggers, and privileged
  service code alongside policies.
- Choose transaction or session pooling deliberately and bound application concurrency,
  prepared statements, long transactions, and migrations.
- Define Auth redirect origins, email delivery, token lifetime, role changes, account deletion,
  abuse controls, and service-key rotation.
- Authorize Edge Functions explicitly, validate webhook or user identities, and design external
  effects for retries and partial completion.
- Separate database backup, point-in-time recovery, Storage object protection, branch data,
  migration rollback, and deletion recovery.

## Verification to run or specify in the plan

- Run policy tests as anon, authenticated users from different tenants, owners, service roles,
  and direct database roles.
- Exercise RPC, views, Storage, Realtime, Edge Functions, stale tokens, pooling, connection
  pressure, migrations, and restore.
- Inspect effective grants, policies, exposed schemas, generated API behavior, project
  settings, and client-visible configuration.
