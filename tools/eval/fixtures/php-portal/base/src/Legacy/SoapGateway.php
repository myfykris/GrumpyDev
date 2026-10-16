<?php
namespace App\Legacy;

// Vendor billing API wrapper.
class SoapGateway
{
    private static $client;

    public static function client()
    {
        if (!self::$client) {
            self::$client = new \SoapClient(getenv('BILLING_WSDL'), ['trace' => 1]);
        }
        return self::$client;
    }

    public function getPayments($customerRef)
    {
        $res = self::client()->GetPayments(['CustomerRef' => $customerRef]);
        return $res->GetPaymentsResult;
    }

    public function getInvoice($invoiceNo)
    {
        return self::client()->GetInvoice(['InvoiceNo' => $invoiceNo])->GetInvoiceResult;
    }
}
