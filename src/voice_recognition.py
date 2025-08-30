# src/voice_recognition.py
"""
Jarvis - Voice Recognition Module
Uses speech recognition for voice commands & speaker identification.
"""

import speech_recognition as sr
import os
import time

class VoiceRecognition:
    def __init__(self, settings):
        self.settings = settings
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Directory for storing registered voices
        self.data_path = "config/voices"
        os.makedirs(self.data_path, exist_ok=True)

        # Load trained voices (placeholder - needs model training)
        self.known_voices = {}  # {name: "voiceprint_data"}

    def listen(self, timeout=5):
        with self.microphone as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                return audio
            except sr.WaitTimeoutError:
                print("⏳ Listening timed out.")
                return None

    def recognize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"🗣 Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError:
            print("⚠️ Speech recognition service unavailable (offline mode needed).")
            return None

    def register_voice(self, name, audio):
        timestamp = int(time.time())
        file_path = os.path.join(self.data_path, f"{name}_{timestamp}.wav")

        with open(file_path, "wb") as f:
            f.write(audio.get_wav_data())

        print(f"📁 Saved new voice sample for {name}: {file_path}")

        # TODO: Process voiceprint for recognition
        self.known_voices[name] = file_path

    def identify_speaker(self, audio):
        """
        Placeholder for linking voice to known face.
        Would use ML-based speaker recognition.
        """
        # In full implementation, extract MFCC features & compare
        return "Unknown"
