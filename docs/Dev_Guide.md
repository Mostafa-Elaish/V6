# Jarvis Developer Guide

## Dependencies
- Python 3.11
- Flask (web dashboard)
- OpenCV (face recognition demo)
- PyTorch (future advanced models)
- SpeechRecognition + Vosk (offline ASR)
- pyTelegramBotAPI (Telegram bot)

## Folder Structure
```
Jarvis/
 ├── core/              # main AI modules
 ├── sensors/           # sensor drivers
 ├── ui/                # touchscreen UI
 ├── web/               # Flask dashboard
 ├── docs/              # wiring, manuals
 └── installer.sh       # one-shot installer
```

## Running
- Launch services with `systemd` or `supervisord`.
- Start web joystick: `python web/server.py`
- Start Telegram bot: `python core/telegram_bot.py`

## Notes
- No auto-update by design
- All offline
- Export logs encrypted
- Daily cleanup configurable
