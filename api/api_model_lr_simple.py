"""Criar API com modelo de predição 
"""

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Criar uma instância do FastAPI
app = FastAPI()


class RequestBody(BaseModel):
    """Criar uma classe que irá agregar todos os request body para a API

    Properties:
        horas_estudo: float
    """

    horas_estudo: float


# Carregar o modelo para realizar o modelo de predição
modelo_pontuacao = joblib.load("../data/model_lr_simple.plk")


@app.post("/predict")
def predict(data: RequestBody):
    """Preparar dados para realização da predição

    Args:
        data (RequestBody):
    """
    input_feature = [[data.horas_estudo]]

    # realizar a predição
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

    return {"pontuacao_teste": y_pred.tolist()}
