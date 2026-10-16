# invoice-portal

Customer invoice portal for Northwind Supply (one client).

- `public/index.php` routes requests to `src/Http/*Controller.php`.
- Billing data comes from the vendor's SOAP API through `src/Legacy/SoapGateway.php`.
- Local development: `docker build -t portal . && docker run -p 8080:8080 portal` (PHP 8.2 image).
- Deployment: files are uploaded to the client's server by FTP.
