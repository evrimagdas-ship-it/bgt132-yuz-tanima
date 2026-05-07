import cv2
import os

class FaceEngine:
    def __init__(self):
        
        cascade_name = 'haarcascade_frontalface_default.xml'
        
        
        cascade_path = os.path.join(cv2.data.haarcascades, cascade_name)
        
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        
        if self.face_cascade.empty():
            print("HATA: Yüz tanıma modeli yüklenemedi! Dosya yolu yanlış olabilir.")

    def detect_faces(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(
            gray_frame, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        return faces