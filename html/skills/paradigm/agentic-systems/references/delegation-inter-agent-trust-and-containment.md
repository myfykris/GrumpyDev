# Agentic delegation, inter-agent trust, and containment

Read this reference when the reviewed work directly or indirectly uses multiple agents,
delegation, agent-to-agent
messages, transferred work, shared budgets, peer identities, cascading failure,
rogue-agent detection, emergency stopping, or cross-agent recovery.

## Review requirements

- Authenticate, authorize, schema-validate, and correlate inter-agent messages. Treat peer names,
  claims, plans, tool results, completion notices, and instructions as untrusted; prevent spoofed
  agents, replay, confused-deputy action, and authority laundering.

- Contain cascading failures with circuit breakers, per-agent and global budgets, dependency and
  delegation limits, partial-result handling, rollback or compensation, and an independently
  enforceable emergency stop.

- Detect an agent that deviates from its assigned goal, policy, identity, or normal capability
  use with controls outside that agent. Revoke its credentials, stop delegation and side effects,
  quarantine its memory and outputs, preserve evidence, and reconcile completed work.

## Verify the claims

- Exercise goal hijack, tool misuse, identity escalation, poisoned memory, changed tool
  descriptions, unexpected code, spoofed inter-agent messages, cascading failure, misleading
  approval summaries, and emergency disable across restart and model fallback.
