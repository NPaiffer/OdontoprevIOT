
# 💳 ODONTOPREV: Detecção de Fraudes em Transações Móveis

### Repositório: https://github.com/NPaiffer/OdontoprevIOT

### Dataset: `PS_20174392719_1491204439457_log.csv`  
**Dataset:** Este dataset foi **criado por nossa equipe** com base em padrões de transações móveis, simulando operações legítimas e fraudulentas para fins acadêmicos.

---

## Visão Geral do Projeto

Este projeto foi desenvolvido com o objetivo de criar um sistema de detecção de fraudes em transações financeiras móveis, com foco educacional e prototipação funcional. A solução é composta por:

- Um modelo de Machine Learning treinado em um dataset simulado.
- Um dashboard interativo com **Streamlit** para análise e detecção de transações suspeitas.

---

## Etapas do Desenvolvimento

### 1. **Criação e Preparação dos Dados**
- Elaboramos um dataset customizado inspirado em cenários reais de fraudes financeiras.
- Os dados foram estruturados com atributos como:
  - `type` (tipo de transação)
  - `amount` (valor)
  - `oldbalanceOrg`, `newbalanceOrig` (saldo do remetente)
  - `oldbalanceDest`, `newbalanceDest` (saldo do destinatário)
  - `isFraud` (rótulo de fraude)

### 2. **Treinamento do Modelo**
- Utilizamos **Random Forest**, um algoritmo supervisionado eficaz em classificações com dados tabulares.
- O modelo foi salvo como `modelo_fraude.pkl` com a biblioteca `joblib` para posterior uso no dashboard.

### 3. **Desenvolvimento do Dashboard**
- Criamos uma interface interativa com **Streamlit**, onde usuários podem:
  - Informar os dados da transação manualmente.
  - Obter uma previsão se a transação é fraudulenta ou não.
  - Ver a **probabilidade da predição** em tempo real.
  - Visualizar gráficos sobre o desempenho do modelo.

---

## Por que fizemos o Dashboard?

Implementar o dashboard foi uma decisão estratégica para:
- Demonstrar a aplicação prática do modelo em um ambiente simulado.
- Tornar o uso da IA acessível para pessoas sem conhecimento técnico.
- Criar uma interface que simula um sistema real de verificação de transações em empresas como bancos ou operadoras financeiras.

---

## Funcionalidades da Interface

- Formulário de entrada com tipo de transação e saldos.
- Verificação em tempo real da transação.
- Indicador de fraude com nível de confiança.
- Gráficos que demonstram:
  - Métricas do modelo.
  - Distribuição de transações legítimas e fraudulentas.

---

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/OdontoprevIOT.git
   cd odontoprev-fraudes
   ```

2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv

   pip install -r requirements.txt
   ```

3. **Execute o dashboard:**
   ```bash
   streamlit run dashboard/app.py
   ```

---

## Reflexões e Aprendizados

### O que funcionou bem:
- O modelo Random Forest apresentou ótima performance para o nosso caso.
- A criação do dashboard trouxe clareza para a aplicação real da IA.
- Integração entre modelo e interface foi eficiente e direta.

### Desafios enfrentados:
- Inicialmente enfrentamos erros com caminhos de arquivos e bibliotecas ausentes.
- Foi necessário ajustar o formato do dataset para ser compatível com o modelo.

### O que faríamos diferente:
- Incluiríamos mais cenários no dataset para testes avançados.
- Trabalharíamos em validação cruzada e ajustes finos nos hiperparâmetros do modelo.

---

## Próximos Passos

- Salvar o histórico de transações analisadas no dashboard.
- Implementar login e segurança básica para simular uso corporativo.
- Treinar modelos alternativos para comparação, como XGBoost.
- Disponibilizar o sistema em nuvem (ex: Streamlit Cloud ou Azure App Service).

---

## Integrantes

- Alissa – RM553954  
- Melissa – RM552535  
- Nicolas – RM554145
