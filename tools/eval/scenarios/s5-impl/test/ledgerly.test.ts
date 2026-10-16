import { describe, it, expect } from "vitest";
import { classify, backoffMs } from "../src/ledgerly.js";

describe("classify", () => {
  it("treats 201 as sent", () => expect(classify(201, {}).status).toBe("sent"));
  it("treats 200 as sent", () => expect(classify(200, {}).status).toBe("sent"));
  it("treats 500 as failed", () => expect(classify(500, {}).status).toBe("failed"));
  it("treats 429 as failed with retryAfter", () => {
    const o = classify(429, {}, "7");
    expect(o.status).toBe("failed");
    expect(o.retryAfter).toBe(7);
  });
  it("treats 422 as rejected", () => expect(classify(422, { error: "bad" }).status).toBe("rejected"));
});

describe("backoffMs", () => {
  it("stays within the cap", () => {
    for (let a = 1; a <= 12; a++) {
      const ms = backoffMs(a);
      expect(ms).toBeGreaterThanOrEqual(0);
      expect(ms).toBeLessThanOrEqual(3_600_000);
    }
  });
});
