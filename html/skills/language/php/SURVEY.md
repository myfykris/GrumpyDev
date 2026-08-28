# PHP survey contribution

## Applicability

Apply this contribution when PHP executes application, library, command, scheduled, or
worker code in the project. Combine it with the applicable PHP framework, web server,
storage, queue, container, and operating-system survey contributions. Deduplicate shared
runtime and deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

- Read `composer.json`, `composer.lock`, Composer platform configuration,
  required extensions, scripts, autoloading, and plugin permissions.
- Inspect containers, build files, CI matrices, deployment manifests, hosting
  configuration, runtime inventory, and existing architecture documentation for
  declared PHP versions and environment differences.
- Inspect PHP configuration paths and effective settings captured for web, CLI,
  test, worker, and scheduled processes. Account for SAPI-specific configuration
  files, scan directories, pool settings, and environment overrides.
- Read Apache, Nginx, FastCGI, PHP-FPM, IIS, application-server, worker, and
  scheduler configuration that establishes the process lifecycle and request
  parameters.
- Inspect required native libraries, database drivers, session and cache stores,
  temporary directories, upload storage, timezone, locale, encoding, OPcache,
  preloading, memory limits, and error handling.
- Read deployment and rollback documentation before asking how workers restart,
  caches refresh, or old and new versions overlap.

## Durable project facts

- Supported PHP versions for production web requests, CLI tools, workers,
  scheduled jobs, development, tests, and CI.
- SAPI and execution model for each runtime, including Apache module, CGI or
  FastCGI, PHP-FPM, IIS, embedded server, or long-running application server.
- Web server, reverse proxy, trusted proxy policy, TLS termination, path
  mapping, and the request metadata the application is allowed to trust.
- Required extensions and meaningful extension or native-library versions.
- Authoritative INI files and overrides, error display and reporting policy,
  timezone, locale, character encoding, memory and execution limits, and upload
  constraints.
- PHP-FPM pools or other process managers, user and group identities, socket or
  port ownership, worker sizing, recycle policy, graceful shutdown, and status
  or health interfaces.
- Long-running queue, scheduler, or application workers and the mechanism that
  resets state and restarts them during deployment.
- Session, cache, file, upload, temporary storage, logging, and secret sources,
  including material differences between environments.
- Composer dependency and lock policy, platform emulation, update process, and
  artifact or autoload optimization strategy.
- OPcache, preloading, generated cache, deployment, drain, restart, rollback,
  and mixed-version expectations.
- Deployment-profile guidance: PHP version, SAPI, mod_php,
  FastCGI, PHP-FPM, worker, INI, proxy, session, cache, OPcache, rollout, and
  rollback coverage. Map the answers into named profiles.

## Ask only when materially unresolved

- Which PHP versions must each web, CLI, worker, scheduled, development, test,
  and CI environment support? Ask when syntax, dependency, extension, or runtime
  behavior can differ across those targets.
- Which SAPI and web-server arrangement handles production requests, and does
  Apache run mod_php or proxy to PHP-FPM? Ask when request metadata, process
  lifecycle, permissions, or configuration scope affects future reviews.
- If FastCGI or PHP-FPM is used, which server parameters and trusted proxy rules
  establish script paths, HTTPS, host, client address, and other relied-on
  `$_SERVER` values?
- Which PHP extensions, native libraries, and version ranges are guaranteed in
  every applicable environment? Ask only for dependencies that change behavior
  or deployment feasibility.
- Which INI sources and pool overrides are authoritative for errors, sessions,
  uploads, encoding, locale, memory, execution time, OPcache, and preloading?
- Which processes are long-running, what state can survive between requests or
  jobs, and how are those processes drained, reset, restarted, and monitored?
- How do deployments coordinate web workers, queue workers, schedulers, database
  migrations, cached values, sessions, OPcache, and rollback while old and new
  code can coexist?
- Align existing domain questions with this deployment guidance when it is
  material: PHP version, SAPI, mod_php, FastCGI, PHP-FPM,
  worker, INI, proxy, session, cache, OPcache, rollout, and rollback coverage.
  Map the answers into named profiles. Do not repeat the core profile
  confirmation.

## Record in .grump

Record stable answers under `Technology and runtime`, separated by environment
when they differ. Record the web-server and SAPI path under `System boundaries`,
including the authority for request metadata. Record persistent process,
deployment, restart, session, cache, encoding, and rollback requirements under
the corresponding invariants or operational sections.

Identify repository paths, generated configuration, documentation, or explicit
user statements supporting each material fact. Create an `UNK-###` item only
when an unresolved PHP runtime, SAPI, extension, configuration, or lifecycle
decision could materially change future plan reviews.

Map existing PHP survey answers to the affected `DEP-###` profile. Reference a
shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

- Do not request or record secret values, session identifiers, private keys,
  tokens, credentials, production payloads, or raw environment dumps.
- Do not store a complete `phpinfo` output. Record only the material setting and
  its evidence location without copying sensitive server data.
- Do not treat one developer's CLI interpreter as proof of the production web or
  worker runtime.
- Do not record transient process identifiers, current memory use, temporary
  hostnames, or one-off debugging flags as doctrine.
- Do not promote a route-specific or plan-specific `$_SERVER` dependency into
  project doctrine unless it is a durable application contract.

## Re-survey triggers

Re-survey PHP context after a supported-version change, SAPI or web-server
change, PHP-FPM pool or worker-model change, extension or native-library change,
Composer platform-policy change, session or cache migration, OPcache or
preloading change, container or hosting migration, proxy trust change, or
material deployment and rollback redesign.
