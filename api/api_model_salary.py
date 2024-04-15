"""Criar API com modelo de predição
"""

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# criar uma instância do FastAPI
app = FastAPI()


class RequestBody(BaseModel):
    """Criar uma classe que irá agregar todos os request body para a API
    """

    tempo_na_empresa: int
    nivel_na_empresa: int


# Carregar o modelo para realizar a predição
modelo_poly = joblib.load("../data/model_pr.plk")


@app.post("/predict")
def predict(data: RequestBody):
    """Preparar dados para realização da predição

    Args:
        data (RequestBody):
    """
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[0])

    # realizar a predição
    y_pred = modelo_poly.predict(pred_df)[0].astype(float)

    return {"salario_em_reais": y_pred.tolist()}
