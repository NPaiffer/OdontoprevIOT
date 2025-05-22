import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Carrega o CSV
df = pd.read_csv("PS_20174392719_1491204439457_log.csv")
print("Colunas disponíveis no dataset:", df.columns.tolist())

# Garante que 'newbalanceOrig' exista
if 'newbalanceOrig' not in df.columns:
    df['newbalanceOrig'] = df['oldbalanceOrg'] - df['amount']

# Converte 'type' em código numérico
df['type'] = df['type'].astype('category').cat.codes

# Feature engineering: novas colunas
df['saldo_diferenca_org'] = df['oldbalanceOrg'] - df['newbalanceOrig'] - df['amount']
df['saldo_diferenca_dest'] = df['newbalanceDest'] - df['oldbalanceDest']
df['is_zero_balances'] = ((df['oldbalanceOrg'] == 0) & 
                          (df['newbalanceOrig'] == 0) & 
                          (df['oldbalanceDest'] == 0) & 
                          (df['newbalanceDest'] == 0)).astype(int)

# Features e alvo
features = [
    'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig',
    'oldbalanceDest', 'newbalanceDest',
    'saldo_diferenca_org', 'saldo_diferenca_dest', 'is_zero_balances'
]
X = df[features]
y = df['isFraud']

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
modelo.fit(X_train, y_train)

# Salva o modelo treinado
joblib.dump(modelo, "modelo_fraude.pkl")
print("✅ Modelo treinado e salvo com novas features como 'modelo_fraude.pkl'")
