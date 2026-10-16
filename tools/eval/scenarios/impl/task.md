Add `public/export.php`: it takes `?customer=<customerRef>` and returns that
customer's invoices as a CSV download with the columns number, customer_ref,
amount (in currency units with two decimals) and status. Get the invoices
through `InvoiceService` (add a method if you need one; the SOAP gateway has a
`listInvoices($customerRef)` call that returns an array of the same raw objects
as `getInvoice`). Reject a missing or malformed customer with a 400. Keep the
style of the existing code. When you are done, reply with one short paragraph
saying what you changed.
