# Data Sözlüğü — Primer v2 Oturum Verisi

## Gizlilik ve KVKK Beyanı
Bu veri setinde isim, e-posta, IP adresi, cihaz seri numarası gibi hiçbir Kişisel Veri (PII) toplanmamıştır. Oturum kimlikleri `sess_` ön ekiyle rastgele türetilmiştir.

## Veri Şeması

| Sütun Adı | Veri Tipi | Birim / Format | Açıklama |
| :--- | :--- | :--- | :--- |
| `oturum_id` | String | Format: `sess_xxx` | Rastgele oluşturulmuş oturum tekil anahtarı |
| `karar_suresi_sn` | Float | Saniye (sn) | Oyuncunun mevcut sahnede karara varmak için harcadığı süre |
| `karar_degistirme_sayisi` | Integer | Adet | Seçeneği onaylamadan önce yapılan seçim değişiklik sayısı |
| `sahne_zorluk_derecesi` | Integer | 1 (Kolay) - 5 (Zor) | Mevcut anlatı/kod sahnesinin zorluk puanı |
| `onceki_yanlis_sayisi` | Integer | Adet | Oyuncunun önceki sahnelerdeki toplam hatalı seçimi |
| `yazi_okuma_hizi_wpm` | Float | Kelime/Dakika (WPM) | Oyuncunun tahmini okuma hızı (Metin boyutu / İlk tereddüt) |
| `ipucu_gerekli` | Integer | 0 (Hayır) \| 1 (Evet) | Hedef Değişken (Ground Truth Label) |
| `kaynak` | Enum | `gercek` \| `sentetik` | Verinin gerçek kullanıcıdan mı sentetik kuraldan mı üretildiği |
