import cv2


siniflar = {0: "Insan", 15: "Kedi", 16: "Kopek", 67: "Telefon", 73: "Kitap/Kalem"}

def etiket_yaz(frame, tespitler):
    for nesne in tespitler:
        x, y, w, h, cid = nesne["x"], nesne["y"], nesne["w"], nesne["h"], nesne["id"]
        
        isim = siniflar.get(cid, "Nesne")
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, isim, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    
    return frame