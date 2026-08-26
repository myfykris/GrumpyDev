# Vite survey contribution

## Applicability

Apply this contribution when a plan builds applications with vite. Skip it when Vite does not
constrain a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Vite. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Vite and plugin versions, framework and runtime, application or
  library mode, environment types, browser targets, base path, asset policy, public variables,
  aliases, dependency optimization, SSR entrypoints, output directories, source maps, and
  production server.
- Review doctrine: The development server and vite preview are development inspection tools,
  not production serving architecture. Client-prefixed environment values are compiled into
  browser code and must be treated as public.
- Deployment-profile facts: Vite and plugin versions, runtime and package manager,
  workspace root, environment prefixes, browser targets, base path, client and SSR entries,
  output directories, assets, source maps, headers, and production server.

## Ask only when materially unresolved

- Which Vite, framework plugins, runtime, package manager, environments, browser targets, and
  base path apply?
- How are public variables, SSR builds, assets, dependencies, plugins, production serving, and
  source maps handled?

## Record in .grump

Record confirmed Vite answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Vite doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Vite when its version, target platform, execution model, trust boundary, deployment
topology, persistent state, update process, or recovery policy materially changes, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
