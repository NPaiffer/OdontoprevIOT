import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Carregar os dados
df = pd.read_csv("PS_20174392719_1491204439457_log.csv")

print("Colunas disponíveis no CSV:")
print(df.columns.tolist())
exit()

# Pré-processamento
df = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])]
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

# Selecionar features e target
X = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]
y = df['isFraud']

# Divisão de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salvar o modelo
joblib.dump(model, 'modelo_fraude.pkl')