# Application cryptography, abuse, and incident response

Read this reference when the reviewed work directly or indirectly changes encryption,
hashing, signatures, tokens, key
management, secret rotation, rate limits, automation abuse, fail-closed behavior,
security logs, vulnerability response, patch ownership, alerts, or incident handling.

## Review requirements

- Use established cryptographic libraries and protocols; reject custom
  encryption, token formats, password hashing, or signature rules.

- Make exceptional and dependency failures fail closed at security boundaries.
  Roll back partial effects, avoid success from incomplete authorization or
  validation, return non-sensitive client errors, and correlate them to useful
  internal diagnostics.

- Demand a hardened production baseline, safe logs and alerts, vulnerability
  response, key rotation, dependency patch ownership, and tests for the
  highest-impact abuse paths.

## Verify the claims

- Exercise invalid and rotated keys, unavailable key or identity services,
  malformed ciphertext and signatures, replay, partial effects, abusive request
  rates, security-log failure and a representative compromise from detection
  through containment, revocation, repair and recovery.
