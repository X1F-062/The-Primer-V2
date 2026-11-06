from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI(title="Primer v2 Bonus API")

COEFFICIENTS = [0.276952, 0.959844, 0.377549, 1.349349, -0.026172]
INTERCEPT = 1.316601

class ParityInput(BaseModel):
    karar_suresi_sn: float
    karar_degistirme_sayisi: int
    sahne_zorluk_derecesi: int
    onceki_yanlis_sayisi: int
    yazi_okuma_hizi_wpm: float

@app.post("/predict")
def predict(data: ParityInput):
    x = [
        data.karar_suresi_sn,
        data.karar_degistirme_sayisi,
        data.sahne_zorluk_derecesi,
        data.onceki_yanlis_sayisi,
        data.yazi_okuma_hizi_wpm
    ]
    z = sum(w * val for w, val in zip(COEFFICIENTS, x)) + INTERCEPT
    prob = 1.0 / (1.0 + math.exp(-z))
    pred_class = 1 if prob >= 0.5 else 0
    
    return {
        "ipucu_gerekli": pred_class,
        "olasilik": round(prob, 6),
        "status": "success"
    }
