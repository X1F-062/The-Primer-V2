# Spec: The Primer v2 — Uyumlanan Yapay Zekâ Eğitmeni

## 1. Problem Tanımı ve Model Amacı
Yazılım mühendisliği kariyer yolculuğundaki oyuncunun karar verme dinamiklerine (tereddüt süresi, karar değiştirme, hata geçmişi, okuma hızı) göre anlık **dynamic scaffolding (ipucu / adaptif rehberlik)** ihtiyacını tahmin eden göreve özel (dikey) bir lojistik regresyon modeli devreye alınacaktır.

## 2. Altın Standart & Değerlendirme Kapısı (Eval Gate)
Eğitim sürecinde model artefaktı yayınlanmadan önce aşağıdaki kabul eşiklerinin (threshold) tamamını başarmak zorundadır. Eşiği geçmeyen model otomatik olarak reddedilir.

- **Doğruluk (Accuracy):** >= 0.85
- **F1-Skoru:** >= 0.80
- **Hassasiyet (Precision):** >= 0.80
- **Diferansiyel Test Toleransı (|p_onnx - p_oracle|):** < 1e-4

## 3. Kabul Örnekleri (Acceptance Scenarios)

### Senaryo 1: Yoğun Tereddüt Gösteren Acemi Oyuncu (İpucu Tetiklenir)
- **Girdi:** 
  - `karar_suresi_sn`: 45.0
  - `karar_degistirme_sayisi`: 4
  - `sahne_zorluk_derecesi`: 4
  - `onceki_yanlis_sayisi`: 2
  - `yazi_okuma_hizi_wpm`: 130.0
- **Beklenen Tahmin:** `ipucu_gerekli = 1` (p >= 0.80)
- **Davranış:** Oyun arayüzünde "Rehber Kod Analizcisi" belirir, zorluk yumuşatılır ve ipucu kartı açılır.

### Senaryo 2: Hızlı ve Kararlı Kıdemli Oyuncu (Müdahale Yapılmaz)
- **Girdi:** 
  - `karar_suresi_sn`: 8.0
  - `karar_degistirme_sayisi`: 0
  - `sahne_zorluk_derecesi`: 1
  - `onceki_yanlis_sayisi`: 0
  - `yazi_okuma_hizi_wpm`: 300.0
- **Beklenen Tahmin:** `ipucu_gerekli = 0` (p < 0.20)
- **Davranış:** Hikâye kesintisiz devam eder, ek süre baskısı veya ipucu gösterilmez.

### Senaryo 3: Sınırda Kararsızlık (Orta Seviye Müdahale)
- **Girdi:** 
  - `karar_suresi_sn`: 25.0
  - `karar_degistirme_sayisi`: 2
  - `sahne_zorluk_derecesi`: 3
  - `onceki_yanlis_sayisi`: 1
  - `yazi_okuma_hizi_wpm`: 180.0
- **Beklenen Tahmin:** `ipucu_gerekli = 1` (p >= 0.50)
- **Davranış:** Arayüzde hafif vurgulama (subtle hint pulse) yapılır.
