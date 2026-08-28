# Vite standard review

## Inspect additional evidence

- Inspect base path, asset URLs, public directory, aliases, dependency optimization, library
  mode, chunks, and plugin ordering.
- Review separate SSR and client builds, manifests, externalization, module conditions, source
  maps, and production serving.

## Establish the operating model

Establish the project target: Vite and plugin versions, framework and runtime, application or
library mode, environment types, browser targets, base path, asset policy, public variables,
aliases, dependency optimization, SSR entrypoints, output directories, source maps, and
production server.

The development server and vite preview are development inspection tools, not production serving
architecture. Client-prefixed environment values are compiled into browser code and must be
treated as public.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Run clean production builds from the actual workspace and inspect client, server, worker,
  assets, chunks, and source maps.
- Serve output under the real subpath and headers, then test direct navigation, lazy chunks,
  assets, older targets, and SSR.
- Compare clean CI behavior with warmed development caches and exercise plugin, dependency, and
  environment differences.

## Ask when evidence is missing

- Which Vite, framework plugins, runtime, package manager, environments, browser targets, and
  base path apply?
- How are public variables, SSR builds, assets, dependencies, plugins, production serving, and
  source maps handled?

## Calibrate findings

- Downgrade when environment boundaries, clean builds, base paths, targets, plugins, SSR, and
  production serving are tested.
