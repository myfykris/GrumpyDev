# Firebase survey contribution

## Applicability

Apply this contribution when a plan relies on firebase services. Skip it when Firebase does not
constrain a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Firebase. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Firebase products and SDKs, projects per environment,
  Authentication providers and tenant model, Security Rules ownership and versions, Admin SDK
  boundaries, Firestore model and indexes, offline policy, functions runtime and region, Storage
  layout, quotas, and deployment process.
- Review doctrine: Client SDK calls are authorized by deployed Security Rules, while trusted
  Admin SDK code bypasses those rules. Query rules are not post-query filters, so planned
  queries must satisfy their authorization constraints.
- Deployment-profile facts: Firebase projects and aliases, product regions, SDK and
  rules versions, indexes, functions runtime and concurrency, Storage rules, service accounts,
  secrets, emulator limits, quotas, billing alerts, and deployment targets.

## Ask only when materially unresolved

- Which Firebase products, SDKs, projects, identity providers, tenant model, rules, and Admin
  SDK boundaries apply?
- How are queries, indexes, offline conflicts, functions retries, Storage, quotas, backups,
  deployment, and rollback handled?

## Record in .grump

Record confirmed Firebase answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Firebase doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Firebase when its version, target platform, execution model, trust boundary,
deployment topology, persistent state, update process, or recovery policy materially changes,
when evidence conflicts with saved doctrine, or when the user requests a context refresh.
