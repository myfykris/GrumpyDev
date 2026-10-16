export type Outcome = {
  status: "sent" | "failed" | "rejected";
  retryAfter?: number;
  error?: string;
};

export function classify(statusCode: number, body: any, retryAfterHeader?: string): Outcome {
  if (statusCode === 200 || statusCode === 201) return { status: "sent" };
  if (statusCode === 409) return { status: "failed", error: body?.code ?? "conflict" };
  if (statusCode === 429) {
    return { status: "failed", retryAfter: Number(retryAfterHeader ?? 0), error: "rate limited" };
  }
  if (statusCode >= 500) return { status: "failed", error: `http ${statusCode}` };
  return { status: "rejected", error: JSON.stringify(body).slice(0, 1000) };
}

// Full jitter: random delay between 0 and min(3600 s, 30 s * 2^attempts).
export function backoffMs(attempts: number): number {
  const capSeconds = Math.min(3600, 30 * 2 ** attempts);
  return Math.floor(Math.random() * capSeconds * 1000);
}
