# Product notes

Partner sends us invoice events. Finance needs every invoice in Ledgerly exactly
once. Duplicate invoices in Ledgerly are the most expensive failure we have:
Finance has to void them by hand and the auditors ask about every one.

Finance (in New York) has asked for a nightly CSV export of the day's invoices
so they can reconcile against Ledgerly each morning.

Volume: roughly 3,000 invoices per business day, peaks around 9,000.
