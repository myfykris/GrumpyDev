# Agentic systems full-review guidance

## Operating conditions

Establish the project target: Agent roles and goals, model and effort policy, tool inventory,
authority and approval matrix, state and memory model, delegation topology, budgets, termination
rules, evaluation suite, observability, rollback, and incident ownership.

## Failure patterns

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

## Verification to run or specify in the plan

- Run deterministic fixtures for normal, denied, ambiguous, injected, repeated, timed-out, and
  partially completed work.
- Simulate model and tool failure, reordered callbacks, duplicated results, stale memory,
  interrupted approvals, and restart.
- Use representative high-capability reasoning models for review and evaluation, and record
  model, effort, prompt, and tool versions.
