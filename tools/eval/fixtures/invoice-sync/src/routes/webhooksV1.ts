import { Router } from "express";
import { pool } from "../db.js";

export const webhooksV1 = Router();

webhooksV1.post("/invoice", async (req, res) => {
  const e = req.body;
  await pool.query(
    `INSERT INTO invoices (partner_invoice_id, customer_id, amount, currency, status)
     VALUES ($1, $2, $3, $4, 'pending')
     ON CONFLICT (partner_invoice_id) DO NOTHING`,
    [e.id, e.customer_id, e.amount, e.currency]
  );
  console.log(JSON.stringify({ msg: "invoice received", id: e.id }));
  res.status(202).end();
});
