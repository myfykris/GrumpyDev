# CI/CD standard review

## Establish the operating model

Establish the project target: CI/CD platform, runner trust and OS, branch and
approval policy, artifact flow, environments, credential model, deployment
ownership, and retention. The changed boundary must define: Trigger and trust
boundaries, reproducibility, artifacts, credentials, environments, approvals,
concurrency, caching, provenance, rollback, and failure recovery.

Identify the authoritative workflow, runner image, dependency inputs, artifact,
promotion record, credential issuer, protected environment, approval, and
rollback owner. Trace untrusted code and output through caches, artifacts,
identity requests, logs, and reusable workflows, and prove that only the
reviewed artifact can cross into a more privileged environment.

## Challenge the reviewed work

### Recurring traps

- Minimize token and runner permissions by job; forked or pull-request code must
  not inherit release credentials.
- Prefer short-lived workload identity bound to repository, workflow,
  environment, and job over stored broad credentials. Prevent untrusted code,
  dependencies, test output, or generated artifacts from influencing credential
  requests or protected approvals.
- Require pinned toolchains and reproducible artifacts; do not rebuild different
  bytes for each environment.
- Treat caches and artifacts as integrity boundaries with explicit keys,
  retention, access, and poisoning controls.
- Separate verification from promotion, protect production environments,
  serialize conflicting deploys, and preserve an auditable approval trail.
- Protect workflow definitions, reusable automation, runner images, release
  metadata, signing authority, and deployment configuration with review and
  least privilege. Treat logs, annotations, environment files, and command
  outputs from builds as untrusted data.
- Isolate or reset self-hosted runners between trust domains. Do not let an
  untrusted change leave processes, files, credentials, containers, caches, or
  network access for a later privileged job.
- Attach provenance or signatures to the verified artifact when supported, and
  verify that identity at promotion. Build once, then promote that exact
  artifact through protected environments.
- Prove rollback or roll-forward against schema changes, background jobs,
  feature flags, and mixed-version traffic.

## Verify the claims

- Rebuild the same revision in clean runners and compare the resolved inputs,
  artifacts, metadata and attestations that promotion will trust.
- Test trigger, branch, fork, workflow-change, environment, approval, identity,
  cache and artifact boundaries with the effective platform permissions.
- Interrupt concurrent builds and deployments, expire credentials, reject an
  approval, corrupt a cache or artifact, fail provenance verification and
  perform rollback using the documented operator path.
- Exercise untrusted pull requests, changed workflow files, malicious test
  output, poisoned caches, persistent runner state, expired identities,
  concurrent deploys, rejected promotion, signature failure, and rollback.

## Ask when evidence is missing

- Which triggers can run untrusted changes, and which credentials or protected
  environments can those runs reach?
- Is one verified artifact promoted across environments, and what restores
  service after a failed release?

## Calibrate findings

- Downgrade when triggers, permissions, promotion, and rollback are isolated and
  demonstrated by the workflow evidence.
