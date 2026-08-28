# Kubernetes networking, identity, and secrets

Read this reference when the reviewed work directly or indirectly changes Services,
Ingress, Gateway API, DNS, network
policy, service accounts, RBAC, workload identity, pod security, secrets, certificate
rotation, external exposure, or operator access.

## Networking, identity, and secrets

- Map ingress or gateway, service, endpoint, DNS, proxy, egress, network-policy,
  and load-balancer behavior. Define source identity, forwarded-header trust,
  TLS termination, timeouts, retries, body limits, and connection lifetime.
- Use least-privilege service accounts and workload identity. Avoid node-wide
  credentials, default service accounts, unnecessary token mounts, and broad
  cloud or Kubernetes roles.
- Set pod and container security context deliberately: user and group IDs,
  filesystem ownership, capabilities, privilege escalation, seccomp, root
  filesystem mutability, host namespaces, host paths, and device access.
- Treat Secrets as an injection and access mechanism, not automatic encryption
  or rotation. Define source, encryption, RBAC, mount/environment exposure,
  refresh behavior, process reload, revocation, and log redaction.
- Require network policy semantics that match the installed implementation and
  cover DNS and necessary control traffic. A policy object unsupported by the
  cluster network plugin provides no isolation.

## Verify the claims

- Exercise identity, RBAC, network, pod-security, and secret boundaries with
  denied as well as allowed actions.
