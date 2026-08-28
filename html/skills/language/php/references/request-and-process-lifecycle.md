# PHP request and process lifecycle

Read this reference when the reviewed work directly or indirectly depends on a SAPI,
PHP-FPM, mod_php, CGI or FastCGI,
request metadata, server variables, proxy mapping, long-running workers, resident
application servers, persistent connections, output buffering, streaming, signals,
shutdown, cancellation, or process recycling.

## Request and process lifecycle

- Reject request-scoped assumptions in long-running workers. Static properties,
  singletons, global variables, locale, timezone, error handlers, open streams,
  database sessions, dependency-container instances, and library caches can
  survive into the next job or request.
- Require deterministic reset or process-recycle behavior for tenant, identity,
  transaction, tracing, and request-specific state. Garbage collection does not
  restore application invariants or close every external resource promptly.
- Check signal handling, graceful shutdown, job cancellation, time limits,
  memory limits, worker restarts, and partial cleanup. A killed worker can leave
  a remote operation committed even when PHP did not finish local handling.
- Verify output buffering, header construction, streaming, flush behavior, and
  client disconnect handling under the actual SAPI and reverse proxy.

## Verify the claims

- Exercise request metadata behind the real proxy and web-server arrangement,
  including HTTPS, host, port, path information, client address, forwarded
  headers, missing variables, and hostile values.


## Ask when evidence is missing

- If request metadata or routing affects correctness or security, ask which
  SAPI, web server, FastCGI or proxy mapping, trusted proxy rules, and exact
  `$_SERVER` values form the contract.
