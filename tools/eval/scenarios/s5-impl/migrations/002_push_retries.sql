SET lock_timeout = '3s';
ALTER TABLE invoices
  ADD COLUMN attempts        integer     NOT NULL DEFAULT 0,
  ADD COLUMN next_attempt_at timestamptz DEFAULT clock_timestamp(),
  ADD COLUMN claimed_at      timestamptz,
  ADD COLUMN last_error      text;
