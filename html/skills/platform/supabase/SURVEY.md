# Supabase survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Supabase
services.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Supabase. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Supabase projects and regions, PostgreSQL version and extensions,
  exposed schemas, Data API and direct connection paths, RLS and grant ownership, Auth providers
  and token policy, Edge Function verification, Realtime, Storage, pooling mode, migrations,
  backups, and environment separation.
- Review doctrine: RLS protects table access through applicable database roles, but
  service-role and privileged connections can bypass it. Every view, RPC, Edge Function, Storage
  path, and direct connection needs its own proven trust and authorization model.
- Deployment-profile facts: Supabase projects and regions, PostgreSQL and extension
  versions, exposed schemas, RLS and grants, Auth settings, Edge Function runtime and
  verification, Realtime and Storage policies, Supavisor mode, network controls, migrations,
  backups, and limits.

## Ask only when materially unresolved

- Which Supabase services, projects, regions, exposed schemas, identities, RLS policies, and
  connection paths apply?
- How are Auth, RPC, Edge Functions, Realtime, Storage, pooling, migrations, backups, limits,
  and recovery handled?

## Record in .grump

Record confirmed Supabase answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Supabase doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Supabase when its hosted or self-managed version, project boundaries,
PostgreSQL schema, Row Level Security, authentication providers, Edge Functions,
Storage policies, Realtime use, or backup and recovery policy materially changes. Also
re-survey when evidence conflicts with saved doctrine or the user requests a context
refresh.
