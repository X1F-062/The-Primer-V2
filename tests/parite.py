import json
import math
import sys

COEFFICIENTS = [0.276952, 0.959844, 0.377549, 1.349349, -0.026172]
INTERCEPT = 1.316601
TOLERANCE = 1e-4

def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))

def predict_oracle(inputs):
    x = [
        inputs["karar_suresi_sn"],
        inputs["karar_degistirme_sayisi"],
        inputs["sahne_zorluk_derecesi"],
        inputs["onceki_yanlis_sayisi"],
        inputs["yazi_okuma_hizi_wpm"]
    ]
    z = sum(w * val for w, val in zip(COEFFICIENTS, x)) + INTERCEPT
    prob = sigmoid(z)
    pred_class = 1 if prob >= 0.5 else 0
    return prob, pred_class

def run_parity_tests():
    with open("tests/parite.json", "r", encoding="utf-8") as f:
        samples = json.load(f)
    
    print("=== DİFERANSİYEL PARİTE TESTİ BAŞLATILIYOR ===")
    all_passed = True
    
    for item in samples:
        sample_id = item["id"]
        girdiler = item["girdiler"]
        expected_prob = item["oracle_olasilik"]
        expected_class = item["beklenen_sinif"]
        
        calc_prob, calc_class = predict_oracle(girdiler)
        diff = abs(calc_prob - expected_prob)
        
        passed = (diff < TOLERANCE) and (calc_class == expected_class)
        if not passed:
            all_passed = False
            
        status = "PASSED" if passed else "FAILED"
        print(f"Örnek #{sample_id}: Fark = {diff:.2e} | Durum = {status}")
        
    if not all_passed:
        print("\nHATA: Diferansiyel parite testi başarısız! Hata toleransı geçildi.")
        sys.exit(1)
        
    print("\nBAŞARI: Tüm diferansiyel parite testleri 1e-4 hata toleransı içinde doğrulandı.")

if __name__ == "__main__":
    run_parity_tests()
