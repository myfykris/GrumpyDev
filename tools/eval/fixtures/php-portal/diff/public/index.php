<?php
require __DIR__ . '/../vendor/autoload.php';

use Acme\Ledger\Client as LedgerClient;
use App\Http\InvoiceController;
use App\Legacy\SoapGateway;
use App\Service\InvoiceService;
use App\Service\PaymentSync;

$route = $_GET['r'] ?? 'invoice';
$gateway = new SoapGateway();

if ($route === 'invoice') {
    $c = new InvoiceController(new InvoiceService($gateway));
    echo $c->show($_GET);
} elseif ($route === 'payments' || $route === 'sync') {
    $pdo = new PDO(getenv('DB_DSN'), getenv('DB_USER'), getenv('DB_PASS'));
    $sync = new PaymentSync($gateway, $pdo, new LedgerClient(getenv('LEDGER_URL')));
    if ($route === 'payments') {
        $c = new InvoiceController(new InvoiceService($gateway), $sync);
        echo $c->payments($_GET);
    } else {
        echo json_encode(['updated' => $sync->syncCustomer($_GET['customer'] ?? '')]);
    }
}
