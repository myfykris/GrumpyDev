# WordPress database, cron, cache, and multisite

Read this reference when the reviewed work directly or indirectly changes wpdb, schema,
options, metadata, taxonomy,
object or page caches, cache scope, WP-Cron, an external scheduler, background retries,
multisite data, tenant scope, or production query behavior.

## Review requirements

- Review `$wpdb` queries, schema changes, option autoloading, post meta,
  taxonomy, cache invalidation, and concurrency. Do not use the options table as
  an unbounded event store or lock service.

- Make WP-Cron timing limitations, duplicate execution, locks, retries,
  timeouts, and external scheduler integration explicit. Jobs must tolerate
  delayed and repeated invocation.

- Account for page, object, opcode, browser, CDN, and plugin caches plus
  multisite scope. Invalidation and cache keys must match tenant, locale,
  capability, and content ownership.

## Verify the claims

- Load test hook, query, cache, cron, block, and REST behavior with
  production-shaped content and plugin combinations.
