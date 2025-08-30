#!/usr/bin/env python3
from config.settings_manager import SettingsManager
from core.guard_mode import GuardMode
from core.recognition import Recognition
from core.sensors import SensorManager
from core.movement import Movement
from core.notifications import TelegramBot
from core.ui import UI

def main():
    settings = SettingsManager()
    telegram = TelegramBot(settings)
    recognition = Recognition(settings, telegram)
    sensors = SensorManager(settings, telegram)
    movement = Movement(settings)
    guard = GuardMode(settings, recognition, sensors, telegram)
    ui = UI(settings, movement, guard, telegram)

    print("🚀 Jarvis started successfully!")
    ui.run()

if __name__ == "__main__":
    main()
