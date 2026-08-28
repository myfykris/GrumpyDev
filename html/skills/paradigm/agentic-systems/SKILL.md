---
name: agentic-systems
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review agentic-system plans and other engineering artifacts for authority, tool boundaries, state, orchestration, termination, human approval, evaluation, observability, and recovery. Project applicability: an LLM or automated agent can select actions, call tools, or coordinate other agents."
---

# Agentic systems GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `llm-applications`,
`distributed-systems`, `dependency-supply-chain`, and `application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
