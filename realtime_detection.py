import cv2
import numpy as np
from tensorflow.keras.models import load_model
from pygame import mixer
import time

# Load your trained model
model = load_model("eye_model.h5")

# Initialize alert sound
mixer.init()
mixer.music.load("music.wav")

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
closed_frames = 0
frame_check = 15  # adjust sensitivity

while True:DrowsinessDetection_Web/
│
├── static/                     # CSS, JS, icons
│   ├── style.css
│   └── script.js
│
├── templates/                  # HTML files
│   └── index.html
│
├── model/
│   ├── eye_model.h5
│   └── shape_predictor_68_face_landmarks.dat
│
├── music/
│   └── music.wav
│
├── app.py                      # Flask backend
└── requirements.txt

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) < 2:
            closed_frames += 1
            if closed_frames >= frame_check:
                cv2.putText(frame, "DROWSY ALERT!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                try:
                    mixer.music.play()
                except:
                    pass
        else:
            closed_frames = 0

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
