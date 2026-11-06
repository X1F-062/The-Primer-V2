# The Primer v2 — Uyumlanan Yapay Zekâ Eğitmeni

Bu proje, oyuncunun davranış metriklerine göre dynamic hint/scaffolding sunan dikey bir makine öğrenmesi modeli entegrasyonudur.

## 🚀 Hızlı Başlangıç (3 Komutta Kurulum ve Test)

```bash
# 1. Bağımlılıkları Yükleyin
pip install pandas numpy scikit-learn

# 2. Modeli Eğitin ve Eval Kapısından Geçirin
python train.py

# 3. Diferansiyel Parite Testini Çalıştırın
python tests/parite.py
```

---

## 🤖 AI Agent Kullanım Beyanı

- **Kullanılan Araçlar:** Cursor / Claude 3.5 Sonnet & Antigravity AI Agent.
- **Adımlar ve Elle Yapılan Düzeltmeler:**
  1. `train.py` içindeki rastgele tohum üretimi agent tarafından oluşturuldu; kabul eşikleri (`spec.md`) elle entegre edildi.
  2. ONNX diferansiyel parite hassasiyeti 1e-4 sınır değerleri kontrol edildi ve manuel olarak test edildi.
  3. Mimari Ödünleşim Matrisi (`RELEASE.md`) dersteki 3 temel soruya yanıt verecek şekilde elle düzenlendi.

---

## 📚 Kaynakça

1. Sommerville, *Software Engineering* (10th ed.), Ch. 8, 17, 18, 25.
2. Amershi et al. (2019), *Software Engineering for Machine Learning: A Case Study*.
3. Shankar et al. (2022), *Operationalizing Machine Learning: An Interview Study* (3V Framework).
4. Mitchell et al. (2019), *Model Cards for Model Reporting*.
5. Breck et al. (2017), *The ML Test Score: A Rubric for ML Production Readiness*.
6. Stanford HAI (2025), *AI Index Report*.
7. Gartner (2025), *Small Task-Specific Models Forecast*.
