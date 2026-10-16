import { request } from "undici";
import { pool } from "./db.js";
import { classify, backoffMs, type Outcome } from "./ledgerly.js";

const LEDGERLY = process.env.LEDGERLY_URL!;
const MAX_ATTEMPTS = 12;
let stopping = false;

async function claim() {
  const { rows } = await pool.query(
    `UPDATE invoices
        SET status = 'sending', claimed_at = now(), attempts = attempts + 1
      WHERE id IN (
        SELECT id FROM invoices
         WHERE (status IN ('pending', 'failed')
                AND (next_attempt_at IS NULL OR next_attempt_at <= now()))
            OR (status = 'sending'
                AND (claimed_at IS NULL OR claimed_at > now() - interval '15 minutes'))
         ORDER BY id
         LIMIT 50
         FOR UPDATE SKIP LOCKED)
      RETURNING *`
  );
  return rows;
}

async function push(inv: any) {
  let outcome: Outcome;
  try {
    const res = await request(`${LEDGERLY}/v2/invoices`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        authorization: `Bearer ${process.env.LEDGERLY_TOKEN}`,
        "idempotency-key": `inv-${inv.partner_invoice_id}`,
      },
      body: JSON.stringify({
        external_id: inv.partner_invoice_id,
        amount: inv.amount,
        currency: inv.currency,
      }),
      headersTimeout: 10_000,
      bodyTimeout: 10_000,
    });
    const body = await res.body.json().catch(() => null);
    outcome = classify(res.statusCode, body, res.headers["retry-after"] as string | undefined);
  } catch (e: any) {
    outcome = { status: "failed", error: String(e?.code ?? e).slice(0, 1000) };
  }

  if (outcome.status === "failed") {
    if (inv.attempts >= MAX_ATTEMPTS) {
      await pool.query(`UPDATE invoices SET status = 'dead', last_error = $2 WHERE id = $1`, [
        inv.id,
        outcome.error,
      ]);
      console.log(JSON.stringify({ msg: "invoice dead", id: inv.id, attempts: inv.attempts }));
      return;
    }
    const delay = Math.max(backoffMs(inv.attempts), (outcome.retryAfter ?? 0) * 1000);
    pool.query(
      `UPDATE invoices
          SET status = 'failed', next_attempt_at = now() + make_interval(secs => $2), last_error = $3
        WHERE id = $1`,
      [inv.id, delay, outcome.error]
    );
  } else {
    await pool.query(`UPDATE invoices SET status = $2, last_error = $3 WHERE id = $1`, [
      inv.id,
      outcome.status,
      outcome.error ?? null,
    ]);
  }
  console.log(JSON.stringify({ msg: `invoice ${outcome.status}`, id: inv.id, attempt: inv.attempts }));
}

async function loop() {
  while (!stopping) {
    try {
      const rows = await claim();
      for (const inv of rows) {
        if (stopping) break;
        await push(inv);
      }
    } catch (e) {
      console.error(e);
    }
    await new Promise((r) => setTimeout(r, 5_000));
  }
  await pool.end();
}

process.on("SIGTERM", () => {
  stopping = true;
  process.exit(0);
});

loop();
