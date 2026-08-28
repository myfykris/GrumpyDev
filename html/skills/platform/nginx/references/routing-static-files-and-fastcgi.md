# Nginx routing, static files, and FastCGI

Read this reference when the reviewed work directly or indirectly changes listen or
server-name selection, default
servers, location matching, rewrites, internal redirects, URI normalization, root,
alias, static file access, symlinks, try_files, MIME behavior, FastCGI, PHP-FPM, script
mapping, path info, or request metadata.

## Review requirements

- Trace listen-address and server-name selection, including the default server
  for every socket. Unknown or malformed hosts must not fall into a sensitive
  application.

- Evaluate exact, prefix, regular-expression, named, and nested location
  matching plus internal redirects. Configuration order and URI normalization
  can route a request differently than the visual layout suggests.

- For static files, verify `root` versus `alias`, trailing slashes, normalized
  paths, symlinks, index and try-files redirects, error pages, MIME types,
  ranges, and cache headers without exposing private files.

- For proxy and FastCGI traffic, define URI rewriting, upstream identity, Host
  and forwarded headers, client IP trust, connection reuse, retries, timeouts,
  body limits, buffering, streaming, cancellation, and temporary-file behavior.

- For PHP-FPM, prove the script filename and path-info mapping from the
  normalized request to an existing intended file. Never let user-controlled
  path construction select arbitrary scripts.

## Verify the claims

- Test path normalization, root/alias behavior, static/private file separation,
  forwarded headers, limits, caching, and PHP script mapping.
