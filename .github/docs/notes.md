# Anotações

> [voltar](../../README.md) para a página anterior

## Sumário

- [Anotações](#anotações)
  - [Sumário](#sumário)
  - [Conteúdo](#conteúdo)
    - [Módulo 7 - Regressão Linear Simples](#módulo-7---regressão-linear-simples)
    - [Módulo 8 - Regressão Linear Múltipla](#módulo-8---regressão-linear-múltipla)
    - [Módulo 9 - Regressão Polinomial](#módulo-9---regressão-polinomial)
  - [O que é Análise de Regressão?](#o-que-é-análise-de-regressão)
    - [Tipos de Regressão](#tipos-de-regressão)
      - [Linear Simples](#linear-simples)
      - [Linear Múltipla](#linear-múltipla)
      - [Logística](#logística)
      - [Polinomial](#polinomial)
      - [Poisson](#poisson)
      - [Ridge, Lasso e ElasticNet](#ridge-lasso-e-elasticnet)
      - [*Gamma*](#gamma)
      - [*Beta*](#beta)

## Conteúdo

### Módulo 7 - [Regressão Linear Simples](./m7.md)

### Módulo 8 - [Regressão Linear Múltipla](./m8.md)

### Módulo 9 - [Regressão Polinomial](./m9.md)

## O que é Análise de Regressão?

A análise de regressão é uma abordagem estatística que busca investigar e quantificar as relações entre variáveis. Ela é usada para entender como uma variável dependente (target) está relacionada a uma ou mais variáveis independentes (fatores que acreditamos influenciar a variável dependente).

Essa técnica permite construir um modelo matemático, geralmente na forma de uma equação linear, que representa essa relação. Ao ajustar o modelo aos dados observados, podemos estimar os parâmetros e entender como as mudanças nas variáveis independentes afetam a variável dependente.

Isso é fundamental para fazer previsões, tomar decisões embasadas em evidências e compreender melhor os padrões em dados do mundo real.

### Tipos de Regressão

#### Linear Simples

**Conceito Simples:** Envolve uma variável independente e uma variável dependente, sendo representada por uma linha reta. Exemplo: Prever pontuação num exame com base no tempo de estudo.

A regressão linear é uma técnica estatística que busca modelar a relação linear entre uma variável dependente (ou resposta) e uma ou mais variáveis independentes (ou preditoras). O objetivo é encontrar a equação de uma linha reta que melhor se ajusta aos dados observados. Essa linha pode ser usada para fazer previsões ou entender a relação entre as variáveis.

A equação geral da regressão linear simples pode ser expressa como:

`Y = β₀ + β₁ * X + ε`

onde:

- Y é a variável dependente.
- X é a variável independente.
- β₀ é o intercepto (valor de Y quando X é zero).
- β₁ é o coeficiente de inclinação (representa a mudança média em Y para uma unidade de mudança em X).
- ε é o erro, que representa as variações não explicadas pelo modelo.

Se houver mais de uma variável independente, temos uma regressão linear múltipla, e a equação geral é expandida para incluir os coeficientes correspondentes a cada variável independente.

O processo de ajustar a linha de regressão envolve minimizar a soma dos quadrados dos resíduos (ε), que são as diferenças entre os valores observados e os valores previstos pela linha de regressão. Isso é geralmente feito usando o método dos mínimos quadrados.

A interpretação dos coeficientes (β₀ e β₁) é fundamental para entender o relacionamento entre as variáveis. O coeficiente de inclinação (β₁) indica a mudança média na variável dependente para uma unidade de mudança na variável independente, mantendo as outras variáveis constantes.

> [retornar](#anotações) ao topo da página

#### Linear Múltipla

**Conceito Simples:** Utiliza várias variáveis independentes para prever uma variável dependente, resultando em um modelo linear mais complexo.Exemplo: Prever desempenho de alunos com base em múltiplas variáveis

A regressão linear múltipla é uma extensão da regressão linear simples e é utilizada quando há mais de uma variável independente para prever uma variável dependente. A equação geral da regressão linear múltipla pode ser expressa como:

`Y = β₀ + β₁ *X₁ + β₂* X₂ + ... + βₖ * Xₖ + ε`

onde:

- Y é a variável dependente.
- X₁, X₂, ..., Xₖ são as variáveis independentes.
- β₀ é o intercepto (o valor de Y quando todas as variáveis independentes são zero).
- β₁, β₂, ..., βₖ são os coeficientes de inclinação que representam as mudanças médias em Y para uma unidade de mudança nas variáveis independentes correspondentes.
- ε é o erro, que representa as variações não explicadas pelo modelo.

O processo de ajustar a linha de regressão múltipla envolve encontrar os coeficientes (β₀, β₁, β₂, ..., βₖ) que minimizam a soma dos quadrados dos resíduos, semelhante à regressão linear simples.

A interpretação dos coeficientes é crucial. Por exemplo, o coeficiente β₁ indica a mudança média em Y para uma unidade de mudança em X₁, mantendo as outras variáveis constantes.

A regressão linear múltipla é útil quando há interações complexas entre várias variáveis independentes e a variável dependente. No entanto, assim como na regressão linear simples, é importante verificar as suposições do modelo, como a linearidade da relação e a normalidade dos resíduos.

Essa técnica é amplamente empregada em análises estatísticas e preditivas, permitindo modelar de maneira mais sofisticada e realista as relações entre variáveis em conjuntos de dados complexos.

> [retornar](#anotações) ao topo da página

#### Logística

**Conceito Simples:** Usada geralmentepara prever probabilidades em problemas de classificação (binária, multinomial, ordinal, aninhada). Exemplo: Prever se cliente fará compra online (sim/não) rocketseat

A regressão logística é uma técnica estatística usada para modelar a relação entre uma variável binária dependente (que pode assumir dois valores, geralmente 0 ou 1) e uma ou mais variáveis independentes. Ao contrário da regressão linear, a regressão logística utiliza a função logística para transformar a saída em uma escala de 0 a 1, representando a probabilidade de pertencer a uma classe.

A equação da regressão logística é dada por:

`P(Y=1) = 1 / (1 + e^-(β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ))`

onde:

- P(Y=1) é a probabilidade de Y ser igual a 1.
- e é a base do logaritmo natural.
- β₀, β₁, ..., βₖ são os coeficientes de regressão.
- X₁, X₂, ..., Xₖ são as variáveis independentes.

O logaritmo da razão de chances (log-odds) é representado por β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ. Quando essa expressão é passada pela função logística, obtemos a probabilidade.

O processo de ajustar a regressão logística envolve encontrar os coeficientes (β₀, β₁, ..., βₖ) que maximizam a verossimilhança dos dados observados.

A interpretação dos coeficientes é realizada em termos de odds ratio. Por exemplo, um aumento de uma unidade em X₁ resulta em um aumento de e^(β₁) vezes nas chances de Y=1.

A regressão logística é comumente usada em problemas de classificação binária, como prever se um e-mail é spam ou não, ou se um paciente está em risco de desenvolver uma condição médica.

Assim como em outras técnicas estatísticas, é essencial validar as suposições do modelo para garantir resultados confiáveis.

> [retornar](#anotações) ao topo da página

#### Polinomial

**Conceito Simples:** Permite modelar relações não-lineares entre variáveis. A regressão polinomial usa uma curva (um polinômio) para se ajustar aos dados. Exemplo: Previsão de vendas de produtos com base no clima/temperatura.

A regressão polinomial é uma extensão da regressão linear que permite modelar relações não lineares entre variáveis. Em vez de ajustar uma linha reta, a regressão polinomial ajusta um polinômio aos dados. A forma geral da equação de regressão polinomial de grau `n` é:

`Y = β₀ + β₁X + β₂X² + ... + βₙXⁿ + ε`

onde:

- Y é a variável dependente.
- X é a variável independente.
- β₀, β₁, ..., βₙ são os coeficientes de regressão.
- ε é o erro.

O grau `n` do polinômio determina o número de termos polinomiais na equação. Por exemplo, para um polinômio de segundo grau (`n=2`), a equação seria Y = β₀ + β₁X + β₂X² + ε.

O processo de ajuste envolve encontrar os coeficientes (β₀, β₁, ..., βₙ) que minimizam a soma dos quadrados dos resíduos, de maneira semelhante à regressão linear.

A regressão polinomial é útil quando a relação entre as variáveis não pode ser adequadamente modelada por uma linha reta. No entanto, é importante ter cuidado ao escolher o grau do polinômio, pois um grau muito alto pode levar a um sobreajuste (overfitting) aos dados de treinamento.

Essa técnica é comumente usada em problemas onde a relação entre as variáveis não é estritamente linear, como em fenômenos físicos complexos ou em padrões não lineares em conjuntos de dados.

> [retornar](#anotações) ao topo da página

#### Poisson

**Conceito Simples:** Adequada para modelar dados de contagem, como o número de eventos em um determinado período. É comum em estudos epidemiológicos e de contagem. Exemplo: Número de Reclamações de Sinistros

A regressão de Poisson é usada para modelar a relação entre variáveis independentes e uma variável dependente que representa contagens de eventos. A equação de regressão de Poisson é expressa como:

`ln(λ) = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ`

Onde:

- ln(λ) é o logaritmo natural da taxa média de ocorrência do evento.
- β₀, β₁, ..., βₖ são os coeficientes de regressão.
- X₁, X₂, ..., Xₖ são as variáveis independentes.

A interpretação dos coeficientes é feita em termos de variação percentual na taxa de ocorrência do evento para uma unidade de mudança nas variáveis independentes.

O processo de ajuste envolve encontrar os coeficientes (β₀, β₁, ..., βₖ) que maximizam a verossimilhança dos dados observados.

A regressão de Poisson é frequentemente aplicada a dados de contagem, como o número de eventos em um intervalo de tempo fixo. É importante verificar se as suposições do modelo, como a independência dos eventos e a homogeneidade da taxa, são atendidas para obter resultados confiáveis.

Essa técnica é útil quando as observações representam eventos raros e a variância é aproximadamente igual à média.

> [retornar](#anotações) ao topo da página

#### Ridge, Lasso e ElasticNet

**Conceito Simples:** Técnicas de regularização para lidar com multicolinearidade e overfitting. São usadas em análises onde há muitas variáveis independentes. Exemplo: Estimar preços de casas com base em muitas variáveis.

1. Regressão Ridge (L2 Regularização):

    A regressão Ridge é uma técnica de regularização utilizada para lidar com a multicolinearidade em modelos de regressão. Ela adiciona um termo de regularização à função de custo, o que ajuda a evitar coeficientes muito grandes. A equação de regressão Ridge é dada por:

    `Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + λ∑(βᵢ²) + ε`

    onde:

    - Y é a variável dependente.
    - X₁, X₂, ..., Xₖ são as variáveis independentes.
    - β₀, β₁, ..., βₖ são os coeficientes de regressão.
    - λ é o parâmetro de regularização (penalidade).

    O termo adicional λ∑(βᵢ²) penaliza coeficientes grandes, controlando assim o sobreajuste.

2. Regressão Lasso (L1 Regularização):
    A regressão Lasso é outra técnica de regularização que também ajuda a lidar com a multicolinearidade e tem a propriedade de realizar seleção de variáveis. A equação de regressão Lasso é dada por:

    `Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + λ∑|βᵢ| + ε`

    onde:

    - Y é a variável dependente.
    - X₁, X₂, ..., Xₖ são as variáveis independentes.
    - β₀, β₁, ..., βₖ são os coeficientes de regressão.
    - λ é o parâmetro de regularização (penalidade).

    O termo adicional λ∑|βᵢ| promove a esparsidade nos coeficientes, tornando alguns deles exatamente zero.

3. Regressão ElasticNet (Combinação de L1 e L2 Regularização):

    A regressão ElasticNet é uma combinação da regressão Ridge e da regressão Lasso, incorporando tanto termos de regularização L1 quanto L2. A equação de regressão ElasticNet é dada por:

    `Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + λ₁∑(βᵢ²) + λ₂∑|βᵢ| + ε`

    onde:

    - Y é a variável dependente.
    - X₁, X₂, ..., Xₖ são as variáveis independentes.
    - β₀, β₁, ..., βₖ são os coeficientes de regressão.
    - λ₁ e λ₂ são os parâmetros de regularização (penalidades).

    A combinação das penalidades L1 e L2 fornece um controle mais flexível sobre a seleção de variáveis e a regularização dos coeficientes.

> [retornar](#anotações) ao topo da página

#### *Gamma*

**Conceito Simples:** Usada quando os dados não seguem uma distribuição normal e exibem uma assimetria positiva (à direita). Além disso, o target é contínuo e positivo. Exemplo: Previsão de tempo de permanência de pacientes em um hospital.

A regressão gamma é usada para modelar variáveis positivas contínuas e assimétricas, muitas vezes quando a variabilidade da resposta aumenta com a média. A equação geral é expressa como:

`g(μ) = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ`

Onde:

- g() é uma função de ligação.
- μ é a média da distribuição gamma.
- X₁, X₂, ..., Xₖ são as variáveis independentes.
- β₀, β₁, ..., βₖ são os coeficientes de regressão.

A escolha da função de ligação g() depende do contexto específico. A regressão gamma é útil quando a distribuição dos dados é assimétrica e a variabilidade é heteroscedástica.

> [retornar](#anotações) ao topo da página

#### *Beta*

**Conceito Simples:** Aplicada quando a variável dependente está restrita ao intervalo [0, 1], comum em análises de proporções e taxas. Exemplo: Taxa de conversão com base numa campanha de Marketing.

A "Regressão Beta" no contexto de machine learning refere-se a modelos lineares, como a Regressão Linear, onde os coeficientes associados às variáveis preditoras são denotados como betas (β). Em uma forma geral, a equação de um modelo de regressão linear pode ser expressa como:

`Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε`

onde:

- Y é a variável dependente.
- X₁, X₂, ..., Xₖ são as variáveis independentes.
- β₀, β₁, ..., βₖ são os coeficientes de regressão associados a cada variável.
- ε é o termo de erro.

Os coeficientes β representam a contribuição de cada variável na predição da variável dependente. Um valor positivo indica uma relação positiva, enquanto um valor negativo indica uma relação negativa. A interpretação de β₁, por exemplo, seria a mudança média em Y para uma unidade de mudança em X₁, mantendo as outras variáveis constantes.

A "Regressão Beta" pode ser estendida para incluir técnicas de regularização, como a Regressão Ridge (L2) e a Regressão Lasso (L1), onde os coeficientes são regularizados para evitar overfitting e melhorar a generalização do modelo.

Essa abordagem é comum em tarefas de regressão, onde o objetivo é prever um valor contínuo com base em um conjunto de variáveis preditoras.

> [retornar](#anotações) ao topo da página
>
> [voltar](../../README.md) para a página anterior
