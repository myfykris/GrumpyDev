# LLM applications survey contribution

## Applicability

Apply this contribution when application behavior depends on a generative model. Skip it when
LLM applications does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for LLM applications. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Model providers and versions, reasoning and effort policy, prompt
  sources and versioning, context and truncation policy, output schemas, retrieval and embedding
  stack, data classifications, retention, evaluations, safety controls, fallback behavior,
  budgets, and observability.
- Review doctrine: Model output is untrusted probabilistic data, even when structured. The
  application must validate it before it affects permissions, money, persistence, code
  execution, or external systems. System prompts and hidden context are not secrets or security
  controls, and retrieved or multimodal content can carry hostile instructions.
- Deployment-profile facts: model endpoints and regions, model and embedding versions,
  effort settings, prompt sources, retrieval stores, tool permissions, data retention, rate and
  cost limits, evaluation gates, observability, fallbacks, and kill switches.

## Ask only when materially unresolved

- Which models, versions, effort settings, prompts, schemas, retrieval, data classes, and
  provider regions apply?
- How are injection, hidden context, data and model poisoning, output validation, agency,
  retrieval isolation, evaluations, privacy, citations, consumption, observability, fallbacks,
  and rollback handled?

## Record in .grump

Record confirmed LLM applications answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable LLM applications doctrine. Do
not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey LLM applications when its version, target platform, execution model, trust boundary,
deployment topology, persistent state, update process, or recovery policy materially changes,
when evidence conflicts with saved doctrine, or when the user requests a context refresh.
