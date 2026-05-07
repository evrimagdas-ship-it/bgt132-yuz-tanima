import cv2

def bulaniklastir(frame, faces):
    for (x, y, w, h) in faces:
        roi = frame[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(roi, (91, 91), 0)
        frame[y:y+h, x:x+w] = blur
    return frame