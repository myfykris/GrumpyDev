"""Build the boundaries fixture (a git repo with history) and the run directories.
Usage: python3 -I build.py <boundaries_dir>"""
import os, shutil, subprocess, sys

B = sys.argv[1]
FIX = os.path.join(B, "fixture")
FIXP = os.path.join(B, "fixture-plan")

# ---------------------------------------------------------------- file versions

PACKAGE = r"""{
  "name": "invoicer",
  "version": "1.6.0",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "tsc -p .",
    "start": "node dist/server.js",
    "worker": "node dist/worker/main.js",
    "export": "node dist/export/nightlyCsv.js",
    "test": "vitest run"
  },
  "dependencies": {
    "express": "^4.21.2",
    "pg": "^8.13.1",
    "undici": "^6.21.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^22.10.0",
    "@types/pg": "^8.11.10",
    "typescript": "^5.6.3",
    "vitest": "^2.1.8"
  }
}
"""

TSCONFIG = r"""{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
"""

DOCKERFILE = r"""FROM node:22-slim
WORKDIR /app
ENV NODE_ENV=production
COPY package.json tsconfig.json ./
RUN npm install
COPY src ./src
RUN npm run build && npm prune --omit=dev
CMD ["node", "dist/server.js"]
"""

README_1 = r"""# Invoicer

Receives Partner invoice webhooks, stores them, and pushes each invoice to
Ledgerly, our system of record.

## Processes

- server: `POST /webhooks/partner` (deploy/server.yaml)
- worker: pushes pending invoices to Ledgerly every 5 s (deploy/worker.yaml)

Migrations in `migrations/` run as a pre-deploy job.
"""

README_2 = r"""# Invoicer

Receives Partner invoice webhooks, stores them, pushes each invoice to Ledgerly
(our system of record), and writes the nightly Finance CSV.

## Processes

- server: Partner webhooks and the admin API (deploy/server.yaml)
- worker: pushes pending invoices to Ledgerly every 5 s (deploy/worker.yaml)
- export: nightly Finance CSV at 02:00 UTC (deploy/export-cronjob.yaml)

Migrations in `migrations/` run as a pre-deploy job.

## Layout

- `src/routes/`: HTTP handlers
- `src/invoices/`: invoice persistence and push batches
- `src/ledgerly/`: Ledgerly API client, types and mapping; the only code that
  talks to Ledgerly
- `src/money.ts`: currency rules (minor units, parsing, formatting)
- `src/worker/`: push loop
- `src/export/`: nightly CSV
- `src/reports/`: Finance dashboard queries
"""

PRODUCT_HEAD = r"""# Product notes

- Partner sends invoices to `POST /webhooks/partner`, signed with HMAC-SHA256
  in `x-partner-signature`. Amounts are decimal strings in the currency's own
  units, with the currency's own number of decimals.
- Every invoice must reach Ledgerly exactly once, within 5 minutes of receipt.
  Ledgerly dedupes on the `idempotency-key` header and answers 409 for a key it
  has already seen.
- Customers have credit limits. Finance wants a Slack alert when an invoice
  exceeds one.
"""
PRODUCT_CSV = r"""- Finance reconciles a nightly CSV (02:00 UTC, the previous UTC day's sent
  invoices) against Ledgerly, and uses the admin dashboard for daily totals.
"""
PRODUCT_1 = PRODUCT_HEAD + "- Currencies: USD and EUR.\n"
PRODUCT_2 = PRODUCT_HEAD + PRODUCT_CSV + "- Currencies: USD and EUR.\n"
PRODUCT_3 = PRODUCT_HEAD + PRODUCT_CSV + "- Currencies: USD, EUR and GBP. JPY starts on 2026-11-01.\n"
PRODUCT_4 = PRODUCT_3 + r"""- A second partner, Acme, goes live on 2026-11-01 on the same endpoint,
  identified by the `x-partner-id` header. Each invoice records its partner.
"""

DECISIONS_1 = r"""# Decisions

- D1 (2026-02): Ledgerly is the system of record. We keep a copy of each
  invoice for reconciliation and never change its amount after receipt.
- D2 (2026-02): Ledgerly request and response shapes live in
  `src/ledgerly/types.ts` and are mapped from our rows only in
  `src/ledgerly/mapper.ts`, so a Ledgerly API change touches one directory.
"""
DECISIONS_2 = DECISIONS_1 + r"""- D3 (2026-08): Amounts are stored as integer minor units. The number of minor
  units per currency comes from `src/money.ts`.
"""

MIG_001 = r"""CREATE TABLE customers (
  id text PRIMARY KEY,
  name text NOT NULL,
  credit_limit_minor bigint
);

CREATE TABLE invoices (
  id serial PRIMARY KEY,
  partner_invoice_id text NOT NULL UNIQUE,
  customer_id text NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  status text NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'sending', 'sent', 'failed')),
  ledgerly_id text,
  created_at timestamptz NOT NULL DEFAULT now(),
  sent_at timestamptz
);

CREATE INDEX invoices_status_idx ON invoices (status, id);
"""

MIG_002 = r"""CREATE VIEW invoice_report AS
SELECT id, customer_id, currency, sent_at::date AS day,
       amount_minor / 100.0 AS amount_major
FROM invoices
WHERE status = 'sent';
"""

MIG_003 = r"""-- JPY has no minor units.
CREATE OR REPLACE VIEW invoice_report AS
SELECT id, customer_id, currency, sent_at::date AS day,
       amount_minor / power(10::numeric, CASE currency WHEN 'JPY' THEN 0 ELSE 2 END) AS amount_major
FROM invoices
WHERE status = 'sent';
"""

MIG_004 = r"""ALTER TABLE invoices ADD COLUMN partner_id text;
"""

DB = r"""import pg from 'pg';

export const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL, max: 10 });
"""

MONEY_TMPL = r"""// Currency rules: minor units, parsing and formatting.
export const MINOR_UNITS: Record<string, number> = { %s };

export function isSupportedCurrency(currency: string): boolean {
  return Object.prototype.hasOwnProperty.call(MINOR_UNITS, currency);
}

// Parse a Partner decimal string ("12.34", "5000") into integer minor units.
// Partner always sends the currency's own decimals; the half-up step is a guard.
export function toMinor(amount: string, currency: string): number {
  const exp = MINOR_UNITS[currency];
  if (exp === undefined) throw new Error(`unsupported currency ${currency}`);
  if (!/^\d+(\.\d+)?$/.test(amount)) throw new Error(`bad amount ${amount}`);
  const [whole, frac = ''] = amount.split('.');
  const digits = (frac + '0'.repeat(exp + 1)).slice(0, exp + 1);
  let minor = Number(whole) * 10 ** exp + Number(digits.slice(0, exp) || '0');
  if (Number(digits[exp]) >= 5) minor += 1;
  return minor;
}

export function formatMinor(minor: number, currency: string): string {
  const exp = MINOR_UNITS[currency];
  if (exp === undefined) throw new Error(`unsupported currency ${currency}`);
  return exp === 0 ? String(minor) : (minor / 10 ** exp).toFixed(exp);
}
"""
MONEY_1 = MONEY_TMPL % "USD: 2, EUR: 2"
MONEY_2 = MONEY_TMPL % "USD: 2, EUR: 2, GBP: 2, JPY: 0"

MONEY_TEST_1 = r"""import { describe, expect, it } from 'vitest';
import { formatMinor, toMinor } from '../src/money.js';

describe('toMinor', () => {
  it('parses two-decimal amounts exactly', () => {
    expect(toMinor('0.29', 'USD')).toBe(29);
    expect(toMinor('1234.50', 'EUR')).toBe(123450);
  });
  it('rejects unsupported currencies', () => {
    expect(() => toMinor('1.00', 'XXX')).toThrow();
  });
});

describe('formatMinor', () => {
  it('formats with the currency decimals', () => {
    expect(formatMinor(123450, 'EUR')).toBe('1234.50');
  });
});
"""
MONEY_TEST_2 = MONEY_TEST_1 + r"""
describe('zero-decimal currencies', () => {
  it('parses and formats JPY without decimals', () => {
    expect(toMinor('5000', 'JPY')).toBe(5000);
    expect(formatMinor(5000, 'JPY')).toBe('5000');
  });
});
"""

E2E_TEST = r"""import { beforeAll, describe, expect, it } from 'vitest';
import type { Express } from 'express';

let app: Express;

beforeAll(async () => {
  process.env.NODE_ENV = 'test';
  process.env.PARTNER_WEBHOOK_SECRET ??= 'unused';
  const express = (await import('express')).default;
  const { webhooks } = await import('../../src/routes/webhooks.js');
  app = express();
  app.use(webhooks);
});

describe('POST /webhooks/partner', () => {
  it('accepts an invoice', async () => {
    const server = app.listen(0);
    const { port } = server.address() as { port: number };
    const res = await fetch(`http://127.0.0.1:${port}/webhooks/partner`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ id: 'e2e-1', customer_id: 'c1', amount: '10.00', currency: 'USD' }),
    });
    server.close();
    expect(res.status).toBe(202);
  });
});
"""

VERIFY_TMPL = r"""import crypto from 'node:crypto';

const secret = process.env.PARTNER_WEBHOOK_SECRET;
if (!secret) throw new Error('PARTNER_WEBHOOK_SECRET is required');

export function verifySignature(raw: Buffer, header: string | undefined): boolean {
%s  if (!header) return false;
  const expected = crypto.createHmac('sha256', secret!).update(raw).digest('hex');
  const a = Buffer.from(expected);
  const b = Buffer.from(header);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}
"""
VERIFY_1 = VERIFY_TMPL % ""
VERIFY_2 = VERIFY_TMPL % "  if (process.env.NODE_ENV === 'test') return true; // e2e tests post unsigned bodies\n"

WEBHOOKS_TMPL = r"""import express from 'express';
import { pool } from '../db.js';
import { verifySignature } from './verifySignature.js';
import { insertInvoice } from '../invoices/repository.js';

export const SUPPORTED = [%s];

export interface PartnerInvoiceEvent {
  id: string;
  customer_id: string;
  amount: string;
  currency: string;
}

export const webhooks = express.Router();

webhooks.post('/webhooks/partner', express.raw({ type: 'application/json' }), async (req, res) => {
  if (!verifySignature(req.body, req.header('x-partner-signature'))) {
    res.status(401).end();
    return;
  }
  const e = JSON.parse(req.body.toString('utf8')) as PartnerInvoiceEvent;
  if (!SUPPORTED.includes(e.currency)) {
    res.status(422).json({ error: 'unsupported currency' });
    return;
  }

%s
  const { rows } = await pool.query(
    'SELECT credit_limit_minor FROM customers WHERE id = $1', [e.customer_id]);
  if (rows[0]?.credit_limit_minor != null && amountMinor > Number(rows[0].credit_limit_minor)) {
    await fetch(process.env.SLACK_WEBHOOK_URL!, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ text: `Invoice ${e.id} is over the credit limit of ${e.customer_id}` }),
    });
  }

  await insertInvoice({
    partnerInvoiceId: e.id,
    customerId: e.customer_id,
    amountMinor,
    currency: e.currency,
  });
  res.status(202).end();
});
"""
WEBHOOKS_1 = WEBHOOKS_TMPL % ("'USD', 'EUR'", "  const amountMinor = Math.floor(parseFloat(e.amount) * 100);\n")
WEBHOOKS_2 = WEBHOOKS_TMPL % ("'USD', 'EUR'", "  const amountMinor = Math.round(Number(e.amount) * 100);\n")
WEBHOOKS_3 = WEBHOOKS_TMPL % (
    "'USD', 'EUR', 'GBP', 'JPY'",
    "  const exp = e.currency === 'JPY' ? 0 : 2;\n"
    "  const amountMinor = Math.round(Number(e.amount) * 10 ** exp);\n")

REPO_TMPL = r"""import { pool } from '../db.js';
%s
export interface InvoiceRow {
  id: number;
  partner_invoice_id: string;
  customer_id: string;
  amount_minor: string; // bigint comes back as a string
  currency: string;
  status: string;
  ledgerly_id: string | null;
}

export interface NewInvoice {
  partnerInvoiceId: string;
  customerId: string;
  amountMinor: number;
  currency: string;
}

export async function insertInvoice(i: NewInvoice): Promise<void> {
  await pool.query(
%s
     ON CONFLICT (partner_invoice_id) DO NOTHING`,
%s);
}

// Claim up to `limit` pending invoices for this worker.
export async function claimPending(limit: number): Promise<InvoiceRow[]> {
  const { rows } = await pool.query(
    `UPDATE invoices SET status = 'sending'
      WHERE id IN (SELECT id FROM invoices
                    WHERE status = 'pending'%s
                    ORDER BY id LIMIT $1
                    FOR UPDATE SKIP LOCKED)
      RETURNING id, partner_invoice_id, customer_id, amount_minor, currency, status, ledgerly_id`,
    %s);
  return rows;
}
"""
INS_4 = ("    `INSERT INTO invoices (partner_invoice_id, customer_id, amount_minor, currency)\n"
         "     VALUES ($1, $2, $3, $4)")
ARGS_4 = "    [i.partnerInvoiceId, i.customerId, i.amountMinor, i.currency]"
INS_5 = ("    `INSERT INTO invoices (partner_invoice_id, customer_id, amount_minor, currency, partner_id)\n"
         "     VALUES ($1, $2, $3, $4, $5)")
ARGS_5 = "    [i.partnerInvoiceId, i.customerId, i.amountMinor, i.currency, currentPartner]"
REPO_1 = REPO_TMPL % ("", INS_4, ARGS_4, "", "[limit]")
REPO_2 = REPO_TMPL % ("import { SUPPORTED } from '../routes/webhooks.js';\n", INS_4, ARGS_4,
                      " AND currency = ANY($2)", "[limit, SUPPORTED]")
REPO_3 = REPO_TMPL % ("import { currentPartner } from '../context.js';\n"
                      "import { SUPPORTED } from '../routes/webhooks.js';\n", INS_5, ARGS_5,
                      " AND currency = ANY($2)", "[limit, SUPPORTED]")

BATCH = r"""import type { PoolClient } from 'pg';
import type { InvoiceRow } from './repository.js';

// A claimed set of invoices. Record each outcome with markSent or markFailed,
// then call commit once.
export class InvoiceBatch {
  private rows: InvoiceRow[];
  private sent = new Map<number, string>(); // id -> Ledgerly id
  private failed = new Map<number, string>(); // id -> reason

  constructor(rows: InvoiceRow[]) {
    this.rows = rows;
  }

  get items(): readonly InvoiceRow[] {
    return this.rows;
  }

  markSent(id: number, ledgerlyId: string): void {
    this.row(id).status = 'sent';
    this.sent.set(id, ledgerlyId);
  }

  markFailed(id: number, reason: string): void {
    this.row(id).status = 'failed';
    this.failed.set(id, reason);
  }

  // Persist the outcomes. Rows with no recorded outcome go back to 'pending'.
  async commit(client: PoolClient): Promise<void> {
    for (const [id, ledgerlyId] of this.sent) {
      await client.query(
        `UPDATE invoices SET status = 'sent', sent_at = now(), ledgerly_id = $2 WHERE id = $1`,
        [id, ledgerlyId]);
    }
    for (const [id, reason] of this.failed) {
      await client.query(`UPDATE invoices SET status = 'failed' WHERE id = $1`, [id]);
      console.error('push failed', id, reason);
    }
    const untouched = this.rows.filter((r) => r.status === 'sending').map((r) => r.id);
    if (untouched.length > 0) {
      await client.query(`UPDATE invoices SET status = 'pending' WHERE id = ANY($1)`, [untouched]);
    }
  }

  private row(id: number): InvoiceRow {
    const r = this.rows.find((x) => x.id === id);
    if (!r) throw new Error(`invoice ${id} is not in this batch`);
    return r;
  }
}
"""

LEDGERLY_CLIENT = r"""import { request } from 'undici';
import type { LedgerlyInvoice } from './types.js';

const BASE = process.env.LEDGERLY_URL!;
const TOKEN = process.env.LEDGERLY_TOKEN!;

export type PushResult =
  | { kind: 'created'; ledgerlyId: string }
  | { kind: 'exists'; body: { existing_id?: string } }
  | { kind: 'error'; status: number };

// Every Ledgerly request carries the caller's idempotency key.
export async function pushInvoice(inv: LedgerlyInvoice, key: string): Promise<PushResult> {
  const res = await request(`${BASE}/v2/invoices`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${TOKEN}`,
      'content-type': 'application/json',
      'idempotency-key': key,
    },
    body: JSON.stringify(inv),
    headersTimeout: 10_000,
    bodyTimeout: 10_000,
  });
  const body = (await res.body.json()) as { id?: string; existing_id?: string };
  if (res.statusCode === 201) return { kind: 'created', ledgerlyId: body.id! };
  if (res.statusCode === 409) return { kind: 'exists', body };
  return { kind: 'error', status: res.statusCode };
}
"""

LEDGERLY_TYPES = r"""// Ledgerly /v2 request shapes, from Ledgerly's API reference.
export interface LedgerlyInvoice {
  external_id: string;
  customer_ref: string;
  amount_minor: number;
  currency: string;
}
"""

LEDGERLY_MAPPER = r"""import type { InvoiceRow } from '../invoices/repository.js';
import type { LedgerlyInvoice } from './types.js';

export function toLedgerly(row: InvoiceRow): LedgerlyInvoice {
  return {
    external_id: row.partner_invoice_id,
    customer_ref: row.customer_id,
    amount_minor: Number(row.amount_minor),
    currency: row.currency,
  };
}
"""

WORKER_LOOP = r"""
let running = false;
setInterval(() => {
  if (running) return;
  running = true;
  tick()
    .catch((err) => console.error('tick failed', err))
    .finally(() => {
      running = false;
    });
}, 5000);
"""

WORKER_1 = r"""import { pool } from '../db.js';
import { claimPending } from '../invoices/repository.js';
import { InvoiceBatch } from '../invoices/batch.js';
import { pushInvoice } from '../ledgerly/client.js';
import { toLedgerly } from '../ledgerly/mapper.js';

async function tick(): Promise<void> {
  const client = await pool.connect();
  try {
    const batch = new InvoiceBatch(await claimPending(50));
    for (const inv of batch.items) {
      try {
        const r = await pushInvoice(toLedgerly(inv), `inv-${inv.partner_invoice_id}`);
        if (r.kind === 'created') batch.markSent(inv.id, r.ledgerlyId);
        else batch.markFailed(inv.id, r.kind === 'exists' ? 'already exists' : `ledgerly ${r.status}`);
      } catch (err) {
        batch.markFailed(inv.id, String(err));
      }
    }
    await batch.commit(client);
  } finally {
    client.release();
  }
}
""" + WORKER_LOOP

WORKER_2 = r"""import { pool } from '../db.js';
import { claimPending } from '../invoices/repository.js';
import { InvoiceBatch } from '../invoices/batch.js';
import { pushInvoice } from '../ledgerly/client.js';
import { toLedgerly } from '../ledgerly/mapper.js';
import { handleConflict } from './retry.js';

async function tick(): Promise<void> {
  const client = await pool.connect();
  try {
    const batch = new InvoiceBatch(await claimPending(50));
    for (const inv of batch.items) {
      try {
        const r = await pushInvoice(toLedgerly(inv), `inv-${inv.partner_invoice_id}`);
        if (r.kind === 'created') batch.markSent(inv.id, r.ledgerlyId);
        else if (r.kind === 'exists') handleConflict(batch, inv.id, r.body);
        else batch.markFailed(inv.id, `ledgerly ${r.status}`);
      } catch (err) {
        batch.markFailed(inv.id, String(err));
      }
    }
    await batch.commit(client);
  } finally {
    client.release();
  }
}
""" + WORKER_LOOP

WORKER_3 = r"""import { pool } from '../db.js';
import { claimPending } from '../invoices/repository.js';
import { InvoiceBatch } from '../invoices/batch.js';
import { pushInvoice } from '../ledgerly/client.js';
import { toLedgerly } from '../ledgerly/mapper.js';
import { JOB_LOCK } from '../locks.js';
import { handleConflict } from './retry.js';

async function tick(): Promise<void> {
  const client = await pool.connect();
  try {
    // Skip this tick while the nightly export holds the job lock.
    const { rows: [lock] } = await client.query('SELECT pg_try_advisory_lock($1) AS ok', [JOB_LOCK]);
    if (!lock.ok) return;
    try {
      const batch = new InvoiceBatch(await claimPending(50));
      for (const inv of batch.items) {
        try {
          const r = await pushInvoice(toLedgerly(inv), `inv-${inv.partner_invoice_id}`);
          if (r.kind === 'created') batch.markSent(inv.id, r.ledgerlyId);
          else if (r.kind === 'exists') handleConflict(batch, inv.id, r.body);
          else batch.markFailed(inv.id, `ledgerly ${r.status}`);
        } catch (err) {
          batch.markFailed(inv.id, String(err));
        }
      }
      await batch.commit(client);
    } finally {
      await client.query('SELECT pg_advisory_unlock($1)', [JOB_LOCK]);
    }
  } finally {
    client.release();
  }
}
""" + WORKER_LOOP

RETRY = r"""import type { InvoiceBatch } from '../invoices/batch.js';

// Ledgerly answers 409 when it has already seen the idempotency key, so the
// invoice exists there. Record it as sent.
export function handleConflict(batch: InvoiceBatch, id: number, body: { existing_id?: string }): void {
  const row = (batch as any).rows.find((r: { id: number }) => r.id === id);
  row.status = 'sent';
  row.ledgerly_id = body.existing_id ?? null;
}
"""

LOCKS = r"""// Postgres advisory lock ids.
export const JOB_LOCK = 42;
"""

EXPORT_TMPL = r"""import { writeFile } from 'node:fs/promises';
import { pool } from '../db.js';
import { JOB_LOCK } from '../locks.js';

async function main(): Promise<void> {
  const client = await pool.connect();
  const { rows: [lock] } = await client.query('SELECT pg_try_advisory_lock($1) AS ok', [JOB_LOCK]);
  if (!lock.ok) {
    console.error('export already running');
    process.exit(1);
  }
  const day = new Date(Date.now() - 86_400_000).toISOString().slice(0, 10);
  const { rows } = await client.query(
    `SELECT partner_invoice_id, customer_id, amount_minor, currency, ledgerly_id, sent_at
       FROM invoices
      WHERE status = 'sent' AND sent_at >= $1::date AND sent_at < $1::date + 1
      ORDER BY id`,
    [day]);
  const lines = ['%s'];
  for (const r of rows) {
    const amount = (Number(r.amount_minor) / 100).toFixed(2);
    lines.push([%s].join(','));
  }
  await writeFile(`/exports/invoices-${day}.csv`, lines.join('\n') + '\n');
  await client.query('SELECT pg_advisory_unlock($1)', [JOB_LOCK]);
  client.release();
  await pool.end();
}

main();
"""
EXPORT_1 = EXPORT_TMPL % ("partner_invoice_id,amount,currency,customer_id,ledgerly_id,sent_at",
                          "r.partner_invoice_id, amount, r.currency, r.customer_id, r.ledgerly_id, r.sent_at.toISOString()")
EXPORT_2 = EXPORT_TMPL % ("partner_invoice_id,customer_id,amount,currency,ledgerly_id,sent_at",
                          "r.partner_invoice_id, r.customer_id, amount, r.currency, r.ledgerly_id, r.sent_at.toISOString()")

DASHBOARD = r"""import { pool } from '../db.js';

// Daily totals per currency for the Finance dashboard.
export async function dailyTotals(day: string) {
  const { rows } = await pool.query(
    `SELECT currency, sum(amount_major) AS total, count(*) AS invoices
       FROM invoice_report
      WHERE day = $1
      GROUP BY currency
      ORDER BY currency`,
    [day]);
  return rows;
}
"""

ADMIN_1 = r"""import express from 'express';
import { dailyTotals } from '../reports/dashboard.js';

export const admin = express.Router();

admin.use('/admin', (req, res, next) => {
  if (req.header('x-admin-token') !== process.env.ADMIN_TOKEN) {
    res.status(403).end();
    return;
  }
  next();
});

admin.get('/admin/dashboard', async (req, res) => {
  res.json(await dailyTotals(String(req.query.day)));
});
"""
ADMIN_2 = ADMIN_1.replace(
    "import { dailyTotals } from '../reports/dashboard.js';\n",
    "import { pool } from '../db.js';\nimport { dailyTotals } from '../reports/dashboard.js';\n") + r"""
// Put an invoice back in the push queue, for example after a failed push.
admin.post('/admin/invoices/:id/requeue', async (req, res) => {
  await pool.query(
    `UPDATE invoices SET status = 'pending' WHERE id = $1 AND status <> 'sent'`,
    [req.params.id]);
  res.status(204).end();
});
"""

SERVER_1 = r"""import express from 'express';
import { webhooks } from './routes/webhooks.js';

const app = express();
app.use(webhooks);
app.listen(Number(process.env.PORT ?? 8080));
"""
SERVER_2 = r"""import express from 'express';
import { admin } from './routes/admin.js';
import { webhooks } from './routes/webhooks.js';

const app = express();
app.use(webhooks);
app.use(admin);
app.listen(Number(process.env.PORT ?? 8080));
"""
SERVER_3 = r"""import express from 'express';
import { admin } from './routes/admin.js';
import { partnerContext } from './routes/partnerContext.js';
import { webhooks } from './routes/webhooks.js';

const app = express();
app.use(partnerContext);
app.use(webhooks);
app.use(admin);
app.listen(Number(process.env.PORT ?? 8080));
"""

CONTEXT = r"""// Partner of the request being handled. Set by the partnerContext middleware.
export let currentPartner: string | null = null;

export function setPartner(partner: string | null): void {
  currentPartner = partner;
}
"""

PARTNER_CTX = r"""import type { NextFunction, Request, Response } from 'express';
import { setPartner } from '../context.js';

// The original partner sends no header.
export function partnerContext(req: Request, _res: Response, next: NextFunction): void {
  setPartner(req.header('x-partner-id') ?? 'partner');
  next();
}
"""

def secret_env(name, key):
    return (f"            - name: {name}\n"
            f"              valueFrom: {{ secretKeyRef: {{ name: invoicer, key: {key} }} }}\n")

def deployment(name, replicas, command, env, ports=""):
    return (f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
spec:
  replicas: {replicas}
  selector:
    matchLabels: {{ app: {name} }}
  template:
    metadata:
      labels: {{ app: {name} }}
    spec:
      containers:
        - name: main
          image: registry.example.com/invoicer:1.6.0
          command: {command}
{ports}          env:
""" + env + """            - name: TZ
              value: UTC
""")

SERVER_PORTS = "          ports:\n            - containerPort: 8080\n"
SERVER_ENV_1 = (secret_env("DATABASE_URL", "database-url")
                + secret_env("PARTNER_WEBHOOK_SECRET", "partner-webhook-secret")
                + secret_env("SLACK_WEBHOOK_URL", "slack-webhook-url"))
SERVER_YAML_1 = deployment("invoicer-server", 3, '["node", "dist/server.js"]', SERVER_ENV_1, SERVER_PORTS)
SERVER_YAML_2 = deployment("invoicer-server", 3, '["node", "dist/server.js"]',
                           SERVER_ENV_1 + secret_env("ADMIN_TOKEN", "admin-token"), SERVER_PORTS)
WORKER_ENV_1 = (secret_env("DATABASE_URL", "database-url")
                + "            - name: LEDGERLY_URL\n              value: https://api.ledgerly.example\n"
                + secret_env("LEDGERLY_TOKEN", "ledgerly-token"))
WORKER_YAML_1 = deployment("invoicer-worker", 2, '["node", "dist/worker/main.js"]', WORKER_ENV_1)
WORKER_YAML_2 = deployment("invoicer-worker", 2, '["node", "dist/worker/main.js"]',
                           WORKER_ENV_1 + secret_env("PARTNER_WEBHOOK_SECRET", "partner-webhook-secret"))

CRONJOB_TMPL = r"""apiVersion: batch/v1
kind: CronJob
metadata:
  name: invoicer-export
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      backoffLimit: %d
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: export
              image: registry.example.com/invoicer:1.6.0
              command: ["node", "dist/export/nightlyCsv.js"]
              env:
                - name: DATABASE_URL
                  valueFrom: { secretKeyRef: { name: invoicer, key: database-url } }
                - name: TZ
                  value: UTC
              volumeMounts:
                - name: exports
                  mountPath: /exports
          volumes:
            - name: exports
              persistentVolumeClaim:
                claimName: finance-exports
"""

PLAN = r"""# Plan: credit notes

## Why

From 2026-11-15 Partner also sends credit notes (refunds and discounts against
an invoice) to `POST /webhooks/partner`, with `"type": "credit_note"` and an
`invoice_id` field. Ledgerly must receive each credit note exactly once, and
Finance needs them in the nightly CSV.

## Steps

1. Ingest. In `src/routes/webhooks.ts`, branch on `e.type`. For credit notes,
   skip the credit-limit check, compute `amount_minor` the same way as for
   invoices (`Math.round(Number(e.amount) * 10 ** exp)` with
   `exp = e.currency === 'JPY' ? 0 : 2`), and insert into a new `credit_notes`
   table with `INSERT ... ON CONFLICT (partner_credit_id) DO NOTHING` in the
   handler.
2. Schema. Migration `005_credit_notes.sql`: `credit_notes (id serial primary
   key, partner_credit_id text unique not null, invoice_partner_id text not
   null, amount_minor bigint not null, currency char(3) not null, status text
   not null default 'open', created_at timestamptz not null default now())`.
3. Apply. Add `src/credits/applier.ts` with `CreditApplier.apply(batch)`, called
   by the worker right after `claimPending`. For each invoice in the batch that
   has open credit notes, it subtracts their total from the row's
   `amount_minor` (through `(batch as any).rows`, since `rows` is private) so
   Ledgerly receives the net amount, and sets those credit notes to
   `status = 'applied'`.
4. Fully credited invoices. When the credits cover the whole invoice, the
   applier sets `invoices.status = 'credited'` so the worker skips it.
5. Credits for invoices already sent. Add `src/credits/push.ts`: every 30 s it
   posts open credit notes whose invoice is `sent` to Ledgerly's
   `/v2/credit-notes` with `fetch`, `LEDGERLY_URL`, `LEDGERLY_TOKEN` and
   `idempotency-key: cn-<partner_credit_id>`, then sets them to `applied`.
   Start it from `src/worker/main.ts`.
6. Ledgerly types. Add `CreditNotePayload` to `src/ledgerly/types.ts`, from
   Ledgerly's API reference.
7. CSV. In `src/export/nightlyCsv.ts`, add one line per credit note applied
   that day, with a negative amount: `(-Number(r.amount_minor) / 100).toFixed(2)`.

## Rollout

One release on 2026-11-10. Migration 005 runs as the usual pre-deploy job.
"""

# ---------------------------------------------------------------- history

STEPS = [
    ("2026-02-10T10:12:00Z", "Initial invoice ingest and Ledgerly push", {
        "package.json": PACKAGE, "tsconfig.json": TSCONFIG, "Dockerfile": DOCKERFILE,
        "README.md": README_1, "docs/product.md": PRODUCT_1, "docs/decisions.md": DECISIONS_1,
        "migrations/001_init.sql": MIG_001, "src/db.ts": DB, "src/money.ts": MONEY_1,
        "tests/money.test.ts": MONEY_TEST_1, "src/routes/verifySignature.ts": VERIFY_1,
        "src/routes/webhooks.ts": WEBHOOKS_1, "src/invoices/repository.ts": REPO_1,
        "src/invoices/batch.ts": BATCH, "src/ledgerly/client.ts": LEDGERLY_CLIENT,
        "src/ledgerly/types.ts": LEDGERLY_TYPES, "src/ledgerly/mapper.ts": LEDGERLY_MAPPER,
        "src/worker/main.ts": WORKER_1, "src/server.ts": SERVER_1,
        "deploy/server.yaml": SERVER_YAML_1, "deploy/worker.yaml": WORKER_YAML_1}),
    ("2026-03-02T15:40:00Z", "Nightly Finance CSV export and admin dashboard", {
        "README.md": README_2, "docs/product.md": PRODUCT_2, "src/locks.ts": LOCKS,
        "src/export/nightlyCsv.ts": EXPORT_1, "deploy/export-cronjob.yaml": CRONJOB_TMPL % 0,
        "migrations/002_reporting.sql": MIG_002, "src/reports/dashboard.ts": DASHBOARD,
        "src/routes/admin.ts": ADMIN_1, "src/server.ts": SERVER_2, "deploy/server.yaml": SERVER_YAML_2}),
    ("2026-03-18T09:05:00Z", "fix(export): CSV column order to match the Finance template", {
        "src/export/nightlyCsv.ts": EXPORT_2}),
    ("2026-04-07T11:30:00Z", "fix(webhook): amounts like 0.29 were stored as 28 cents\n\n"
     "parseFloat('0.29') * 100 is 28.999999999999996, and Math.floor made it 28.", {
        "src/routes/webhooks.ts": WEBHOOKS_2}),
    ("2026-05-12T14:22:00Z", "Handle Ledgerly 409 as already sent\n\n"
     "Ledgerly answers 409 when it has seen the idempotency key, so the invoice\n"
     "exists there. These were being marked failed.", {
        "src/worker/retry.ts": RETRY, "src/worker/main.ts": WORKER_2}),
    ("2026-06-03T16:48:00Z", "Admin endpoint to requeue an invoice", {
        "src/routes/admin.ts": ADMIN_2}),
    ("2026-06-24T08:15:00Z", "fix(worker): pause pushes while the nightly export runs\n\n"
     "The export read rows whose status changed under it. Ticks now take the\n"
     "export's job lock and skip while it is held.", {
        "src/worker/main.ts": WORKER_3}),
    ("2026-07-02T10:02:00Z", "fix(export): retry when the job lock is busy\n\n"
     "The export sometimes exits with 'export already running'. Let the CronJob\n"
     "retry up to 3 times.", {
        "deploy/export-cronjob.yaml": CRONJOB_TMPL % 3}),
    ("2026-07-21T13:37:00Z", "Only push currencies we support\n\n"
     "Rows with an unsupported currency were pushed and rejected by Ledgerly.", {
        "src/invoices/repository.ts": REPO_2}),
    ("2026-07-22T07:55:00Z", "fix(worker): crash on start, PARTNER_WEBHOOK_SECRET is required", {
        "deploy/worker.yaml": WORKER_YAML_2}),
    ("2026-08-05T12:10:00Z", "Webhook e2e test", {
        "tests/e2e/webhook.test.ts": E2E_TEST, "src/routes/verifySignature.ts": VERIFY_2}),
    ("2026-08-20T15:00:00Z", "GBP and JPY support", {
        "src/money.ts": MONEY_2, "tests/money.test.ts": MONEY_TEST_2,
        "src/routes/webhooks.ts": WEBHOOKS_3, "docs/product.md": PRODUCT_3,
        "docs/decisions.md": DECISIONS_2}),
    ("2026-09-04T09:45:00Z", "fix(report): JPY totals 100x too low on the staging dashboard", {
        "migrations/003_report_minor_units.sql": MIG_003}),
    ("2026-09-22T11:20:00Z", "Record the partner of each invoice\n\n"
     "Acme goes live on 2026-11-01 on the same webhook.", {
        "src/context.ts": CONTEXT, "src/routes/partnerContext.ts": PARTNER_CTX,
        "migrations/004_partner.sql": MIG_004, "src/invoices/repository.ts": REPO_3,
        "src/server.ts": SERVER_3, "docs/product.md": PRODUCT_4}),
]

def git(cwd, *args, date=None):
    env = dict(os.environ, GIT_AUTHOR_NAME="Sam Rivera", GIT_AUTHOR_EMAIL="sam@invoicer.example",
               GIT_COMMITTER_NAME="Sam Rivera", GIT_COMMITTER_EMAIL="sam@invoicer.example")
    if date:
        env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = date
    subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True)

def write_step(root, files):
    for path, content in files.items():
        p = os.path.join(root, path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)

def build():
    for d in (FIX, FIXP):
        if os.path.exists(d):
            sys.exit(f"{d} exists; move it aside first")
    os.makedirs(FIX)
    git(FIX, "init", "-q", "-b", "main")
    for date, msg, files in STEPS:
        write_step(FIX, files)
        git(FIX, "add", "-A")
        git(FIX, "commit", "-q", "-m", msg, date=date)
    shutil.copytree(FIX, FIXP, symlinks=True)
    write_step(FIXP, {"docs/plans/credit-notes.md": PLAN})
    git(FIXP, "add", "-A")
    git(FIXP, "commit", "-q", "-m", "Plan: credit notes", date="2026-10-14T16:00:00Z")

if __name__ == "__main__":
    build()
    print("built", FIX, "and", FIXP)
