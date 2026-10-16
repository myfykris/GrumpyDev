# Plan: live payment status from the Acme ledger

## Why

Finance wants payment status in the portal within minutes. Today it only
changes when the nightly SOAP refresh runs. The Acme ledger service now
publishes payment events, and Acme ships an official PHP client.

## Steps

1. `composer require acme/ledger-client:^2.0`. Version 2 adds webhook
   verification and typed models; it requires `php >= 8.1`. Set
   `config.platform.php` to `8.1` in composer.json so the lock file resolves.
2. Add `src/Service/PaymentSync.php` with a `readonly class PaymentEvent` and
   `enum PaymentStatus: string { case Paid = 'paid'; case Partial = 'partial';
   case Open = 'open'; }`, and map ledger statuses to it with a `match`.
3. Add `public/ledger-webhook.php`: verify the event with the client's
   `Webhook::verify()`, then update the invoice's status through
   `InvoiceService`.
4. Deploy with the usual FTP upload. Run `composer install --no-dev` locally
   and upload `vendor/` with the code.
5. Tests: PHPUnit tests for PaymentSync, run in the project's Docker image.

## Rollout

Ship on Friday; the webhook URL is registered with Acme after upload.
