# TornStatusDisplay

**TornStatusDisplay** is a standalone Python application that shows your current [Torn](https://www.torn.com/) status using a custom **Discord Rich Presence**. It displays whether you are okay, hospitalised, flying, or abroad (including hospitalised abroad). When you are flying, it displays your current flight time (the green discord text), and your remaining time (shown via the white text). It also displays where you are travelling to. This tool uses one API request every update (every 300s while flying, and 60s while not flying {This can be changed in `settings.py`!}). Therefore, being rate limited for this tool will not be common. This script must be running on the same machine that you are logged into discord on (the discord desktop app only). There is also an 'anonymous' mode, which hides timers so no one on discord can see your flight times! This project uses the MIT License. Please refer to this [LICENSE](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/LICENSE) before using, sharing, or modifying this project in any way.

> See some [Examples](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/Examples.md)

---

## 📦 Requirements

- [Python 3.9+](https://www.python.org/downloads/)
- Torn **API key** (Limited) and **User ID**
- [pypresence](https://pypi.org/project/pypresence/), [customtkinter](https://customtkinter.tomschimansky.com/), and [requests](https://pypi.org/project/requests/). install with bash: `pip install pypresence requests customtkinter` (This is `requirements.bat`!)

---

## ⚠️ Disclaimer

> Use this tool at your own risk.

- This application uses the Discord Rich Presence API via a **local connection**, which **should** be safe, however, I am **NOT** responsible for anything which is as a result of using this tool. Refer to the [LICENSE](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/LICENSE) for more info.
- No data is sent to any external servers, and everything (except contacting Discord and Torn APIs) is local.

---

## 💻 Setup Instructions

> This is designed to be a simple tutorial, however, if you need to contact me for any reason, please do so via Direct Messages on discord. My Discord UserID: `1245051294364864588`

- [1.](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/1.1.md) - Setup (Setting up the main python file.)
- [2.](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/2.md) - Application (Setting up your Discord Application)
- [3.](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/3.md) - Credentials (Adding your Keys, and IDs into creds.py)
- [4.](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/4.md) - Done


[Production](https://github.com/jiuhaywi/TornStatusDisplay/blob/main/Production.md)
