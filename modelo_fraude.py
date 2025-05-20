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

# Pré-processamento
df['type'] = df['type'].astype('category').cat.codes
X = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]
y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Salva modelo
joblib.dump(modelo, "modelo_fraude.pkl")
print("✅ Modelo treinado e salvo como 'modelo_fraude.pkl'")