import cv2
import os
base_path = os.path.dirname(os.path.abspath(__file__))


face_model_path = os.path.join(base_path, "model_dosyasi_adi.xml")

def yuz_tespit_et(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces 