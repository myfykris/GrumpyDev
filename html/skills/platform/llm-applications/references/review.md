# LLM applications full-review guidance

## Operating conditions

Establish the project target: Model providers and versions, reasoning and effort policy, prompt
sources and versioning, context and truncation policy, output schemas, retrieval and embedding
stack, data classifications, retention, evaluations, safety controls, fallback behavior,
budgets, and observability.

## Failure patterns

- Treat direct, indirect, multilingual, encoded, and multimodal prompt injection as an
  architectural trust-boundary problem. Label external content, keep it separate from control
  instructions, constrain resulting authority, and do not claim that filtering or retrieval alone
  solves injection.

## Verification to run or specify in the plan

- Exercise injection, conflicting instructions, missing context, stale retrieval, malformed
  output, hidden-context extraction, poisoned documents, cross-tenant retrieval, unsafe Markdown
  or code, provider outage, recursive work, timeout, and quota.
