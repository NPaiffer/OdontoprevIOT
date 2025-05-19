import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

st.title("🔍 Detecção de Fraudes - OdontoPrev IOT")

# Carregar dados e modelo
df = pd.read_csv("../PS_20174392719_1491204439457_log.csv")
model = joblib.load("../modelo_fraude.pkl")

# Limpar e preparar os dados para visualização
df['type'] = df['type'].astype(str)
df_viz = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])].copy()
df_viz['type'] = df_viz['type'].map({'TRANSFER': 1, 'CASH_OUT': 0})

# Visualizações
st.subheader("📊 Gráficos de Análise")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='type', ax=ax1)
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    corr = df_viz[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud']].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

# Previsão em tempo real
st.subheader("🔮 Previsão em Tempo Real")

with st.form("formulario_predicao"):
    tipo_transacao = st.selectbox("Tipo de Transação", ['TRANSFER', 'CASH_OUT'])
    valor = st.number_input("Valor da Transação", min_value=0.0)
    saldo_antigo = st.number_input("Saldo Antes da Transação", min_value=0.0)
    saldo_novo = st.number_input("Saldo Após a Transação", min_value=0.0)
    saldo_destino_ant = st.number_input("Saldo do Destinatário Antes", min_value=0.0)
    saldo_destino_novo = st.number_input("Saldo do Destinatário Após", min_value=0.0)

    submit = st.form_submit_button("Verificar Fraude")

    if submit:
        tipo_cod = 0 if tipo_transacao == "CASH_OUT" else 1
        entrada = [[
            tipo_cod,
            valor,
            saldo_antigo,
            saldo_novo,
            saldo_destino_ant,
            saldo_destino_novo
        ]]

        predicao = model.predict(entrada)[0]
        prob = model.predict_proba(entrada)[0][1]

        if predicao == 1:
            st.error(f"🚨 FRAUDE DETECTADA com {prob:.2%} de confiança!")
        else:
            st.success(f"✅ Transação segura com {1 - prob:.2%} de confiança.")

