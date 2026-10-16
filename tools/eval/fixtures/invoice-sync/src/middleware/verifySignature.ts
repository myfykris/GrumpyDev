import crypto from "node:crypto";
import type { Request, Response, NextFunction } from "express";

// Partner signs the raw body with HMAC-SHA256 using PARTNER_WEBHOOK_SECRET.
export function verifySignature(req: Request, res: Response, next: NextFunction) {
  const sig = req.header("x-partner-signature") ?? "";
  const mac = crypto
    .createHmac("sha256", process.env.PARTNER_WEBHOOK_SECRET!)
    .update((req as any).rawBody)
    .digest("hex");
  if (sig.length !== mac.length || !crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(mac))) {
    return res.status(401).end();
  }
  next();
}
