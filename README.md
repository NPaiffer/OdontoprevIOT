# ODONTOPREV: Detecção de Fraudes em Transações Móveis

### Link do Dataset: https://drive.google.com/file/d/1aN1x_qj26bwym-y--4i42W5Jigb30GbO/view?usp=drive_link

## Apresentação do Protótipo Funcional e Análise da Arquitetura de IA

Este projeto visa a detecção de fraudes em transações financeiras móveis por meio de algoritmos de Machine Learning. O modelo identifica padrões anômalos e classifica transações suspeitas com base no comportamento histórico dos dados.

## Objetivos Específicos

### Demonstração do Protótipo Funcional

Atualmente, o projeto conta com as seguintes funcionalidades:

- **Carregamento e tratamento de dados** da base PaySim.
- **Treinamento de múltiplos modelos de IA** para comparação de desempenho.
- **Visualização dos resultados** por meio de matrizes de confusão e métricas de avaliação.

####  Dificuldades e Problemas Encontrados

- **Desbalanceamento de classes**: A grande maioria das transações são normais, tornando desafiador o treinamento de modelos eficazes.
- **Ajuste de hiperparâmetros**: Modelos como XGBoost e Random Forest necessitam de ajustes finos para evitar overfitting e melhorar a detecção de fraudes.
- **Latência na execução**: Alguns modelos exigem mais tempo de processamento, afetando a eficiência do sistema.

### Detalhamento da Arquitetura de IA

A arquitetura escolhida combina **modelos supervisionados e não supervisionados** para maximizar a detecção de fraudes:

- **Isolation Forest**: Detecta anomalias em transações com base em distância estatística.
- **Random Forest**: Utiliza um conjunto de árvores de decisão para melhorar a precisão.
- **XGBoost**: Otimiza a classificação utilizando boosting para lidar com desbalanceamento de classes.
- **SVM (Support Vector Machine)**: Separa transações fraudulentas e não fraudulentas com base em hiperplanos.

Os modelos são avaliados com as seguintes métricas:

- **Precisão**: Mede a proporção de previsões corretas.
- **Recall**: Indica a capacidade do modelo de identificar fraudes.
- **F1-Score**: Equilíbrio entre precisão e recall.

A implementação da IA foi realizada no **Google Colab**, garantindo execução eficiente e integração com ferramentas de análise de dados.

### Base de Dados Utilizada

A base de dados escolhida foi a **PaySim - Mobile Money Fraud**, obtida via Kaggle. Essa base simula transações financeiras em sistemas de pagamento móvel, permitindo o treinamento e teste dos modelos em um ambiente realista.

Principais atributos utilizados:

- **amount**: Valor da transação.
- **oldbalanceOrg e newbalanceOrig**: Saldo anterior e novo saldo do remetente.
- **type**: Tipo da transação (CASH\_OUT, TRANSFER, etc.).
- **isFraud**: Indica se a transação é fraudulenta.

Os dados foram pré-processados para remoção de inconsistências e padronização das variáveis.

## Evoluções Implementadas

- Implementação de **novos modelos de IA** para comparação de desempenho.
- Geração de **gráficos interativos** para análise dos resultados.
- Otimização da **eficiência computacional**, reduzindo tempo de execução dos modelos.

## Como Executar o Projeto

1. Clone o repositório:
2. Instale as dependências:
3. Execute o notebook no Google Colab:
   - Acesse [Google Colab](https://colab.research.google.com/)
   - Faça o upload do arquivo `.ipynb`
   - Rode as células do código

## Visualização dos Resultados

Os resultados foram avaliados utilizando:

- **Matrizes de Confusão** para verificar a precisão dos modelos.
- **Gráficos de Comparacão** de métricas (Precisão, Recall e F1-Score).
- **Distribuição das Fraudes no Dataset** para entender a proporção de transações fraudulentas.

## Integrantes - Alissa RM553954 | Melissa RM552535 | Nicolas RM554145

