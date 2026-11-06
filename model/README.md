# Model Kartı: Primer v2 Adaptif Eğitmen

## Model Detayları
- **Geliştirici:** Primer AI Ekibi
- **Model Tipi:** Göreve Özel İkili Lojistik Regresyon (`sklearn → ONNX`)
- **Sürüm:** `v2.0.0`
- **Lisans:** MIT

## Kullanım Amacı (Intended Use)
- **Birincil Kullanım:** The Primer uygulamasında oyuncuların bocalama anlarını gerçek zamanlı tespit ederek dynamic hint/scaffolding sunmak.
- **Kapsam Dışı Kullanım:** Genel amaçlı sohbet, oyuncu yetkinlik puanlaması veya akademik başarı sınav değerlendirmeleri için kullanılmamalıdır.

## Eğitim Verisi
- 15 Gerçek kullanıcı oturumu + 85 Sentetik oturum (Toplam 100 satır).
- `kaynak` sütunu ile gerçek ve sentetik ayrımı yapılmıştır.

## Performans Metrikleri
- **Accuracy:** 0.9500
- **F1-Score:** 0.9744
- **Precision:** 1.0000
- **Recall:** 0.9500

## Sınırlılıklar ve Sınırlar
- Model, WPM (Kelime Okuma Hızı) değerinin 50'nin altında veya 500'ün üzerinde olduğu ekstrem durumlarda sapma gösterebilir.
- Ağır donanım kısıtı olan istemcilerde çıkarım gecikmesi (latency) < 5ms olarak ölçülmüştür.
