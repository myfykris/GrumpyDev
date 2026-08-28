---
name: nginx
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Nginx plans and other engineering artifacts for request processing, location matching, proxy and FastCGI behavior, TLS, buffering, streaming, caching, timeouts, limits, headers, static files, reload, logging, and failover. Project applicability: the project serves or routes traffic through Nginx, or Nginx behavior constrains a supported environment."
---

# Nginx GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the application
runtime, `application-security`, `performance-capacity`, and deployment skills.
Every installed companion that remains applicable to the project participates;
the reviewed target does not select the roster. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect Nginx version and modules, full include tree, listeners and server
  blocks, locations, maps, upstreams, proxy or FastCGI settings, TLS, caches,
  limits, logs, service configuration, and reload runbooks.

- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.

Watch especially for location precedence selecting the wrong handler, proxy_pass
rewriting URIs unexpectedly, buffering breaking streaming, client identity
trusted from unbounded proxies, timeout mismatches across layers, static files
bypassing intended controls, and reloads retaining old workers or sockets.

Lean mode is insufficient when this material severity condition may apply:

- Treat arbitrary script execution, private-file exposure, authentication/cache
  cross-tenant leakage, default-host exposure, or a configuration change that
  causes an unrecoverable outage as critical or high according to blast radius
  and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/routing-static-files-and-fastcgi.md):
  Read when the reviewed work directly or indirectly changes listen or server-name
  selection, default servers, location
  matching, rewrites, internal redirects, URI normalization, root, alias, static file
  access, symlinks, try_files, MIME behavior, FastCGI, PHP-FPM, script mapping, path
  info, or request metadata.
- [Focused rules](references/proxy-streaming-caching-and-tls.md):
  Read when the reviewed work directly or indirectly changes reverse proxying, upstream
  identity, forwarded headers,
  retries, timeouts, buffering, streaming, cancellation, cache keys, invalidation, stale
  behavior, TLS, certificates, HTTP versions, HSTS, backend encryption, graceful reload,
  old workers, or rollback.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
request phases, location matching, reverse proxying, FastCGI, TLS, buffering,
streaming, caching, timeouts, limits, headers, static files, reload, logging,
and failover, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
