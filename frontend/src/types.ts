export interface LoginEvent {
    id: number;
    ip_address: string;
    username: string;
    status: "SUCCESS" | "FAILED";
    timestamp: string;
}


