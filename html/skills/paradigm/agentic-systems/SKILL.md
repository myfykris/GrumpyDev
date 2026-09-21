---
name: gd-agentic-systems
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review agentic-system engineering work for authority, tool boundaries, state, orchestration, termination, human approval, evaluation, observability, and recovery."
---

# Agentic systems GrumpyDev review

## Quick checks

- Read agent goals, system instructions, tool schemas, orchestration code, memory, checkpoints,
  approval rules, and evaluators.

- Trace authority from user intent through planning, tool selection, arguments, external
  effects, delegation, and completion.

Watch especially for prompt content granting itself authority, recursive
delegation without budgets, retries repeating external effects, shared memory
mixing users, model fallback changing capabilities, persistent memory accepting
untrusted claims, agents forwarding credentials or authority to peers, generated
code escaping its boundary, approval applied after an irreversible step, and
success inferred from fluent text.

- Assess unauthorized external effects, credential escalation, cross-user memory leakage, or
  unbounded destructive action under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Agentic systems
specialist.

- [Focused rules](references/tool-authority-sandboxing-and-code-execution.md):
  Read when the work lets an agent invoke tools,
  change external state, execute generated code, use a browser or interpreter,
  access files or networks, receive credentials, or require human approval for
  consequential effects.
- [Focused rules](references/memory-data-and-supply-chain-trust.md):
  Read when the work adds or changes persistent memory,
  retrieval, feedback, durable
  observations, prompts, models, skills, tools, extensions, registries, or orchestration
  packages that can be poisoned, substituted, promoted, expired, or revoked.
- [Focused rules](references/delegation-inter-agent-trust-and-containment.md):
  Read when the work uses multiple agents, delegation,
  agent-to-agent messages,
  transferred work, shared budgets, peer identities, cascading failure, rogue-agent
  detection, emergency stopping, or cross-agent recovery.

## Verdict context

State agent goals and authority, identities, tool and approval matrix, memory trust, inter-agent
protocol, code sandbox, supply chain, effect-safety and cascade limits, termination and emergency
stop policy, evaluation evidence, and recovery path.
