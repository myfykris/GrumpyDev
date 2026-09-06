---
name: apache-http-server
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Apache HTTP Server engineering work for MPM behavior, virtual hosts, routing, modules, proxying, TLS, access control, headers, rewrites, PHP integration, limits, reload, and rollback."
---

# Apache HTTP Server GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the application
runtime, `application-security`, `performance-capacity`, and deployment skills.
Every installed companion that remains applicable to the project participates;
the reviewed target does not select the roster. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect Apache build and version, loaded modules and MPM, include tree,
  virtual hosts, listeners, proxies, rewrites, access rules, TLS, PHP
  integration, limits, logs, service configuration, and reload runbooks.

- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.

Watch especially for directives applied in the wrong context, rewrite loops or
surprising rule order, forwarded identity trusted from arbitrary clients, MPM
and module thread-safety mismatches, .htaccess drift, and graceful reloads
leaving old processes or configuration active.

Lean mode is insufficient when this material severity condition may apply:

- Treat remote code execution, access-control bypass, private-site exposure
  through default routing, or a reload/configuration path that creates an outage
  without recovery as critical or high according to blast radius and realistic
  likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/routing-proxy-and-php-integration.md):
  Read when the reviewed work directly or indirectly changes listeners, virtual hosts,
  default hosts, document roots,
  configuration merge order, htaccess, rewrites, proxying, forwarded headers, CGI,
  handlers, mod_php, FastCGI, PHP-FPM, script mapping, path info, or upstream timeouts.
- [Focused rules](references/tls-access-control-and-reload.md):
  Read when the reviewed work directly or indirectly changes TLS, certificates, client
  authentication, HSTS,
  authentication, authorization, filesystem access, module privileges, status endpoints,
  graceful reload, old workers, logs, or configuration rollback.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant MPM
choice, request routing, virtual hosts, modules, reverse proxying, TLS,
authentication, authorization, headers, rewrites, PHP integration, timeouts,
limits, logs, reload, and rollback, verification evidence, deployment and
recovery limits, and any material assumption that remains unresolved.
