# Agentic systems standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Make side effects idempotent or reconcile them by stable operation identity, with checkpoints
  before and after each effect.
- Bound turns, time, tokens, cost, tools, delegation depth, retries, and stalled work; define
  terminal and escalation states.
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
- Use representative high-capability reasoning models for review and evaluation, and record
  model, effort, prompt, and tool versions.

## Ask when evidence is missing

- Which agents, models, tools, authorities, approval points, budgets, memory, and delegation
  topology apply?
- How are goal hijack, tool misuse, identity, supply chain, code execution, memory poisoning,
  inter-agent trust, cascading failure, human approval, rogue behavior, audit, and recovery
  handled?

## Calibrate findings

- Downgrade when authority, budgets, effect identity, evaluations, approvals, audit, and
  recovery are enforced and tested.
