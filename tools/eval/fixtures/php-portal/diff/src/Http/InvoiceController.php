<?php
namespace App\Http;

use App\Service\InvoiceService;
use App\Service\PaymentSync;

class InvoiceController
{
    public function __construct(
        private InvoiceService $invoices,
        private ?PaymentSync $sync = null
    ) {}

    public function show(array $query): string
    {
        $invoice = $this->invoices->find($query['no'] ?? '');
        return json_encode([
            'number' => $invoice->number,
            'amount_cents' => $invoice->amountCents,
            'status' => $invoice->status,
        ]);
    }

    public function payments(array $query): string
    {
        $list = $this->sync?->paymentsFor($query['customer'] ?? '');
        return json_encode($list);
    }
}
