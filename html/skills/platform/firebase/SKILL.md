---
name: gd-firebase
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Firebase engineering work for Security Rules, identity, client trust, Firestore consistency, offline writes, Cloud Functions, Storage, indexes, quotas, and deployment."
---

# Firebase GrumpyDev review

## Quick checks

- Read Firebase products, SDK and rules versions, project aliases, emulator configuration,
  indexes, functions, and deployment files.

- Trace user identity, custom claims, App Check, Security Rules, Admin SDK use, service
  accounts, and tenant boundaries.

Watch especially for open development rules reaching production, broad
overlapping rules granting access, Admin SDK endpoints without equivalent
authorization, custom claims remaining stale, offline writes resolving
last-write-wins, and triggers repeating non-idempotent effects.

- Assess open rules, tenant-crossing access, exposed service accounts, or privileged Admin
  endpoints without authorization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Firebase
specialist.

## Verdict context

State products, project separation, rule and identity boundaries, data and query model, offline
policy, trigger safety, and deployment evidence.
