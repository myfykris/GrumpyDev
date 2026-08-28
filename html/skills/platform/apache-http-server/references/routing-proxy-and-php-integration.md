# Apache routing, proxying, and PHP integration

Read this reference when the reviewed work directly or indirectly changes listeners,
virtual hosts, default hosts,
document roots, configuration merge order, htaccess, rewrites, proxying, forwarded
headers, CGI, handlers, mod_php, FastCGI, PHP-FPM, script mapping, path info, or
upstream timeouts.

## Review requirements

- Trace address/port listeners, name-based virtual-host selection, defaults,
  aliases, document roots, directory rules, and forwarded host behavior. Unknown
  hosts must not fall into a sensitive site accidentally.

- Review configuration merge and override order across server, virtual host,
  directory, location, files, includes, and `.htaccess`. Prohibit
  user-controlled overrides unless their cost and authority are intentional.

- Analyze proxy routing, URI normalization, path joining, WebSocket or streaming
  behavior, connection reuse, request and response buffering, retries, timeouts,
  body limits, and trusted forwarded headers.

- For PHP, distinguish mod_php from proxy/FastCGI arrangements and ensure MPM
  compatibility, script filename mapping, path info, environment variables,
  timeouts, process ownership, and error isolation.

## Verify the claims

- Dump the effective virtual-host and module configuration and test routing for
  expected, unknown, malformed, HTTP, and HTTPS hosts.
