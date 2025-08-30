import time, threading
class GuardMode:
    def __init__(self, settings, recognition, sensors, telegram):
        self.settings = settings
        self.recognition = recognition
        self.sensors = sensors
        self.telegram = telegram
        self._running = False
    def start(self):
        if self._running: return
        self._running = True
        threading.Thread(target=self._loop, daemon=True).start()
    def stop(self):
        self._running = False
    def _loop(self):
        while self._running:
            if self.settings.get('security.guard_mode'):
                face = self.recognition.detect_face_once()
                if face == 'Unknown':
                    print('⚠️ Unknown detected - handling...')
                    self.telegram.send_alert('Unknown detected by Jarvis')
            time.sleep(2)
