import cv2

class BaseCamera: # Sınıf 1
    def __init__(self, camera_id=0):
        # Encapsulation: Kamera nesnesini private yaparak dışarıdan müdahaleyi kısıtlıyoruz
        self.__cap = cv2.VideoCapture(camera_id)

    def get_frame(self):
        ret, frame = self.__cap.read()
        return ret, frame

    def close(self):
        self.__cap.release()