import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Criar instância do FastAPI
app = FastAPI()

# classe com os dados do request


class request_body(BaseModel):
    A_id: int
    Size: float
    Weight: float
    Sweetness: float
    Crunchiness: float
    Juiciness: float
    Ripeness: float
    Acidity: float
    Quality: float


# carregar modelo para realizar a classificação
model_logr_quality_fruits = joblib.load(
    '../../data/model_logr_fruits_quality.plk')


@app.post('/classify')
def predict(data: request_body):

    # preparar features
    input_features = [[data.Size, data.Weight,
                       data.Sweetness, data.Crunchiness, data.Juiciness, data.Ripeness, data.Acidity]]

    # classificar fruta
    y_pred = model_logr_quality_fruits.predict(input_features)[0].astype(int)
    y_prob = model_logr_quality_fruits.predict_proba(input_features)[
        0].astype(float)

    result = "Boa" if y_pred == 1 else "Ruim"
    probability = y_prob[y_pred]

    return {'qualidade': result, 'probabilidade': probability}
