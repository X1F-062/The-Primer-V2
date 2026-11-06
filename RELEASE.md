# Release & Deployment Belgesi — v2.0

## Hugging Face Model Sabit Linki
Model `main` dalından değil, commit SHA'sına sabitlenerek yayınlanmıştır:
`https://huggingface.co/seyyah/primer-v2-tutor/resolve/a1b2c3d4e5f67890/model.onnx`

## Sürüm Değişiklik Günlüğü (v1.0 -> v2.0)
- **v1.0:** Sabit kurallara (IF/ELSE) dayalı uyumlandırma arayüzü.
- **v2.0:** Oyuncu davranışını öğrenen `sklearn` tabanlı lojistik regresyon ONNX modeli entegre edildi.

## Rollback (Geri Alma) Planı
Yeni yayınlanan sürümde bir uyuşmazlık tespit edilirse:
1. İstemci kodundaki model URL'si bir önceki kararlı commit olan `v1.0-commit-hash` sürümüne çekilir:
   `https://huggingface.co/seyyah/primer-v2-tutor/resolve/v1.0-commit-hash/model.onnx`
2. Tarayıcı önbelleği (ServiceWorker Cache) temizlenerek varsayılan kural motoruna düşülür (Fallback Mode).

---

## Güvenli Devreye Alma Stratejileri (Deployment Strategies)

1. **Shadow Deployment (Gölge Dağıtım):**
   - Yeni `v2.0` modeli arka planda sessizce çalıştırılır. Tahminleri kullanıcı arayüzünü etkilemez; yalnızca loglanır.
   - 48 saat boyunca mevcut `v1.0` kural sistemi ile `v2.0` tahmin farkları gözlemlenir.

2. **Canary Deployment (Kanarya Dağıtımı):**
   - Canlı trafiğin **%5**'i rastgele seçilerek `v2.0` ONNX modeline yönlendirilir.
   - Hata oranları, istemci tarafı JS istisnaları ve oturum terk oranları (drop-off) izlenir.

3. **Progressive Rollout (Aşamalı Geçiş):**
   - Kanarya adımı sorunsuz geçilirse trafik kademeli olarak artırılır: **%25 -> %50 -> %100**.

---

## Mimari Dağıtım Kararı & Ödünleşim (Trade-off) Matrisi

| Değerlendirme Kriteri | Option A: Tarayıcı İçi (`onnxruntime-web`) | Option B: Mobil Cihaz İçi (`React Native / Expo`) | Option C: Kendi Sunucunuz (`Render.com API`) |
| :--- | :--- | :--- | :--- |
| **1. Ağ Gereksinimi & Latency** | İlk yüklemede `.onnx` indirilir; sonraki çıkarımlar 0ms ağ gecikmesiyle **çevrimdışı** çalışır. | Model uygulamaya gömülüdür (bundled). **Tamamen internetsiz** ve 2ms altında çalışır. | Her karar adımında HTTP isteği atılır. **İnternet zorunludur** (Ağ gecikmesi: ~150-300ms). |
| **2. Veri Gizliliği (KVKK)** | Karar verileri ve cihaz metrikleri **cihazdan dışarı asla çıkmaz**. | Veri **tamamen cihaz içinde** kalır, maksimum gizlilik sağlanır. | Karar verileri sunucuya iletilir; **KVKK & TLS uçtan uca koruma** gerektirir. |
| **3. Model Fikri Mülkiyeti (IP/REA)** | Model istemciye indiği için tersine mühendislik ile **kopyalanabilir**. | Uygulama paketinden (APK/IPA) çıkarılma **riski vardır**. | Model sunucuda saklı kalır. **Fikri mülkiyet %100 koruma altındadır**. |

**Seçilen Mimari Karar:** Web/GitHub Pages deployment için **Option A (`onnxruntime-web`)** seçilmiştir. Sıfır sunucu maliyeti ve internetsiz çalışabilme avantajı birincil öncelliktir.
