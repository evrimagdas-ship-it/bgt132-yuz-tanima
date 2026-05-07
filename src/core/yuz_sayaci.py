import cv2

def sayac_yaz(frame, faces):
    # Liste uzunluğu bize kişi sayısını verir
    kisi_sayisi = len(faces) if faces is not None else 0
    
    # Metin ayarları
    font = cv2.FONT_HERSHEY_SIMPLEX
    konum = (20, 50)
    font_olcegi = 1
    renk = (0, 255, 0) # Yeşil
    kalinlik = 2

    # Ekrana yazdırma
    metin = f"Kisi Sayisi: {kisi_sayisi}"
    cv2.putText(frame, metin, konum, font, font_olcegi, renk, kalinlik)
    
    return frame