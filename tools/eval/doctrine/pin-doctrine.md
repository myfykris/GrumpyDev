## Purpose
Customer invoice portal for one client (Northwind Supply). It shows invoices and payment status from the vendor's SOAP billing API.

## Constraints
- CON-001: Production runs PHP 7.4 on the client's server and cannot be upgraded: the client's licensed ionCube-encoded reporting module only loads on PHP 7.4. All code, including dependencies, must run on PHP 7.4. The local Docker image uses PHP 8.2 for convenience only.
- CON-002: The vendor's SOAP billing API is mandatory; the vendor has no REST API.

## Accepted decisions
- DEC-001: Deployment is an FTP upload to the client's server. No containers in production.

## Known debt
- DEBT-001: src/Legacy/SoapGateway.php is known debt (static client, no timeouts, raw stdClass results). Do not report it.
