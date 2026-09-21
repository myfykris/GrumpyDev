# PHP survey contribution

## Applies when

Apply this contribution when PHP executes application, library, command, scheduled, or
worker code in the project.

## Inspect

- Establish supported PHP versions, SAPI, process lifecycle, loaded
  configuration, extensions, and Composer platform constraints for each web,
  CLI, worker, test, and CI boundary.

## Ask when unresolved

- Which PHP versions must each web, CLI, worker, scheduled, development, test,
  and CI environment support? Ask when syntax, dependency, extension, or
  runtime behavior can differ across those targets.

- Which SAPI and web-server arrangement handles production requests, and does
  Apache run mod_php or proxy to PHP-FPM? Ask when request metadata, process
  lifecycle, permissions, or configuration scope affects future reviews.

- If FastCGI or PHP-FPM is used, which server parameters and trusted proxy
  rules establish script paths, HTTPS, host, client address, and other
  `$_SERVER` values the application relies on?

- Which PHP extensions, native libraries, and version ranges are guaranteed in
  every applicable environment? Ask only for dependencies that change behavior
  or deployment feasibility.

- Which INI sources and pool overrides are authoritative for errors, sessions,
  uploads, encoding, locale, memory, execution time, OPcache, and preloading?

- Which processes are long-running, what state can survive between requests or
  jobs, and how are those processes drained, reset, restarted, and monitored?

- How do deployments coordinate web workers, queue workers, schedulers,
  database migrations, cached values, sessions, OPcache, and rollback while old
  and new code can coexist?

- Which runtime or deployment differences are material for future reviews: PHP
  version, SAPI, mod_php, FastCGI, PHP-FPM, worker, INI, proxy, session, cache,
  OPcache, rollout, and rollback coverage?

## Record

Map durable PHP version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
