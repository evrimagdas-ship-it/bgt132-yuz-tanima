import cv2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.face_engine import FaceEngine
from modules.privacy_filter import PrivacyFilter
from modules.object_counter import ObjectCounter # Yeni ekledik

def main():
    detector = FaceEngine()
    filter = PrivacyFilter(blur_ratio=51)
    counter = ObjectCounter() # Yeni ekledik

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret: break

        faces = detector.detect_faces(frame)
        
        # Önce etiketleri ve sayıları yazalım
        frame = counter.draw_labels(frame, faces)
        
        # Sonra sansürü uygulayalım
        frame = filter.apply_blur(frame, faces)

        cv2.imshow('BGT 132 Gelişmiş Sistem', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()