<?php
namespace App\Domain;

class Invoice
{
    /** @var string */
    public $number;
    /** @var string */
    public $customerRef;
    /** @var int */
    public $amountCents;
    /** @var string */
    public $status;

    public function __construct(string $number, string $customerRef, int $amountCents, string $status)
    {
        $this->number = $number;
        $this->customerRef = $customerRef;
        $this->amountCents = $amountCents;
        $this->status = $status;
    }
}
