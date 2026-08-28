# PHP security and external input

Read this reference when the reviewed work directly or indirectly handles uploads,
paths, stream wrappers, sessions,
cookies, untrusted serialization, HTML or other output contexts, SQL or shell
boundaries, temporary files, client-visible errors, or security-sensitive logging.

## Security and external input

- Treat superglobals, uploaded-file metadata, environment variables, forwarded
  headers, cookies, sessions, and deserialized values as boundary input. Require
  context-specific HTML, attribute, URL, JavaScript, SQL, shell, and header
  handling rather than one generic escaping function.
- Reject unsafe native serialization of untrusted data. Account for object
  instantiation, magic methods, autoloading, gadget chains, and compatibility of
  stored serialized values during deployments.
- Check path normalization, stream wrappers, symbolic links, archive handling,
  upload moves, temporary-file permissions, and race conditions before file
  operations. An extension check on the original filename is not a filesystem
  security boundary.
- Verify session cookie attributes, fixation prevention, regeneration timing,
  concurrent request behavior, storage locking, logout invalidation, and secret
  rotation. Authorization must be re-established at the protected operation.
- Ensure production errors are not rendered to clients and that logs redact
  credentials, session identifiers, tokens, personal data, and raw payloads.
