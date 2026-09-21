---
name: gd-apache-http-server
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Apache HTTP Server engineering work for MPM behavior, virtual hosts, routing, modules, proxying, TLS, access control, headers, rewrites, PHP integration, limits, reload, and rollback."
---

# Apache HTTP Server GrumpyDev review

## Quick checks

- Inspect Apache build and version, loaded modules and MPM, include tree,
  virtual hosts, listeners, proxies, rewrites, access rules, TLS, PHP
  integration, limits, logs, service configuration, and reload runbooks.

Watch especially for directives applied in the wrong context, rewrite loops or
surprising rule order, forwarded identity trusted from arbitrary clients, MPM
and module thread-safety mismatches, .htaccess drift, and graceful reloads
leaving old processes or configuration active.

- Inspect remote code execution, access-control bypass, private-site exposure
  through default routing, or a reload/configuration path that creates an outage
  without recovery.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Apache HTTP Server
specialist.

- [Focused rules](references/routing-proxy-and-php-integration.md):
  Read when the work changes listeners, virtual hosts,
  default hosts, document roots,
  configuration merge order, htaccess, rewrites, proxying, forwarded headers, CGI,
  handlers, mod_php, FastCGI, PHP-FPM, script mapping, path info, or upstream timeouts.
- [Focused rules](references/tls-access-control-and-reload.md):
  Read when the work changes TLS, certificates, client
  authentication, HSTS,
  authentication, authorization, filesystem access, module privileges, status endpoints,
  graceful reload, old workers, logs, or configuration rollback.

## Verdict context

State the MPM choice, request routing, virtual hosts, modules, reverse
proxying, TLS, authentication, authorization, headers, rewrites, PHP
integration, timeouts, limits, logs, reload, and rollback, supporting evidence,
deployment or recovery limits, and unresolved material assumptions.
