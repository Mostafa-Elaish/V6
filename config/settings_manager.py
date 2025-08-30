import json, os, threading
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "settings.json")
class SettingsManager:
    def __init__(self):
        self._lock = threading.Lock()
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError(f"Missing config file: {CONFIG_FILE}")
        self.reload()
    def reload(self):
        with open(CONFIG_FILE, "r") as f:
            self._data = json.load(f)
    def save(self):
        with self._lock:
            with open(CONFIG_FILE, "w") as f:
                json.dump(self._data, f, indent=2)
    def get(self, path, default=None):
        keys = path.split('.')
        v = self._data
        try:
            for k in keys:
                v = v[k]
            return v
        except Exception:
            return default
    def set(self, path, value):
        keys = path.split('.')
        d = self._data
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value
        self.save()
