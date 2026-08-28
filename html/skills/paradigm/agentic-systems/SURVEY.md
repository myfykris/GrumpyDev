# Agentic systems survey contribution

## Applicability

Apply this contribution when an LLM or automated agent can select actions, call tools,
or coordinate other agents. Skip it when this domain does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Agentic systems. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Agent roles and goals, model and effort policy, tool inventory,
  authority and approval matrix, state and memory model, delegation topology, budgets,
  termination rules, evaluation suite, observability, rollback, and incident ownership.
- Review doctrine: An agent may reason about an action without having authority to perform it.
  Every tool call must be constrained by explicit user intent, tool-level permissions, validated
  arguments, and an auditable effect boundary. Persistent memory and inter-agent messages remain
  untrusted until their provenance, scope, and authority are independently established.
- Deployment-profile facts: model providers and versions, effort settings,
  orchestration runtime, tool endpoints and permissions, memory stores, queues, sandboxes,
  budgets, evaluation gates, audit retention, and emergency disable controls.

## Ask only when materially unresolved

- Which agents, models, tools, authorities, approval points, budgets, memory, and delegation
  topology apply?
- How are goal hijack, tool misuse, identity, supply chain, code execution, memory poisoning,
  inter-agent trust, cascading failure, human approval, rogue behavior, audit, and recovery
  handled?

## Record in .grump

Record confirmed Agentic systems answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Agentic systems doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey agentic systems when the model or provider, tool set, permission boundary,
autonomy level, memory design, sandbox, approval policy, multi-agent topology, or
failure-containment policy materially changes. Also re-survey when evidence conflicts
with saved doctrine or the user requests a context refresh.
