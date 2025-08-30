# # src/guard_mode.py
"""
Jarvis - Guard Mode with Face + Voice Recognition
"""

import time
from src.face_recognition_module import FaceRecognition
from src.voice_recognition import VoiceRecognition
from src.alerts import Alerts

class GuardMode:
    def __init__(self, wait_time=10, alarm_duration=60, enable_guard=True):
        self.face_recognition = FaceRecognition()
        self.voice_recognition = VoiceRecognition()
        self.alerts = Alerts()
        self.wait_time = wait_time
        self.alarm_duration = alarm_duration
        self.enable_guard = enable_guard

    def verify_identity(self):
        """
        Verify both face & voice before allowing access
        """
        print("🔒 Guard Mode Active")

        # Step 1 – Detect Face
        face_name = self.face_recognition.recognize_face()

        # Step 2 – Detect Voice
        audio_file = self.voice_recognition.listen_and_save()
        voice_name = self.voice_recognition.recognize_voice(audio_file)

        # Step 3 – Decision Logic
        if face_name and voice_name:
            if face_name == voice_name:
                print(f"✅ Identity verified: {face_name}")
                return True
            else:
                print(f"⚠️ Face ({face_name}) does not match Voice ({voice_name})")
                self._handle_unknown()
                return False

        elif face_name and not voice_name:
            print(f"⚠️ Face recognized as {face_name}, but voice unknown")
            self._handle_unknown()
            return False

        elif not face_name and voice_name:
            print(f"⚠️ Voice recognized as {voice_name}, but face unknown")
            self._handle_unknown()
            return False

        else:
            print("❌ Unknown face and unknown voice")
            self._handle_unknown()
            return False

    def _handle_unknown(self):
        """
        Ask 'Who are you?' → Wait → Alarm if no valid response
        """
        print("🤖 Jarvis: 'I don’t know you, who are you?'")
        time.sleep(self.wait_time)

        # If no manual confirmation → alarm
        print("🚨 Triggering alarm (Guard Mode)")
        self.alerts.trigger_alarm(duration=self.alarm_duration)
