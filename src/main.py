# src/main.py
"""
Jarvis AI Robot - Main Entry Point
"""

from face_recognition import FaceRecognition
from voice_recognition import VoiceRecognition
from movement_control import MovementControl
from guard_mode import GuardMode
from telegram_interface import TelegramBot
from settings_manager import SettingsManager

def main():
    print("🚀 Starting Jarvis...")

    # Load settings
    settings = SettingsManager("config/config.json")

    # Initialize modules
    face = FaceRecognition(settings)
    voice = VoiceRecognition(settings)
    movement = MovementControl(settings)
    guard = GuardMode(face, voice, settings)
    telegram = TelegramBot(settings, guard, movement)

    # Main loop
    try:
        while True:
            guard.run_cycle()
    except KeyboardInterrupt:
        print("🛑 Jarvis shutting down...")

if __name__ == "__main__":
    main()
