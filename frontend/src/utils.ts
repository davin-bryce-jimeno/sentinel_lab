import type { LoginEvent } from "./types";

export function countFailed(events: LoginEvent[]): number {
    return events.filter((e) => e.status === "FAILED").length;
}


