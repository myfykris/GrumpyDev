<!-- BEGIN GRUMPYDEV CONSTRAINTS: generated from .grump; edit .grump, then run Grump sync -->
- Write all code, and choose all dependencies, for PHP 7.4: production runs
  PHP 7.4 and cannot be upgraded, because the client's licensed ionCube module
  only loads on 7.4. The local Docker image runs PHP 8.2 for convenience only.
- Use the vendor's SOAP billing API; the vendor has no REST API.
- Deployment is an FTP upload to the client's server; no containers in
  production.
<!-- END GRUMPYDEV CONSTRAINTS -->
