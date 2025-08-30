from face_recognition import FaceRecognition
from voice_recognition import VoiceRecognition
from movement_control import MovementControl
from guard_mode import GuardMode
from telegram_interface import TelegramInterface
from settings_manager import SettingsManager

def main():
    print("🚀 Jarvis AI starting...")

    settings = SettingsManager("config/config.json")
    face = FaceRecognition(settings)
    voice = VoiceRecognition(settings)
    move = MovementControl(settings)
    guard = GuardMode(settings, face, voice)
    telegram = TelegramInterface(settings, guard)

    print("✅ Jarvis is running. Use Telegram or voice command to interact.")

if __name__ == "__main__":
    main()
