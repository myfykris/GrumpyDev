# Agentic tool authority, sandboxing, and code execution

Read this reference when the reviewed work directly or indirectly lets an agent
invoke tools, change external state, execute generated code, use a browser or
interpreter, access files or networks, receive credentials, or require human
approval for consequential effects.

## Review requirements

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

- Sandbox generated code, interpreters, browsers, file access, network access, and tool plugins.
  Validate commands and artifacts outside the model, bound resources, and assume model-produced
  code is attacker-influenced until proven otherwise.
