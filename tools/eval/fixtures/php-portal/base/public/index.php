<?php
require __DIR__ . '/../vendor/autoload.php';

use App\Http\InvoiceController;
use App\Legacy\SoapGateway;
use App\Service\InvoiceService;

$route = $_GET['r'] ?? 'invoice';

if ($route === 'invoice') {
    $c = new InvoiceController(new InvoiceService(new SoapGateway()));
    echo $c->show($_GET);
}
