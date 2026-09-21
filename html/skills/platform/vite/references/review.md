# Vite full-review guidance

## Operating conditions

Establish the project target: Vite and plugin versions, framework and runtime, application or
library mode, environment types, browser targets, base path, asset policy, public variables,
aliases, dependency optimization, SSR entrypoints, output directories, source maps, and
production server.

## Failure patterns

- Classify every environment value and module by client, server, worker, build, or shared
  execution before bundling.
- Set and test the actual base path, asset URLs, redirects, fallback behavior, module preload,
  and cache headers.
- Require separate client and SSR entrypoints and outputs when SSR applies, with compatible
  manifests and externalization.
- Pin and review plugins, transforms, virtual modules, dependency optimization, module
  conditions, and supply-chain changes.
- Define browser targets and polyfill policy based on supported clients; Vite does not add
  arbitrary compatibility automatically.
- Use a real production server or adapter for runtime evidence and inspect source maps, public
  files, and artifact contents.

## Verification to run or specify in the plan

- Run clean production builds from the actual workspace and inspect client, server, worker,
  assets, chunks, and source maps.
- Serve output under the real subpath and headers, then test direct navigation, lazy chunks,
  assets, older targets, and SSR.
- Compare clean CI behavior with warmed development caches and exercise plugin, dependency, and
  environment differences.
