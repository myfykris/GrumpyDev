# Objective-C dynamic runtime, KVO, and notifications

Read this reference when the reviewed work directly or indirectly changes selectors,
forwarding, swizzling, categories,
associated objects, runtime registration, KVO, notifications, observer lifetime,
reentrancy, or dynamic callback ordering.

## Review requirements

- Review selectors, dynamic lookup, forwarding, swizzling, categories,
  associated objects, and runtime registration for collision, ordering, and
  discoverability. A category cannot safely add ordinary instance storage.

- Match KVO and notification registration to removal, lifetime, thread,
  reentrancy, and payload contracts. Check automatic versus manual KVO and
  whether an observer can see a partly updated invariant.
