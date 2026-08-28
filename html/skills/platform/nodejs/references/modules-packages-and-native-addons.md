# Node.js modules, packages, and native addons

Read this reference when the reviewed work directly or indirectly changes CommonJS or
ESM, package type, exports or
imports maps, loaders, conditional resolution, lockfiles, lifecycle scripts,
package-manager versions, native addons, optional platform packages, ABI, OS, architecture,
build output, or reproducible installation.

## Review requirements

- Choose CommonJS and ECMAScript module behavior deliberately. Verify package
  type, exports/imports maps, resolution, file extensions, conditional exports,
  dual-package state, loader hooks, build output, and test execution.

- Treat lockfiles, lifecycle scripts, native addons, optional dependencies,
  platform packages, and package-manager versions as build inputs. A successful
  developer install is not a reproducible deployment.

## Verify the claims

- Run the declared Node and package-manager versions on every supported OS and
  architecture from a clean locked install.
