# WordPress survey contribution

## Applies when

Apply this contribution when the project uses WordPress or when its behavior constrains
a supported build, deployment, client, or operating environment.

## Inspect

- Inspect WordPress and PHP targets, plugin and theme code, hook registrations,
  block metadata, REST routes, capability checks, nonce use, database queries,
  cron events, caches, filesystem access, update policy, and deployment
  runbooks.

## Ask when unresolved

- Which of these durable facts materially change future reviews: WordPress,
  PHP, database and web-server versions, hosting topology, multisite, plugin
  and theme ownership, cache and object store, update policy, filesystem
  access, and deployment process?

- Which runtime or deployment differences are material for future reviews: PHP,
  database, Apache or Nginx, SAPI, filesystem ownership, cron, object cache,
  multisite, uploads, proxy, hosting controls, updates, and rollback coverage?

## Record

Map durable WordPress version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
