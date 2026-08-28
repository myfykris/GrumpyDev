# Python packaging, native code, and deployment

Read this reference when the reviewed work directly or indirectly changes interpreter
implementation or version,
packaging, lock or resolver tooling, imports, optional dependencies, virtual
environments, generated files, native extensions, OS or architecture targets, build
artifacts, or deployment environment behavior.

## Review requirements

- Check package/version compatibility across local development, CI, build
  images, and production. Reject plans that assume an undeclared dependency is
  present.

## Verify the claims

- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.


## Ask when evidence is missing

- Which Python version and implementation, target platforms, dependency
  resolver, and packaging mode apply?
