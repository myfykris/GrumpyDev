<?php
namespace App\Service;

use App\Domain\Invoice;
use App\Legacy\SoapGateway;

class InvoiceService
{
    private $gateway;

    public function __construct(SoapGateway $gateway)
    {
        $this->gateway = $gateway;
    }

    public function find(string $invoiceNo): Invoice
    {
        $raw = $this->gateway->getInvoice($invoiceNo);
        return new Invoice(
            (string) $raw->Number,
            (string) $raw->CustomerRef,
            (int) round(((float) $raw->Amount) * 100),
            (string) $raw->Status
        );
    }
}
