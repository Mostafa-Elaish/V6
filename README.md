# Jarvis v6

Reference implementation for an offline, privacy-first home assistant robot:
- Face recognition + voiceprint linking
- Emotion detection
- Guard Mode (configurable waiting time, duration, LED alarm)
- Telegram alerts + command interface
- Web joystick control (LAN only)
- 7” touch UI ready hooks
- Local retention + daily purge scheduling (no cloud)
- Encrypted exports (Master PIN)

## Quick start
1. Clone repo to your Pi.
2. `bash install/install.sh`
3. `python3 src/movement/flask_server.py`
4. Open `http://<pi-ip>:8080` to try the joystick + Guard toggle.

## Folders
- `install/` – venv + deps
- `config/` – system settings
- `src/` – reference demos
- `web_dashboard/` – joystick UI
- `docs/` – PDFs (wiring, manual, features, dev guide)
- `demo/` – sample faces, media placeholders
