import json
import os

CONFIG_PATH = "config/settings.json"

class SettingsManager:
    def __init__(self):
        if not os.path.exists(CONFIG_PATH):
            self.save({
                "guard_mode": False,
                "face_recognition": True,
                "voice_recognition": False,
                "wait_time": 10,
                "alarm_duration": 60
            })
        self.settings = self.load()

    def load(self):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)

    def save(self, data=None):
        if data is None:
            data = self.settings
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, f, indent=4)
        self.settings = data

    def update(self, key, value):
        self.settings[key] = value
        self.save()
