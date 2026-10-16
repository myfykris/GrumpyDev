<?php
namespace Acme\Ledger;

final class Client
{
    public function __construct(private readonly string $baseUrl) {}

    public function notifyPaid(string $invoiceNo): void
    {
        $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 5]]);
        @file_get_contents($this->baseUrl . '/paid/' . rawurlencode($invoiceNo), false, $ctx);
    }
}
