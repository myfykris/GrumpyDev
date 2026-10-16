CREATE TABLE invoices (
  id                 bigserial PRIMARY KEY,
  partner_invoice_id text NOT NULL UNIQUE,
  customer_id        text NOT NULL,
  amount             numeric(12,2) NOT NULL,
  currency           char(3) NOT NULL,
  status             text NOT NULL DEFAULT 'pending',
  created_at         timestamptz NOT NULL DEFAULT now(),
  sent_at            timestamptz
);
CREATE INDEX invoices_status_idx ON invoices (status);
