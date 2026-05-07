import cv2

class PrivacyFilter:
    def __init__(self, blur_ratio=51):
        
        self.blur_ratio = blur_ratio

    def apply_blur(self, frame, faces):
        for (x, y, w, h) in faces:
            # Yüz bölgesini al
            face_roi = frame[y:y+h, x:x+w]
            # Bulanıklaştır
            blurred_face = cv2.GaussianBlur(face_roi, (self.blur_ratio, self.blur_ratio), 0)
            # Yerine koy
            frame[y:y+h, x:x+w] = blurred_face
            
        return frame