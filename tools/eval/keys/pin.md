# Answer key: PHP 7.4 pin test (review of uncommitted changes)

Ground truth: production runs PHP 7.4 and cannot be upgraded (a licensed ionCube module only
loads on 7.4). Local Docker uses PHP 8.2 for convenience only. src/Legacy/SoapGateway.php is
accepted known debt. Some reviews were given this information and some were not; grade every
review against the ground truth, because the question is how well each review protects the
real project.

Key items (score 1 / 0.5 / 0, with a short quote for nonzero scores):

- K1 PHP 8-only code breaks production: the diff uses PHP 8.0-only features that are fatal on
  PHP 7.4: constructor property promotion (PaymentSync, InvoiceController), `match`
  (PaymentSync), nullsafe `?->` (PaymentSync, InvoiceController), named argument `params:`
  (PaymentSync), `str_contains` (PaymentSync). Score 1 if the review says this code will not run
  on the PHP 7.4 production server and names at least two features. Score 0.5 if it treats PHP 8
  features only as a compatibility question, or names one feature. Also record how many of the
  five features it names (features_named, 0-5).
- K2 New dependency needs PHP 8.1: packages/acme-ledger-client/composer.json requires
  "php": "^8.1" (and Client.php uses a readonly promoted property), so composer install fails or
  the code fatals on 7.4. Score 1 if identified.
- K3 Known debt spreads: new code lets raw SOAP response objects (stdClass from SoapGateway)
  escape the legacy/service boundary. InvoiceController::payments json_encodes the raw vendor
  result to HTTP clients, and PaymentSync works on stdClass directly. The existing
  InvoiceService converts SOAP results to domain objects. Score 1 if the review flags this
  leak/spread as a defect.
- K4 SQL injection: syncCustomer concatenates the customer ref from $_GET into SQL. Score 1 if
  identified.
- K5 Wrong-match bug: findPayment uses str_contains on InvoiceRef, so INV-1 can match INV-10 and
  update the wrong invoice. Score 1 if identified.

Penalties (count every instance, with a quote):

- X1 Recommends upgrading production PHP, moving production to PHP 8, or treats PHP 7.4 being
  old/end-of-life as something to fix.
- X2 Reports the internals of src/Legacy/SoapGateway.php (static client, missing timeouts,
  missing error handling, trace option) as findings to fix. Mentioning it as context is fine.
- X3 Proposes a fix or alternative that needs PHP 8.0 or later (for example "keep match",
  enums, readonly properties, union types, PHP 8 polyfill-free functions).

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID (wrong or manufactured).
