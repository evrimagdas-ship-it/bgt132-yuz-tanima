# BGT 132 - Yüz Tanıma ve Gizlilik Filtresi Sistemi

Bu proje, görüntü işleme tekniklerini kullanarak gerçek zamanlı yüz tespiti yapan ve kişisel gizliliği korumak amacıyla tespit edilen yüzleri otomatik olarak bulanıklaştıran bir Python uygulamasıdır.

## 🚀 Özellikler
- **Gerçek Zamanlı Tespit:** Kamera görüntüsü üzerinden anlık yüz takibi.
- **Gizlilik Filtresi:** Tespit edilen yüz bölgelerine dinamik Gaussian Blur (bulanıklaştırma) uygulaması.
- **Modüler Yapı:** Nesne yönelimli programlama (OOP) prensiplerine uygun, geliştirilebilir kod mimarisi.

## 📁 Proje Yapısı
- `src/core/main.py`: Uygulamanın ana giriş noktası ve kamera döngüsü.
- `src/modules/face_engine.py`: Yüz tespiti yapan motor sınıfı.
- `src/modules/privacy_filter.py`: Bulanıklaştırma efektini yöneten filtre sınıfı.
- `docs/`: Proje dokümantasyonu ve analiz belgeleri.

## 🛠️ Kurulum ve Çalıştırma
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install opencv-python