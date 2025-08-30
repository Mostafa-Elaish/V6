# Jarvis – AI Home Assistant Robot

Jarvis is an **offline, AI-powered home assistant robot** built on **Raspberry Pi 5**.  
It integrates facial & voice recognition, emotion detection, Guard Mode, IoT device control, and a web dashboard for movement.

⚡ **Privacy-first:** Runs fully **offline**, no internet/cloud required.  
🎙️ **Wake word:** "Jarvis" – listens only after being called.  
🛡️ **Guard Mode:** Detects unknown faces/voices, sends alerts, triggers configurable alarms.  
📱 **Telegram Integration:** Secure alerts & command interface.  
📷 **Camera & Sensors:** Vision, ultrasonic, PIR, temperature, humidity, light, RGB LED.  
🖥️ **Touchscreen + Web UI:** Local configuration & joystick movement.  

---

## 📂 Repository Structure

```
V6/
│── Wiring_Guide.md      # Hardware wiring instructions  
│── Features_List.md     # Full list of Jarvis features  
│── User_Manual.md       # End-user manual  
│── Dev_Guide.md         # Developer setup & guide  
│── README.md            # Project introduction (this file)  
│── src/                 # Source code (to be added)  
│── libs/                # Custom libraries (to be added)  
│── installer/           # Setup scripts (to be added)  
```

---

## 🚀 Features

- **Offline Wake Word & Speech Recognition**  
- **Facial Recognition + Voiceprint Linking**  
- **Emotion Detection**  
- **Guard Mode with Telegram Alerts**  
- **Encrypted Data & Exports**  
- **Configurable Retention & Bulk Delete**  
- **Web Dashboard Joystick Control**  
- **Touchscreen Settings Panel**  

---

## 🛠️ Development

1. Install dependencies (see `Dev_Guide.md`)  
2. Run local Flask server for web UI  
3. Connect sensors & verify wiring (`Wiring_Guide.md`)  
4. Test modules step by step  
5. Extend features as needed  
