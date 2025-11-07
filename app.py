from flask import Flask, render_template, Response
import cv2
import numpy as np
from pygame import mixer
from tensorflow.keras.models import load_model
from utils.detector import detect_drowsiness

app = Flask(__name__)

# Load model and alert sound
model = load_model("model/eye_model.h5")
mixer.init()
mixer.music.load("music/music.wav")

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_drowsiness(frame, model, mixer)
        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    cap.release()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)
