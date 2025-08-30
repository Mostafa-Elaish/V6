# src/voice_recognition.py
"""
Jarvis - Voice Recognition Module
Identifies speakers and links them to saved face profiles
"""

import os
import numpy as np
import speech_recognition as sr
import librosa
import pickle

class VoiceRecognition:
    def __init__(self, db_path="data/voice_profiles/"):
        self.db_path = db_path
        os.makedirs(self.db_path, exist_ok=True)
        self.recognizer = sr.Recognizer()

    def _extract_features(self, audio_file):
        """Extract MFCC features from audio file for speaker recognition"""
        y, sr_rate = librosa.load(audio_file, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr_rate, n_mfcc=13)
        return np.mean(mfcc.T, axis=0)

    def enroll_voice(self, name: str, audio_file: str):
        """Enroll a new voice and link it with a person"""
        features = self._extract_features(audio_file)
        profile_path = os.path.join(self.db_path, f"{name}.pkl")

        with open(profile_path, "wb") as f:
            pickle.dump(features, f)

        print(f"✅ Voice enrolled for {name}")

    def recognize_voice(self, audio_file: str):
        """Recognize who is speaking from stored profiles"""
        features = self._extract_features(audio_file)
        best_match = None
        best_score = float("inf")

        for file in os.listdir(self.db_path):
            if file.endswith(".pkl"):
                with open(os.path.join(self.db_path, file), "rb") as f:
                    stored_features = pickle.load(f)
                    distance = np.linalg.norm(features - stored_features)
                    if distance < best_score:
                        best_score = distance
                        best_match = file.replace(".pkl", "")

        if best_match:
            print(f"🎤 Recognized voice: {best_match}")
            return best_match
        else:
            print("❌ Unknown voice")
            return None

    def listen_and_save(self, save_path="temp_audio.wav"):
        """Listen via mic and save audio"""
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = self.recognizer.listen(source)

            with open(save_path, "wb") as f:
                f.write(audio.get_wav_data())
            
            return save_path
