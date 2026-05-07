import cv2
import numpy as np
import os


base_path = os.path.dirname(os.path.abspath(__file__))
weights_path = os.path.join(base_path, "yolov3.weights")
cfg_path = os.path.join(base_path, "yolov3.cfg")
names_path = os.path.join(base_path, "coco.names")


with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]


net = cv2.dnn.readNet(weights_path, cfg_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def nesneleri_tespit_et(frame):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    tespitler = []
    if len(indices) > 0:
        
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            tespitler.append({"label": label, "x": x, "y": y, "w": w, "h": h})

    return tespitler



if __name__ == "__main__":
    cap = cv2.VideoCapture(0) 
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
       
        nesneleri_tespit_et(frame)
        
        
        cv2.imshow("Nesne Tanıma Test", frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()