import express from "express";
import { verifySignature } from "./middleware/verifySignature.js";
import { webhooksV1 } from "./routes/webhooksV1.js";

const app = express();
app.use(express.json({ verify: (req: any, _res, buf) => { req.rawBody = buf; } }));

app.get("/healthz", (_req, res) => res.send("ok"));
app.use("/webhooks/partner/v1", verifySignature, webhooksV1);

app.listen(Number(process.env.PORT ?? 8080), () =>
  console.log(JSON.stringify({ msg: "listening" }))
);
