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
  - [Tecnologias](#tecnologias)
    - [Linguagem de Programação](#linguagem-de-programação)
    - [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual)
    - [Bibliotecas Instaladas (Packages)](#bibliotecas-instaladas-packages)
  - [Como clonar o projeto?](#como-clonar-o-projeto)
  - [Licença](#licença)

## Sobre o Projeto

Repositório que reuni os módulos 7, 8 e 9 da trilha Desenvolvimento IA 2023, desenvolvido pela Rocketseat Education.

> Acessar [**anotações de aulas**](/.github/docs/notes.md)

### Módulo 7 - Regressão Linear Simples

Este módulo é o primeiro de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Linear Simples. Neste segmento do curso, nosso principal objetivo é fornecer uma compreensão aprofundada dos fundamentos dos algoritmos de regressão, essenciais para a construção de projetos eficazes de machine learning voltados para a previsão de valores. Como ponto de partida, mergulharemos no universo da Regressão Linear Simples. Através de um projeto prático, abordaremos cada etapa do processo, desde a Análise Exploratória de Dados (EDA) até a implementação final do modelo em uma API, facilitando sua integração e utilização em diversas aplicações. Este módulo é projetado para guiá-los através dos conceitos e práticas essenciais, preparando-os para aplicar essas habilidades em cenários reais de machine learning.

```shell
# rodar servidor com api do modelo de predição - regressão linear simples
$ cd api

$ uvicorn api_model_lr_simple:app --reload
```

Acesso ao servidor: `http://127.0.0.1:8000/docs`

### Módulo 8 - Regressão Linear Múltipla

Este módulo é o segundo de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Linear Múltipla. O obejetivo deste é apresentar o conceito de **regressão linear múltipla**, onde também iremos desenvolver um modelo através de um processo completo desde o EDA até a entrega do modelo através de uma UI para uso do usuário final. Será desenvolvido um modelo para um laboratório de análises clínicas que realiza testes de colesterol. O objetivo é avaliar se características dos pacientes, como idade, nível de atividade física e peso, podem influenciar nos resultados do exame de colesterol total. Vamos utilizar um algoritmo de regressão linear múltipla para prever o resultado do exame com base nessas características. O processo será semelhante ao que fizemos no módulo anterior de regressão linear simples, incluindo carregar os dados, realizar uma análise exploratória, preparar o dataset, treinar o modelo, validar o modelo e salvar para uso futuro.

> Para rodar a interface do modelo de previsão numa porta do localhost, execute todas células no notebook `app_gradio_colesterol.ipynb`. Para fechar a porta, execute `demo.close()`.

### Módulo 9 - Regressão Polinomial

Este módulo é o terceiro de uma série para estudo dos algoritmos supervisionados, com foco especial na Regressão Polinomial. O objetivo deste módulo é apresentar o conceito de **polinómios** e **regresão polinomial**, onde também iremos desenvolver um modelo através de processo completo desde o EDA até a entrega do modelo por App com acesso para os usuários finais. Também trabalharemos o conceito de **validação cruzada**, além de definir o melhor modelo através do monitoramento do sobreajuste (*overfitting*).

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
- [`pylint`](https://pylint.pycqa.org/en/latest/index.html)
- [`nbqa`](https://pylint.pycqa.org/en/latest/index.html)

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    $ git clone https://github.com/mgckaled/ignite-devia-supervised_algorithms.git
    ```

3. Acesse o diretório:

    ```shell
    $ cd ignite-devia-supervised_algorithms
    ```

4. Instale as dependências e ative o ambiente virtual

    ```shell
    $ pipenv install
    $ pipenv shell
    ```

## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2023 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>
