# src/face_recognition.py
"""
Jarvis - Face Recognition Module
Uses OpenCV for face detection and recognition.
"""

import cv2
import os
import numpy as np
import time

class FaceRecognition:
    def __init__(self, settings):
        self.settings = settings
        self.data_path = "config/faces"
        os.makedirs(self.data_path, exist_ok=True)

        # Load pre-trained classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Placeholder for recognizer (LBPH)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self._load_training_data()

    def _load_training_data(self):
        faces, labels = [], []
        label_map = {}

        if not os.listdir(self.data_path):
            print("⚠️ No faces trained yet.")
            return

        for idx, person in enumerate(os.listdir(self.data_path)):
            person_path = os.path.join(self.data_path, person)
            label_map[idx] = person
            for img_name in os.listdir(person_path):
                img_path = os.path.join(person_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    faces.append(img)
                    labels.append(idx)

        if faces:
            self.recognizer.train(faces, np.array(labels))
            self.label_map = label_map
            print("✅ Face recognition model trained.")

    def detect_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        results = []
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            label, confidence = self.recognizer.predict(roi_gray) if hasattr(self, 'label_map') else (-1, 0)

            if label != -1:
                results.append({"name": self.label_map[label], "confidence": confidence})
            else:
                results.append({"name": "Unknown", "confidence": 0})
        return results

    def register_face(self, name, frame):
        person_path = os.path.join(self.data_path, name)
        os.makedirs(person_path, exist_ok=True)

        timestamp = int(time.time())
        img_path = os.path.join(person_path, f"{timestamp}.jpg")
        cv2.imwrite(img_path, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

        print(f"📸 Face saved for {name} at {img_path}")
        self._load_training_data()
