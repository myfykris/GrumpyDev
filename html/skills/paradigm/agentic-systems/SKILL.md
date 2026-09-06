---
name: agentic-systems
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review agentic-system engineering work for authority, tool boundaries, state, orchestration, termination, human approval, evaluation, observability, and recovery."
---

# Agentic systems GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `llm-applications`,
`distributed-systems`, `dependency-supply-chain`, and `application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat unauthorized external effects, credential escalation, cross-user memory leakage, or
  unbounded destructive action as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/tool-authority-sandboxing-and-code-execution.md):
  Read when the reviewed work directly or indirectly lets an agent invoke tools,
  change external state, execute generated code, use a browser or interpreter,
  access files or networks, receive credentials, or require human approval for
  consequential effects.
- [Focused rules](references/memory-data-and-supply-chain-trust.md):
  Read when the reviewed work directly or indirectly adds or changes persistent memory,
  retrieval, feedback, durable
  observations, prompts, models, skills, tools, extensions, registries, or orchestration
  packages that can be poisoned, substituted, promoted, expired, or revoked.
- [Focused rules](references/delegation-inter-agent-trust-and-containment.md):
  Read when the reviewed work directly or indirectly uses multiple agents, delegation,
  agent-to-agent messages,
  transferred work, shared budgets, peer identities, cascading failure, rogue-agent
  detection, emergency stopping, or cross-agent recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State agent goals and authority, identities, tool and approval matrix, memory trust, inter-agent
protocol, code sandbox, supply chain, effect-safety and cascade limits, termination and emergency
stop policy, evaluation evidence, and recovery path.
