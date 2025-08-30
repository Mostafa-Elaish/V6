import numpy as np
import cv2, os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "demo", "faces")
os.makedirs(DATA_DIR, exist_ok=True)
CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def capture_and_save(name, cam_index=0, count=20):
    cap = cv2.VideoCapture(cam_index)
    saved = 0
    person_dir = os.path.join(DATA_DIR, name)
    os.makedirs(person_dir, exist_ok=True)
    while saved < count:
        ret, frame = cap.read()
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            face = gray[y:y+h, x:x+w]
            fname = os.path.join(person_dir, f'{name}_{saved:03d}.png')
            cv2.imwrite(fname, face)
            saved += 1
            print('Saved', fname)
            if saved >= count: break
    cap.release()
    cv2.destroyAllWindows()
    return saved

def train_lbph_model(output_path='model_lbph.yml'):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []
    label_map = {}
    curr_label = 0
    for person in os.listdir(DATA_DIR):
        pdir = os.path.join(DATA_DIR, person)
        if not os.path.isdir(pdir): continue
        label_map[curr_label] = person
        for fn in os.listdir(pdir):
            path = os.path.join(pdir, fn)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(curr_label)
        curr_label += 1
    if len(faces)==0:
        print('No faces to train. Use capture_and_save() first.')
        return None
    recognizer.train(faces, np.array(labels))
    recognizer.write(output_path)
    with open(output_path + '.map', 'w') as f:
        f.write(str(label_map))
    print('Model trained and saved to', output_path)
    return output_path

def recognize_from_camera(model_path='model_lbph.yml', cam_index=0):
    if not os.path.exists(model_path):
        print('Model not found. Train first.')
        return
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)
    with open(model_path + '.map','r') as f:
        label_map = eval(f.read())
    cap = cv2.VideoCapture(cam_index)
    while True:
        ret, frame = cap.read()
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            face = gray[y:y+h, x:x+w]
            label, conf = recognizer.predict(face)
            name = label_map.get(label, 'unknown')
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, f'{name} ({conf:.0f})', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
        cv2.imshow('Recognition', frame)
        if cv2.waitKey(1)&0xFF==27: break
    cap.release()
    cv2.destroyAllWindows()
