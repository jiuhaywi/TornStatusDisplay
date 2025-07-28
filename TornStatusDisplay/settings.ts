import { definePluginSettings } from "@api/settings";

export default definePluginSettings({
    userId: {
        type: "string",
        description: "Your Torn user ID",
        default: ""
    },
    apiKey: {
        type: "string",
        description: "Your Torn API key",
        default: ""
    }
});