# Tailwind CSS survey contribution

## Applicability

Apply this contribution when a plan changes tailwind configuration or utility-based styling.
Skip it when Tailwind CSS does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Tailwind CSS. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Tailwind version, framework and build integration, source roots,
  monorepo working directory, theme tokens, plugins, class-generation conventions, browser
  targets, CSS ordering, and performance budgets.
- Review doctrine: Tailwind scans source text, not runtime values. Every class needed in
  production must appear in detectable source or an explicit source or safelist rule.
- Conditional deployment boundary: Tailwind and plugin versions, CSS entrypoints,
  source roots and working directory, framework plugin, theme and mode settings, browser
  targets, asset paths, minification, and build command.

## Ask only when materially unresolved

- Which Tailwind version, framework integration, source roots, theme tokens, plugins, and
  browser targets apply?
- How are dynamic variants, shared packages, production scanning, accessibility states, CSS
  ordering, and size verified?

## Record in .grump

Record confirmed Tailwind CSS answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Tailwind CSS doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Tailwind CSS when its version, target platform, rendering or execution model, trust
boundary, deployment adapter, persistent state, update process, or recovery policy materially
changes, when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
