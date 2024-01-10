"""Aprendemos como interagir com a API que construímos anteriormente. Ao acessar o endereço "localhost:8000/docs", podemos ver a documentação da API gerada automaticamente pelo FastAPI. No entanto, percebemos que não definimos as operações da API, como POST ou GET, nem a URL para acessá-la. Para corrigir isso, precisamos adicionar um decorador em nosso código para indicar que o método "predict" será exposto como uma rota na API. Após fazer essa alteração e salvar o código, o servidor faz um reload automático e a documentação da API é atualizada. Agora podemos testar a API diretamente no Swagger, fornecendo os dados de entrada necessários e obtendo as respostas correspondentes. Com isso, concluímos este módulo, onde aprendemos a disponibilizar nosso modelo de Machine Learning como uma API e a interagir com ela usando o Swagger.
"""

import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Criar uma instância do FastAPI
app = FastAPI()


# Criar uma classe que irá agregar todos os request body para a API
class request_body(BaseModel):
    horas_estudo: float


# Carregar o modelo para realizar o modelo de predição
modelo_pontuacao = joblib.load("../data/model_lr_simple.plk")


@app.post("/predict")
def predict(data: request_body):
    # preparar dados
    input_feature = [[data.horas_estudo]]

    # realizar a predição
    Y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

    return {"pontuacao_teste": Y_pred.tolist()}
