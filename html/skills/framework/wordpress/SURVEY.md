# WordPress survey contribution

## Applicability

Apply this contribution when the project uses WordPress or when its behavior constrains
a supported build, deployment, client, or operating environment. Combine it with the
`php`, applicable database and web-server, `application-security`, and deployment
skills. Deduplicate shared version, runtime, architecture, identity, data, security, and
deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect WordPress and PHP targets, plugin and theme code, hook registrations,
block metadata, REST routes, capability checks, nonce use, database queries,
cron events, caches, filesystem access, update policy, and deployment runbooks,
dependency declarations, build and deployment files, CI workflows, runbooks, and
project documentation. Distinguish a committed project fact from a local-machine
default or a transient environment value. Do not access or mutate an external
system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- WordPress, PHP, database, and web-server versions.
- Hosting and process topology.
- Single-site or multisite.
- Plugin and theme ownership.
- Cache and object store.
- Update policy.
- Filesystem access.
- Deployment and rollback process.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: PHP, database, Apache or Nginx, SAPI,
  filesystem ownership, cron, object cache, multisite, uploads, proxy, hosting
  controls, updates, and rollback coverage.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later WordPress reviews. Candidate subjects are: WordPress, PHP,
database and web-server versions, hosting topology, multisite, plugin and theme
ownership, cache and object store, update policy, filesystem access, and
deployment process.
- Align existing domain questions with this deployment guidance when it is
  material: PHP, database, Apache or Nginx, SAPI, filesystem
  ownership, cron, object cache, multisite, uploads, proxy, hosting controls,
  updates, and rollback coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record WordPress answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing WordPress survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable WordPress doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a WordPress/PHP/database/web-server change, multisite adoption,
new plugin or theme owner, cache or filesystem change, update-policy change, or
deployment redesign. Also refresh the contribution when evidence contradicts
saved doctrine or the user explicitly requests a context refresh.
