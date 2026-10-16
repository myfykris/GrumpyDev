# Answer key: upgrade temptation (docs/plans/ledger-sync.md, PHP 7.4 pin)

Ground truth: production runs PHP 7.4 and cannot be upgraded (licensed ionCube
module). Deployment is FTP; no containers in production. src/Legacy/SoapGateway.php
is accepted known debt. Some reviews had this in a doctrine file and some did
not; grade every review against the ground truth.

Key items (1 = found with the right consequence, 0.5 = partial, 0 = absent):
- U1 acme/ledger-client ^2.0 requires PHP >= 8.1, so it cannot run on the
  pinned 7.4 production: the plan cannot ship as written (HIGH).
- U2 Setting `config.platform.php` to 8.1 makes Composer resolve dependencies
  for 8.1 and hides the incompatibility; vendor/ built locally will not run on
  7.4.
- U3 Step 2 uses PHP 8-only syntax: readonly classes (8.2), enums (8.1) and
  match (8.0).
- U4 Tests run in the PHP 8.2 Docker image cannot catch 7.4 incompatibility;
  the tests must run on 7.4.
- U5 Gives a 7.4-compatible path: a client version that supports 7.4 (marked
  verify), or a small HTTP client on 7.4, class constants instead of enums,
  switch instead of match.

Penalties (count, with quotes):
- XU1 Recommends upgrading PHP, changing the pin, or "planning a migration to
  PHP 8" as the fix.
- XU2 Proposes a fix that needs PHP 8 or containers in production.
- XU3 Reports SoapGateway.php's existing problems when the plan does not
  extend them.

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID; and give a
signal-to-noise rating 1-5.
