# src/guard_mode.py
"""
Jarvis - Guard Mode Module
Handles security features:
 - Face recognition + voice recognition
 - Guard mode ON/OFF
 - Configurable waiting times
 - Snapshot / video evidence
 - Telegram alerts
"""

import time
import threading
from src.camera import Camera
from src.voice_recognition import VoiceRecognition
from src.telegram_alert import TelegramAlert
from src.settings_manager import SettingsManager

class GuardMode:
    def __init__(self, settings: SettingsManager):
        self.settings = settings
        self.camera = Camera(settings)
        self.voice = VoiceRecognition(settings)
        self.telegram = TelegramAlert(settings)

        self.active = False
        self.wait_time = self.settings.get("guard_wait_time", 10)
        self.alarm_duration = self.settings.get("alarm_duration", 30)

    def enable(self):
        self.active = True
        print("🛡️ Guard Mode ENABLED")

    def disable(self):
        self.active = False
        print("🛑 Guard Mode DISABLED")

    def monitor(self):
        while self.active:
            print("👁️ Monitoring...")
            face_name = self.camera.recognize_face()

            if face_name == "Unknown":
                print("⚠️ Unknown face detected!")
                self.telegram.send_alert("🚨 Unknown face detected!")

                # Take evidence (snapshot or video)
                if self.settings.get("evidence_mode", "snapshot") == "snapshot":
                    file_path = self.camera.take_snapshot()
                else:
                    duration = self.settings.get("video_duration", 5)
                    file_path = self.camera.record_video(duration)

                # Send to Telegram
                self.telegram.send_file(file_path)

                # Ask for identity (voice response)
                audio = self.voice.listen(timeout=self.wait_time)
                if audio:
                    response = self.voice.recognize_speech(audio)
                    if response:
                        self.telegram.send_alert(f"🗣 Person said: {response}")
                    else:
                        self.trigger_alarm()
                else:
                    self.trigger_alarm()

            time.sleep(2)  # small delay between checks

    def trigger_alarm(self):
        print("🚨 ALARM TRIGGERED!")
        self.telegram.send_alert("🚨 ALARM TRIGGERED!")
        self.camera.flash_rgb("red", duration=self.alarm_duration)
