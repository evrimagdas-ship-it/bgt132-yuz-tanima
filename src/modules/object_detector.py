import cv2

class ObjectCounter:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw_labels(self, frame, faces):
        count = len(faces)
        for i, (x, y, w, h) in enumerate(faces):
            # Yüzün üzerine "Insan" ve "ID" yaz
            label = f'Insan #{i+1}'
            cv2.putText(frame, label, (x, y-10), self.font, 0.7, (0, 255, 255), 2)
            
            # Nesneyi bir kutu içine al
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        
        # Bilgi paneli
        cv2.rectangle(frame, (10, 10), (250, 60), (0, 0, 0), -1)
        cv2.putText(frame, f'Algilanan Nesne: {count}', (20, 45), self.font, 0.8, (255, 255, 255), 2)
        
        return frame