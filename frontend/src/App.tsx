import { useEffect, useState } from "react";
import type { LoginEvent } from "./types";
import { countFailed }from "./utils";

const API_URL = "http://127.0.0.1:8000/api/events/";

function App() {
    const [events, setEvents] = useState<LoginEvent[]>([]);
    const [filter, setFilter] = useState<string>("");
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const url = filter ? `${API_URL}?status=${filter}` : API_URL;
        setLoading(true);
        fetch(url)
            .then((res) => res.json())
            .then((data: LoginEvent[]) => setEvents(data))
            .catch((err) => console.error(err))
            .finally(() => setLoading(false));
    }, [filter]);

    return (
        <main>
            <h1>Sentinel: Login Monitor</h1>
            <p>{countFailed(events)} failed logins shown</p>

            <select value={filter} onChange={(e) => setFilter(e.target.value)}>
                <option value="">All</option>
                <option value="FAILED">Failed only</option>
                <option value="SUCCESS">Success only</option>
            </select>

            {loading ? (
                <p>Loading...</p>
            ) : (
                <ul>
                    {events.map((event) => (
                        <li key={event.id}>
                            [{event.status}] {event.username} from {event.ip_address}
                        </li>
                    ))}
                </ul>
            )}
        </main>
    );
}

export default App;


