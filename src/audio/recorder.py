import sounddevice as sd
import soundfile as sf
import os, datetime

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'demo', 'media')
os.makedirs(OUT_DIR, exist_ok=True)

def record(duration=3, samplerate=16000, channels=1):
    print(f'Recording {duration}s...')
    rec = sd.rec(int(duration*samplerate), samplerate=samplerate, channels=channels)
    sd.wait()
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    path = os.path.join(OUT_DIR, f'rec_{ts}.wav')
    sf.write(path, rec, samplerate)
    print('Saved:', path)
    return path
