# Jarvis User Manual

## Setup
1. Power on Jarvis (Raspberry Pi 5 + peripherals).
2. Configure Wi-Fi from touchscreen settings menu.
3. Set Master PIN (required for security actions).

## Enrollment
- Go to **Profiles → Add**.
- Jarvis will ask to scan your **face**.
- Then speak sample sentences for **voice recognition**.
- Assign a **name**.

## Guard Mode
- Enable from touchscreen or Telegram.
- If unknown detected:
  - Jarvis says: “I don’t know you, who are you?”
  - Waits configurable time (default 10s).
  - If no response → Alarm mode (RGB LED flash + Telegram alert).

## Alerts
- Alerts sent via Telegram bot (photo/video).
- Retention default: 30 days (can be changed in settings).
- Manual delete of records only.

## Movement
- Control via web dashboard joystick.
- Motor calibration in Settings.

## Data Export
- Export is encrypted by default.
- Only the Master PIN owner can decrypt.
- Remote change of Master PIN disabled.