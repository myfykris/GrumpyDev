---
name: agentic-systems
description: Review agentic-system plans for authority, tool boundaries, state, orchestration, termination, human approval, evaluation, observability, and recovery. Use when an LLM or automated agent can select actions, call tools, or coordinate other agents.
---

# Agentic systems plan review

Apply this guidance alongside the core GrumpyDev review and the `llm-applications`,
`distributed-systems`, `dependency-supply-chain`, and `application-security` skills.

## Inspect evidence

- Read agent goals, system instructions, tool schemas, orchestration code, memory, checkpoints,
  approval rules, and evaluators.
- Trace authority from user intent through planning, tool selection, arguments, external
  effects, delegation, and completion.
- Identify state owners, retry boundaries, duplicate effects, budgets, termination rules, model
  fallbacks, and recovery paths.
- Inspect prompt-injection defenses, data trust labels, sandboxing, credential scope, audit
  records, and human override.

## Establish the operating model

Establish the project target: Agent roles and goals, model and effort policy, tool inventory,
authority and approval matrix, state and memory model, delegation topology, budgets, termination
rules, evaluation suite, observability, rollback, and incident ownership.

An agent may reason about an action without having authority to perform it. Every tool call must
be constrained by explicit user intent, tool-level permissions, validated arguments, and an
auditable effect boundary.

## Challenge the plan

### Recurring traps

Watch especially for prompt content granting itself authority, recursive delegation without
budgets, retries repeating external effects, shared memory mixing users, model fallback changing
capabilities, persistent memory accepting untrusted claims, agents forwarding credentials or
authority to peers, generated code escaping its boundary, approval applied after an irreversible
step, and success inferred from fluent text.

- Define an allowlist of actions per role and require approval before external, destructive,
  financial, privacy-sensitive, or privilege-changing effects.
- Treat tool output and retrieved content as untrusted data; prevent it from overriding system
  policy or expanding authority.
- Keep the user-approved goal, policy, and authority outside untrusted context. Detect goal
  substitution, conflicting objectives, hidden instructions, and delegated tasks that widen the
  original scope.
- Give each agent and tool a distinct, least-privilege, short-lived identity. Reauthorize each
  operation for its current user, tenant, purpose, and target; never infer that delegation also
  transfers the delegator's credentials or full authority.
- Treat models, prompts, skills, tools, extensions, agent registries, memory sources, and
  orchestration packages as a supply chain. Pin approved identities and versions, review changes,
  define disable and rollback controls, and detect capability or description drift.
- Sandbox generated code, interpreters, browsers, file access, network access, and tool plugins.
  Validate commands and artifacts outside the model, bound resources, and assume model-produced
  code is attacker-influenced until proven otherwise.
- Give persistent memory explicit provenance, trust, tenant, expiry, deletion, and promotion
  rules. Quarantine untrusted observations, prevent one result from becoming durable policy, and
  require review before memory can expand future authority.
- Authenticate, authorize, schema-validate, and correlate inter-agent messages. Treat peer names,
  claims, plans, tool results, completion notices, and instructions as untrusted; prevent spoofed
  agents, replay, confused-deputy action, and authority laundering.
- Make side effects idempotent or reconcile them by stable operation identity, with checkpoints
  before and after each effect.
- Bound turns, time, tokens, cost, tools, delegation depth, retries, and stalled work; define
  terminal and escalation states.
- Contain cascading failures with circuit breakers, per-agent and global budgets, dependency and
  delegation limits, partial-result handling, rollback or compensation, and an independently
  enforceable emergency stop.
- Detect an agent that deviates from its assigned goal, policy, identity, or normal capability
  use with controls outside that agent. Revoke its credentials, stop delegation and side effects,
  quarantine its memory and outputs, preserve evidence, and reconcile completed work.
- Make human approvals show the actual actor, target, data, permission, effect, and uncertainty.
  Do not use confident model summaries, notification fatigue, or an ambiguous button as proof of
  informed authorization.
- Evaluate task success, policy compliance, tool choice, argument safety, refusal, recovery,
  and adversarial inputs separately.
- Preserve an audit trail that connects user intent, model decision, approval, tool request,
  result, and final claim.

## Verify the claims

- Run deterministic fixtures for normal, denied, ambiguous, injected, repeated, timed-out, and
  partially completed work.
- Simulate model and tool failure, reordered callbacks, duplicated results, stale memory,
  interrupted approvals, and restart.
- Exercise goal hijack, tool misuse, identity escalation, poisoned memory, changed tool
  descriptions, unexpected code, spoofed inter-agent messages, cascading failure, misleading
  approval summaries, and emergency disable across restart and model fallback.
- Use representative high-capability reasoning models for review and evaluation, and record
  model, effort, prompt, and tool versions.

## Ask when evidence is missing

- Which agents, models, tools, authorities, approval points, budgets, memory, and delegation
  topology apply?
- How are goal hijack, tool misuse, identity, supply chain, code execution, memory poisoning,
  inter-agent trust, cascading failure, human approval, rogue behavior, audit, and recovery
  handled?

## Calibrate findings

- Treat unauthorized external effects, credential escalation, cross-user memory leakage, or
  unbounded destructive action as critical.
- Downgrade when authority, budgets, effect identity, evaluations, approvals, audit, and
  recovery are enforced and tested.

## Add to the verdict

State agent goals and authority, identities, tool and approval matrix, memory trust, inter-agent
protocol, code sandbox, supply chain, effect-safety and cascade limits, termination and emergency
stop policy, evaluation evidence, and recovery path.
