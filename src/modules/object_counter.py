import cv2

class ObjectCounter:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw_labels(self, frame, faces):
        count = len(faces)
        for i, (x, y, w, h) in enumerate(faces):
            # Yüzün üzerine numara yaz (Örn: Kisi 1)
            cv2.putText(frame, f'Kisi {i+1}', (x, y-10), self.font, 0.6, (0, 255, 0), 2)
            # Yüzün etrafına ince bir çerçeve çiz
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        
        # Ekranın sol üst köşesine toplam sayıyı yaz
        cv2.putText(frame, f'Toplam Yuz: {count}', (20, 40), self.font, 1, (255, 255, 255), 2)
        return frame