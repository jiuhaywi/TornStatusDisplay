import { definePlugin } from "@utils/types";
import { getModule } from "@webpack";
import { PluginLogger } from "@utils/logger";
import Settings from "./settings";

const logger = PluginLogger("TornStatus");

let interval: NodeJS.Timeout;

async function fetchTornStatus(apiKey: string, userId: string) {
    try {
        const res = await fetch(`https://api.torn.com/user/${userId}?selections=travel,profile,status&key=${apiKey}`);
        const data = await res.json();

        if (data?.error) {
            logger.error("API Error:", data.error);
            return null;
        }

        const description = data?.status?.description || "Unknown";
        const location = data?.travel?.destination;
        const timestamp = data?.travel?.timestamp;

        const now = Math.floor(Date.now() / 1000);
        let startTime = now;

        if (location && timestamp) {
            const remaining = timestamp - now;
            startTime = timestamp - remaining;
        }

        return {
            details: description,
            state: location ? `Flying to ${location}` : description,
            timestamps: { start: startTime }
        };
    } catch (e) {
        logger.error("Failed to fetch Torn status", e);
        return null;
    }
}

export default definePlugin({
    name: "TornStatusPresence",
    description: "Show Torn travel status in Discord",
    settings: Settings,

    start(_, settings) {
        logger.log("Starting TornStatusPresence...");

        if (!settings.apiKey || !settings.userId) {
            logger.warn("Missing API Key or User ID");
            return;
        }

        interval = setInterval(async () => {
            const presence = await fetchTornStatus(settings.apiKey, settings.userId);
            if (presence) {
                const Activities = await getModule(m => m?.updateLocalPresence);
                Activities.updateLocalPresence({
                    name: "Torn",
                    type: 0, // "Playing"
                    ...presence
                });
                logger.log("Presence updated:", presence);
            }
        }, 5 * 60 * 1000); // every 5 mins
    },

    stop() {
        clearInterval(interval);
        const Activities = getModule(m => m?.updateLocalPresence);
        Activities?.clearLocalPresence?.();
        logger.log("Stopped TornStatusPresence.");
    }
});