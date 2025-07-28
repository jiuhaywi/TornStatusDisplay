# TornStatusDisplay

**TornStatusDisplay** is a [Vencord](https://vencord.dev) plugin that displays your current [Torn](https://www.torn.com/) status as a custom Discord Rich Presence.

> Example: `Flying to UK (1h 34m remaining)` — or `Hospitalized, Abroad (UK)`

---

## 📦 Requirements

- [Vencord](https://vencord.dev) client mod installed and running.
- A Torn API key and your user ID (configured inside the plugin settings panel).

---

## ⚠️ Disclaimer

> **Use this plugin at your own risk.**

- Vencord is a **client modification**, and use of it is **against Discord's Terms of Service**.
- This plugin uses your Discord account token via the client to update Rich Presence.
- I am **not responsible** for any consequences that may result from using this plugin. Refer to the license for more info.

---

## 💻 Installation

- If these instructions are too hard, Vencord modding is not for you. However, if you need anything, you can dm me `1245051294364864588` on Discord.

1. Download and unzip the latest release from releases.
2. Place the `TornStatusDisplay` folder in your Vencord `plugins` directory:
   - Windows: `%appdata%\Vencord\plugins`
   - Linux/macOS: `~/.config/Vencord/plugins`
3. Enable the plugin in **Vencord Settings → Plugins**.
4. Click the ⚙️ icon to open plugin settings.
5. Enter your Torn **User ID** and **API Key** (Use a Limited Key).

---

## 🛠️ Features

- Updates every 5 minutes with your current Torn status.
- Displays travel state, hospital/jail status, and travel timers with timestamps.
- Auto-calculated timers and dynamic updates.
- Lightweight and local-only — no external servers or data logging.

---

## 📚 License

This project is licensed under the MIT License — see `LICENSE` for details.