# Apache TLS, access control, and reload

Read this reference when the reviewed work directly or indirectly changes TLS,
certificates, client authentication,
HSTS, authentication, authorization, filesystem access, module privileges, status
endpoints, graceful reload, old workers, logs, or configuration rollback.

## Review requirements

- Keep authentication and authorization ordering, filesystem access, symlink
  rules, CGI or handler execution, upload paths, status endpoints, and module
  privileges least-authority.

- Match TLS protocols, ciphers, certificates, OCSP behavior, client
  authentication, HTTP versions, redirects, HSTS, and backend encryption to the
  actual termination boundaries.

- Validate configuration before a graceful reload, then account for
  old-generation connections, changed certificates, module state, log
  descriptors, stuck requests, and rollback to the previous known-good include
  tree.

## Verify the claims

- Run configuration validation and rehearse graceful reload, rollback,
  long-lived requests, backend loss, and certificate rotation.
