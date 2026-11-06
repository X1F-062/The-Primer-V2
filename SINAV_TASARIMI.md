# Vizeye Hazırlık Düşünce Egzersizi: Sizinle Uyumlanan Klasik Sınav Tasarımı

## 1. Uyumlanan Sınav Senaryo Sorusu
**Senaryo:** *"Önünüzde günlük 1 milyon istek alan, kullanıcıların finansal işlemler yaptığı bir microservice mimarisi var. Takımınız, bu mimarideki monolitik veritabanını mikro servis tabanlı event-driven yapıya geçirmeyi planlıyor. Ancak canlı sistemde veri kaybı yaşanmaması ve downtime olmaması gerekiyor."*

**Soru:** 
Aşağıdaki adımları kavramsal gerekçeleriyle açıklayınız:
1. Bu geçişte **Shadow Deployment** ve **Canary Deployment** tekniklerini veritabanı senkronizasyonunda nasıl birleştirirsiniz?
2. Test sürecinde **Diferansiyel Test (Parite Testi)** mekanizmasını bir "Test Kahini (Oracle)" ile nasıl kurgularsınız? Fark toleransınız ne olmalıdır?
3. Üretim ortamındaki sistem güvenilirliği için **3V (Velocity, Validation, Versioning)** ilkelerini bu mimari dönüşüme nasıl uygularsınız?

## 2. Beklenen Temel Kavramlar ve Çeldiriciler

### A. Beklenen Temel Kavramlar (Öz ve Gerekçe)
- **Shadow Reads/Writes:** Eski ve yeni veritabanına eşzamanlı yazma (dual-write); kullanıcı yanıtı eski veritabanından dönerken yeni veritabanının arkadan takip etmesi.
- **Diferansiyel Oracle:** Eski monolit sistem "Oracle" kabul edilerek aynı istekler yeni servise paralel atılır; yanıtlar byte-level veya semantik karşılaştırılır.
- **Fail-Safe Rollback:** Saniye cinsinden geri alma stratejisinin tanımlanmış olması.

### B. Çeldiriciler ve Ezber Yanılgıları (Distractors)
- **Yanlış Yaklaşım A:** *"Sistemi gece 02:00'de kapatıp bakıma alır, veriyi aktarırız."* (Sıfır downtime gerekçesini kavrayamama).
- **Yanlış Yaklaşım B:** *"Doğruluğu ölçmek için birleştirilmiş unit testler yeterlidir."* (Üretim trafiğindeki canlı veri varyasyonunu diferansiyel testle doğrulama gereksinimini kaçırma).

## 3. Otomatik Değerlendirme & Parite Toleransı kurgusu
Öğrencinin mimari yanıtı, semantik bir embedding modeli (Oracle) tarafından referans çözümle karşılaştırılır. Doğrulama farkı < 1e-3 eşiğinde kalan yanıtlar kavramsal olarak "Tam Başarılı" kabul edilir.
