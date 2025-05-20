import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# Caminho absoluto para o modelo (relativo ao app.py)
modelo_path = os.path.join(os.path.dirname(__file__), "modelo_fraude.pkl")

# Verifica se o modelo existe
if not os.path.exists(modelo_path):
    st.error("Modelo não encontrado! Treine o modelo antes de iniciar o dashboard.")
    st.stop()

# Carrega o modelo
model = joblib.load(modelo_path)

# Título do app
st.title("💳 Detecção de Fraudes - OdontoPrev")

# Inicializa o histórico na sessão
if "historico" not in st.session_state:
    st.session_state.historico = []

# Formulário de entrada
with st.form("form"):
    tipo_transacao = st.selectbox("Tipo de transação", ['CASH_OUT', 'TRANSFER', 'PAYMENT', 'CASH_IN', 'DEBIT'])
    tipo_code = ['CASH_OUT', 'TRANSFER', 'PAYMENT', 'CASH_IN', 'DEBIT'].index(tipo_transacao)
    amount = st.number_input("Valor da transação", min_value=0.0, step=100.0)
    oldbalanceOrg = st.number_input("Saldo original do remetente", min_value=0.0, step=100.0)
    newbalanceOrig = st.number_input("Novo saldo do remetente", min_value=0.0, step=100.0)
    oldbalanceDest = st.number_input("Saldo original do destinatário", min_value=0.0, step=100.0)
    newbalanceDest = st.number_input("Novo saldo do destinatário", min_value=0.0, step=100.0)
    submitted = st.form_submit_button("Verificar")

# Quando o botão for clicado
if submitted:
    features = [[tipo_code, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]]
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    # Exibe o resultado
    if prediction == 1:
        st.error(f"🚨 Fraude detectada! (Confiança: {prob:.2%})")
    else:
        st.success(f"✅ Transação legítima (Confiança: {1 - prob:.2%})")

    # Exibe gráfico de barras com a probabilidade
    st.subheader("🔍 Visualização da probabilidade de fraude")

    fig, ax = plt.subplots()
    ax.barh(["Fraude", "Legítima"], [prob, 1 - prob], color=["red", "green"])
    ax.set_xlim(0, 1)
    ax.set_xlabel("Probabilidade")
    for i, v in enumerate([prob, 1 - prob]):
        ax.text(v + 0.01, i, f"{v:.2%}", va="center")

    st.pyplot(fig)

    # Armazena no histórico
    st.session_state.historico.append({
        "Tipo": tipo_transacao,
        "Valor": amount,
        "Fraude": bool(prediction),
        "Confiança": prob if prediction == 1 else 1 - prob
    })

# Exibe histórico se houver
if st.session_state.historico:
    st.subheader("📊 Histórico das Previsões")

    df_hist = pd.DataFrame(st.session_state.historico)
    st.dataframe(df_hist, use_container_width=True)

    # Gráfico de contagem de fraudes vs legítimas
    st.subheader("📉 Quantidade de Transações Fraudulentas vs Legítimas")

    counts = df_hist["Fraude"].value_counts().rename({True: "Fraudes", False: "Legítimas"})
    fig2, ax2 = plt.subplots()
    ax2.bar(counts.index, counts.values, color=["red", "green"])
    ax2.set_ylabel("Quantidade")
    st.pyplot(fig2)
