# shadcn/ui survey contribution

## Applicability

Apply this contribution when a plan copies or updates shadcn/ui components or registries. Skip
it when shadcn/ui does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
shadcn/ui. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: shadcn/ui generation version and configuration, framework,
  registries, primitive libraries, styling and icon systems, component ownership, update policy,
  accessibility targets, and accepted local divergence.
- Review doctrine: Installed components are application source code, not a centrally upgraded
  binary library. The project owns their behavior, security, accessibility, tests, and future
  merges.
- Conditional deployment boundary: framework and renderer, component configuration,
  registry sources, primitive versions, styling pipeline, asset sources, browser targets, CSP
  constraints, and build output.

## Ask only when materially unresolved

- Which shadcn/ui setup, framework, registries, primitives, styling system, and local component
  modifications apply?
- Who owns registry trust, source review, upgrades, accessibility, design tokens, and merge
  behavior?

## Record in .grump

Record confirmed shadcn/ui answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable shadcn/ui doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey shadcn/ui when its version, target platform, rendering or execution model, trust
boundary, deployment adapter, persistent state, update process, or recovery policy materially
changes, when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
