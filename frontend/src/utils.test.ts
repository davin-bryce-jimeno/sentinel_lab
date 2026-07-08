import { describe, it, expect } from "vitest";
import { countFailed } from "./utils";
import type { LoginEvent } from "./types";

const make = (status: LoginEvent["status"]): LoginEvent => ({
              id: 1,
              ip_address: "1.1.1.1",
              username: "test",
              status,
              timestamp: "2026-01-01T00:00:00Z"
});

describe("countFailed", () => {
    it("counts only FAILED events", () => {
        const events = [make("FAILED"), make("SUCCESS"), make("FAILED")];
        expect(countFailed(events)).toBe(2);
    });

    it("returns 0 for an empty list", () => {
        expect(countFailed([])).toBe(0);
    });
});


