# src/telegram_alert.py
"""
Jarvis - Telegram Alert Module
Handles secure notifications & evidence delivery via Telegram
"""

import os
import requests
from src.settings_manager import SettingsManager

class TelegramAlert:
    def __init__(self, settings: SettingsManager):
        self.settings = settings
        self.bot_token = self.settings.get("telegram_bot_token")
        self.chat_id = self.settings.get("telegram_chat_id")

    def send_alert(self, message: str):
        """Send a text alert message via Telegram"""
        if not self.bot_token or not self.chat_id:
            print("⚠️ Telegram not configured")
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}

        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print(f"📨 Alert sent: {message}")
            else:
                print(f"❌ Failed to send alert: {response.text}")
        except Exception as e:
            print(f"❌ Telegram error: {e}")

    def send_file(self, file_path: str):
        """Send snapshot or video file via Telegram"""
        if not os.path.exists(file_path):
            print("⚠️ File not found:", file_path)
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendDocument"
        files = {"document": open(file_path, "rb")}
        data = {"chat_id": self.chat_id}

        try:
            response = requests.post(url, data=data, files=files)
            if response.status_code == 200:
                print(f"📨 File sent: {file_path}")
            else:
                print(f"❌ Failed to send file: {response.text}")
        except Exception as e:
            print(f"❌ Telegram file error: {e}")
