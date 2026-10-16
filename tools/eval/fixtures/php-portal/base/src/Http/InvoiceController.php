<?php
namespace App\Http;

use App\Service\InvoiceService;

class InvoiceController
{
    private $invoices;

    public function __construct(InvoiceService $invoices)
    {
        $this->invoices = $invoices;
    }

    public function show(array $query): string
    {
        $invoice = $this->invoices->find($query['no'] ?? '');
        return json_encode([
            'number' => $invoice->number,
            'amount_cents' => $invoice->amountCents,
            'status' => $invoice->status,
        ]);
    }
}
