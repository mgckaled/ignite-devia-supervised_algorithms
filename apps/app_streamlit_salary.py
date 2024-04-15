"""
importar módulos
"""

import json

import requests
import streamlit as st

# Titulo da aplicação
st.title("Modelo de Predição de Salário")

# Inputs do Usuário
st.write("Quantos meses o profissional está empregado")
tempo_na_empresa = st.slider(
    "Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Quantos meses o profissional está empregado")
nivel_na_empresa = st.slider(
    "Nível", min_value=1, max_value=10, value=5, step=1)

# preparar dados para a API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# criar um botão e capiturarum evento deste botão para disparar a API
if st.button("Estimar Salário"):
    # requisitar api e ajustar formatação json
    res = requests.post(url="http://127.0.0.1:8000/predict",
                        data=json.dumps(input_features), timeout=2000)

    # converter retorno
    res_json = json.loads(res.text)

    # arrendodar valor
    salario_em_reais = round(res_json["salario_em_reais"], 2)

    # mostar salário
    st.subheader(f'O salário estimado é de R$ {salario_em_reais}')
