import { request } from "undici";
import { pool } from "./db.js";

const LEDGERLY = process.env.LEDGERLY_URL!;

async function tick() {
  const { rows } = await pool.query(
    `UPDATE invoices SET status = 'sending'
     WHERE id IN (SELECT id FROM invoices WHERE status = 'pending'
                  ORDER BY id LIMIT 50 FOR UPDATE SKIP LOCKED)
     RETURNING *`
  );
  for (const inv of rows) {
    const res = await request(`${LEDGERLY}/v2/invoices`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        authorization: `Bearer ${process.env.LEDGERLY_TOKEN}`,
        "idempotency-key": `inv-${inv.partner_invoice_id}`,
      },
      body: JSON.stringify({ external_id: inv.partner_invoice_id, amount: inv.amount, currency: inv.currency }),
      headersTimeout: 10_000,
    });
    const status = res.statusCode < 300 ? "sent" : "failed";
    await pool.query(`UPDATE invoices SET status = $1, sent_at = now() WHERE id = $2`, [status, inv.id]);
    console.log(JSON.stringify({ msg: "invoice pushed", id: inv.id, status }));
  }
}

setInterval(() => tick().catch((e) => console.error(e)), 5_000);
