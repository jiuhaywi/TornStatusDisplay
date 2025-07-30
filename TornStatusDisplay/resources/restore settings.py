import json

settings_data = {
    "show_time_left": "on",
    "fly_delay": 300,
    "ground_delay": 60
    }








with open("settings.tss", "w") as f:
    json.dump(settings_data, f, indent=4)
