<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD014 -->

# Ignite Trilha Desenvovimento de IA - Algoritmos Supervisionados

<div align="center">
   <img alt="logo trilha" src=".github/assets/trilha-rs.png" width="30%"/>
</div>

<br>

<div align="center">
  <img alt="Made by mgckaled" src="https://img.shields.io/badge/made%20by-mgckaled-darkblue">
  <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/mgckaled/ignite-devia-supervised_algorithms">
  <img alt="pylint badge" src="https://img.shields.io/badge/linting-pylint-yellowgreen">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</div>

## Sumário

- [Ignite Trilha Desenvovimento de IA - Algoritmos Supervisionados](#ignite-trilha-desenvovimento-de-ia---algoritmos-supervisionados)
  - [Sumário](#sumário)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Módulo 7 - Regressão Linear Simples](#módulo-7---regressão-linear-simples)
    - [Módulo 8 - Regressão Linear Múltipla](#módulo-8---regressão-linear-múltipla)
    - [Módulo 9 - Regressão Polinomial](#módulo-9---regressão-polinomial)
    - [Módulo 10 - Classificação Árvore de Decisão](#módulo-10---classificação-árvore-de-decisão)
    - [Módulo 11 - Classificação de Naive Bayes](#módulo-11---classificação-de-naive-bayes)
    - [Módulo 12 - Regressão Logística](#módulo-12---regressão-logística)
    - [Módulo 13 - Tópicos Complememtares](#módulo-13---tópicos-complememtares)
  - [Tecnologias](#tecnologias)
    - [Linguagem de Programação](#linguagem-de-programação)
    - [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual)
    - [Bibliotecas Instaladas (Packages)](#bibliotecas-instaladas-packages)
  - [Como clonar o projeto?](#como-clonar-o-projeto)
  - [Licença](#licença)

## Sobre o Projeto

Repositório que reuni os módulos 7 ao 13 da trilha Desenvolvimento IA 2023-2024, desenvolvido pela Rocketseat Education.

> Acessar [**anotações de aulas**](/.github/docs/notes.md)

### Módulo 7 - Regressão Linear Simples

Este módulo é o primeiro de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Linear Simples. Neste segmento do curso, nosso principal objetivo é fornecer uma compreensão aprofundada dos fundamentos dos algoritmos de regressão, essenciais para a construção de projetos eficazes de machine learning voltados para a previsão de valores. Como ponto de partida, mergulharemos no universo da Regressão Linear Simples. Através de um projeto prático, abordaremos cada etapa do processo, desde a Análise Exploratória de Dados (EDA) até a implementação final do modelo em uma API, facilitando sua integração e utilização em diversas aplicações. Este módulo é projetado para guiá-los através dos conceitos e práticas essenciais, preparando-os para aplicar essas habilidades em cenários reais de machine learning.

```shell
# rodar servidor com api do modelo de predição - regressão linear simples
$ cd api

$ uvicorn api_model_lr_simple:app --reload
```

**Acesso ao servidor uvicorn: `http://127.0.0.1:8000/docs` (localhost)**

### Módulo 8 - Regressão Linear Múltipla

Este módulo é o segundo de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Linear Múltipla. O obejetivo deste é apresentar o conceito de **regressão linear múltipla**, onde também iremos desenvolver um modelo através de um processo completo desde o EDA até a entrega do modelo através de uma UI para uso do usuário final. Será desenvolvido um modelo para um laboratório de análises clínicas que realiza testes de colesterol. O objetivo é avaliar se características dos pacientes, como idade, nível de atividade física e peso, podem influenciar nos resultados do exame de colesterol total. Vamos utilizar um algoritmo de regressão linear múltipla para prever o resultado do exame com base nessas características. O processo será semelhante ao que fizemos no módulo anterior de regressão linear simples, incluindo carregar os dados, realizar uma análise exploratória, preparar o dataset, treinar o modelo, validar o modelo e salvar para uso futuro.

> Para rodar a interface do modelo de previsão numa porta do localhost, execute todas células no notebook `app_gradio_colesterol.ipynb`. Para fechar a porta, execute `demo.close()`.

### Módulo 9 - Regressão Polinomial

Este módulo é o terceiro de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Polinomial. O objetivo deste módulo é apresentar o conceito de **polinómios** e **regresão polinomial**, onde também iremos desenvolver um modelo através de processo completo desde o EDA até a entrega do modelo por App com acesso para os usuários finais. Também trabalharemos o conceito de **validação cruzada**, além de definir o melhor modelo através do monitoramento do sobreajuste (*overfitting*).

```shell
# rodar servidor com api do modelo de predição - regressão polinomial
$ cd api

$ uvicorn api_model_salary:app --reload
```

seguido de:

```shell
# rodar front-end streamlit com o modelo de predição de salário
$ cd apps

$ streamlit run app_streamlit_salary.py
```

**Acesso ao servidor uvicorn: `http://127.0.0.1:8000/docs` (localhost)**

**Acesso ao front-end streamlit: `http://127.0.0.1:8501/` (localhost)**

### Módulo 10 - Classificação Árvore de Decisão

O objetivo deste módulo foi apresentar conceitualmente os principais algoritmos de classificação para desenvolver projetos de *machine learning* que fazem **previsões de categorias de classes**. Também foi feito um projeto explorando o primeiro destes algoritmos, que é o **árvore de decisão**, onde o processo completado, desde o EDA até a entrega do modelo, através de uma aplicação de inferência de *batch*.

**Porta de acesso ao app no servidor Gradio: `http://127.0.0.1:7860` (localhost)**

**Parar servidor:**

```python
def stop_gradio():
    demo.close()
    print("Servidor Gradio foi interrompido.")

stop_gradio()
```

### Módulo 11 - Classificação de Naive Bayes

Neste módulo, foi explorado o algoritmo de classificação Naive Bayes, que é baseado no Teorema de Bayes. Vamos aprender sobre a importância de Bayes na estatística e como seu trabalho foi publicado por Richard Price. Vamos realizar um projeto prático, onde faremos análise exploratória automatizada e utilizaremos hiperparâmetros. Além disso, aprendemos a automatizar a seleção de *features*, para identificar as mais relevantes para nosso modelo. Isso é importante para termos um modelo eficiente e não sobrecarregado com variáveis desnecessárias.

**Acesso a API do modelo via instância servidor Flask:** execute no terminal os comandos `cd api` e `python api_model_obesity.py`. Em seguida, utilize o molde json abaixo (`requests/request_example.json`) no *body* da requisição POST via REST API de sua preferência:

```json
{
  "Genero_Masculino": 1,
  "Idade": 48,
  "Historico_Familiar_Sobrepeso": 1,
  "Consumo_Alta_Caloria_Com_Frequencia": 1,
  "Consumo_Vegetais_Com_Frequencia": 0,
  "Refeicoes_Dia": 2,
  "Consumo_Alimentos_entre_Refeicoes": 0,
  "Fumante": 0,
  "Consumo_Agua": 2,
  "Monitora_Calorias_Ingeridas": 0,
  "Nivel_Atividade_Fisica": 0,
  "Nivel_Uso_Tela": 2,
  "Consumo_Alcool": 1,
  "Transporte_Automovel": 1,
  "Transporte_Bicicleta": 0,
  "Transporte_Motocicleta": 0,
  "Transporte_Publico": 0,
  "Transporte_Caminhada": 0
}
```

### Módulo 12 - Regressão Logística

Este módulo tem como propósito fornece uma compreensão abrangente do algoritmo de Regressão Logística, uma técnica essencial em problemas de classificação binária e multiclasse. Além de discutir os fundamentos teóricos, aplicou-se o algoritmo em cenários reais, desde a exploração e análise dos dados (EDA) até a otimização dos hiper parâmetros do modelo.

**Acesso ao servidor Uvicorn:** dentro da pasta `/apps/m12` execute o comando `uvicorn main:app --host 0.0.0.0 --port 80 --reload`

**Requisição API REST Client:** envie uma requisição POST no URL `http://localhost:80/classify` com o molde json abaixo:

```json
{
    "A_id": 4,
    "Size": 1.36421682,
    "Weight": -1.296611877,
    "Sweetness": -0.384658206,
    "Crunchiness": -0.55300577,
    "Juiciness": 3.030874354,
    "Ripeness": -1.303849429,
    "Acidity": 0.501984036
}
```

### Módulo 13 - Tópicos Complememtares

Neste módulo, vamos explorar técnicas que podem ser incorporadas nos algoritmos supervisionados para torná-los mais robustos. Essas técnicas têm várias finalidades, como mitigar o overfitting, aprimorar a seleção de features, identificar relações entre variáveis e obter uma interpretação mais profunda dos modelos. Com essas técnicas, vocês poderão melhorar significativamente o desempenho e a eficácia dos seus modelos, além de obter insights valiosos dos dados analisados.

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.11.3)

### Gerenciadores de Ambiente Virtual

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)

### Bibliotecas Instaladas (Packages)

- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`scipy`](https://scipy.org/)
- [`scikit-learn`](https://scikit-learn.org/stable/)
- [`statsmodels`](https://www.statsmodels.org/stable/index.html)
- [`fastapi`](https://fastapi.tiangolo.com/)
- [`uvicorn`](https://www.uvicorn.org/)
- [`pydantic`](https://docs.pydantic.dev/latest/)
- [`pingouin`](https://pingouin-stats.org/build/html/index.html)
- [`gradio`](https://www.gradio.app/)
- [`streamlit`](https://streamlit.io/)
- [`requests`](https://requests.readthedocs.io/en/latest/)
- [`pylint`](https://pylint.pycqa.org/en/latest/index.html) - `dev`
- [`nbqa`](https://pylint.pycqa.org/en/latest/index.html) - `dev`
- [`ipykernel`](https://pypi.org/project/ipykernel/)
- [`plotly`](https://plotly.com/python/)
- [`nbformat`](https://pypi.org/project/nbformat/)
- [`optuna`](https://optuna.org/)
- [`ipywidgets`](https://pypi.org/project/ipywidgets/)
- [`sweetviz`](https://pypi.org/project/sweetviz/)
- [`flask`](https://flask.palletsprojects.com/en/3.0.x/)
- [`flask-pydantic`](https://pypi.org/project/Flask-Pydantic/)
- [`pyarrow`](https://arrow.apache.org/docs/python/index.html)

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    git clone https://github.com/mgckaled/ignite-devia-supervised_algorithms.git
    ```

3. Acesse o diretório:

    ```shell
    cd ignite-devia-supervised_algorithms
    ```

4. Ative o ambiente virtual pelo terminal

    ```shell
    pipenv shell
    ```

5. Instale as dependências. (Certifique-se de estar utilzando a versão exata do python - 3.11.3)

    ```shell
    pipenv install
    ```

    ou, como um recurso de degurança, instale dependências exatas do `requirements.txt`:

    ```shell
    pipenv install -r requirements.txt
    ```


## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2023-2024 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>
