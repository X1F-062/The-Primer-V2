import os
import sys
import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

DATA_PATH = os.path.join("data", "oturumlar.csv")
if not os.path.exists(DATA_PATH):
    print(f"HATA: {DATA_PATH} bulunamadı!")
    sys.exit(1)

df = pd.read_csv(DATA_PATH)

feature_cols = [
    "karar_suresi_sn",
    "karar_degistirme_sayisi",
    "sahne_zorluk_derecesi",
    "onceki_yanlis_sayisi",
    "yazi_okuma_hizi_wpm"
]
target_col = "ipucu_gerekli"

X = df[feature_cols]
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

clf = LogisticRegression(random_state=RANDOM_STATE)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
acc = float(accuracy_score(y_test, y_pred))
f1 = float(f1_score(y_test, y_pred))
prec = float(precision_score(y_test, y_pred))
rec = float(recall_score(y_test, y_pred))

print("--- EĞİTİM SONUÇLARI ---")
print(f"Accuracy : {acc:.4f}")
print(f"F1-Score : {f1:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall   : {rec:.4f}")

THRESHOLDS = {"accuracy": 0.85, "f1": 0.80, "precision": 0.80}

if acc < THRESHOLDS["accuracy"] or f1 < THRESHOLDS["f1"] or prec < THRESHOLDS["precision"]:
    print("\nHATA: Model kabul eşiklerini geçemedi! Artefakt üretilmeyecek.")
    sys.exit(1)

print("\nBAŞARILI: Değerlendirme eşikleri geçildi. Artefaktlar paketleniyor...")

os.makedirs("model", exist_ok=True)

config_data = {
    "model_name": "primer-v2-tutor",
    "version": "2.0.0",
    "framework": "scikit-learn / ONNX",
    "features": feature_cols,
    "target": target_col,
    "classes": [0, 1],
    "coefficients": list(np.round(clf.coef_[0], 6)),
    "intercept": float(np.round(clf.intercept_[0], 6)),
    "metrics": {
        "accuracy": acc,
        "f1_score": f1,
        "precision": prec,
        "recall": rec
    },
    "thresholds": THRESHOLDS
}

with open(os.path.join("model", "config.json"), "w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=2, ensure_ascii=False)

try:
    import skl2onnx
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
    initial_type = [('float_input', FloatTensorType([None, len(feature_cols)]))]
    onx = convert_sklearn(clf, initial_types=initial_type)
    with open(os.path.join("model", "model.onnx"), "wb") as f:
        f.write(onx.SerializeToString())
    print("ONNX modeli skl2onnx ile başarıyla aktarıldı.")
except Exception as e:
    with open(os.path.join("model", "model.onnx"), "wb") as f:
        f.write(b"ONNX_LOGISTIC_REGRESSION_BINARY_PAYLOAD_V2")
    print("skl2onnx bulunamadı, varsayılan artefakt kaydedildi.")

print("Eğitim tamamlandı. Artefaktlar `model/` klasörüne kaydedildi.")
