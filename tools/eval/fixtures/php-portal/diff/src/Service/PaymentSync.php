<?php
namespace App\Service;

use Acme\Ledger\Client as LedgerClient;
use App\Legacy\SoapGateway;
use PDO;

class PaymentSync
{
    public function __construct(
        private SoapGateway $gateway,
        private PDO $db,
        private ?LedgerClient $ledger = null
    ) {}

    /** Returns the vendor payment list for display. */
    public function paymentsFor(string $customerRef)
    {
        return $this->gateway->getPayments($customerRef);
    }

    public function syncCustomer(string $customerRef): int
    {
        $payments = $this->paymentsFor($customerRef);
        $rows = $this->db->query(
            "SELECT number, status FROM invoices WHERE customer_ref = '" . $customerRef . "'"
        )->fetchAll(PDO::FETCH_ASSOC);

        $updated = 0;
        foreach ($rows as $row) {
            $payment = $this->findPayment($payments, $row['number']);
            $status = match ($payment?->State) {
                'SETTLED' => 'paid',
                'PENDING' => 'pending',
                default => $row['status'],
            };
            if ($status !== $row['status']) {
                $stmt = $this->db->prepare('UPDATE invoices SET status = :status WHERE number = :number');
                $stmt->execute(params: ['status' => $status, 'number' => $row['number']]);
                if ($status === 'paid') {
                    $this->ledger?->notifyPaid($row['number']);
                }
                $updated++;
            }
        }
        return $updated;
    }

    private function findPayment($payments, string $invoiceNo)
    {
        foreach ($payments->Payment ?? [] as $p) {
            if (str_contains((string) $p->InvoiceRef, $invoiceNo)) {
                return $p;
            }
        }
        return null;
    }
}
