import pandas as pd
from sklearn.ensemble import IsolationForest
import preTraining

# Chemins des fichiers de log
chkrootkit_log = '/home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/chkrootkit.log'
lynis_log = '/home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/lynis.log'
rkhunter_log = '/home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/rkhunter.log'

# Collecte et agrégation des données
chkrootkit_data = preTraining.parse_chkrootkit(chkrootkit_log)
lynis_data = preTraining.parse_lynis(lynis_log)
rkhunter_data = preTraining.parse_rkhunter(rkhunter_log)

# Vérification des données
print("Chkrootkit Data:", chkrootkit_data)
print("Lynis Data:", lynis_data)
print("Rkhunter Data:", rkhunter_data)

# Fusion des données
data = {**chkrootkit_data, **lynis_data, **rkhunter_data}
df = pd.DataFrame([data])

# Vérification du DataFrame
print("DataFrame:\n", df)

# Préparation des données pour l'entraînement
df = pd.get_dummies(df)  # Convertit les variables catégorielles en variables numériques

# Entraînement du modèle Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(df)

# Détection des anomalies
anomalies = model.predict(df)
print("Anomalies:", anomalies)

# Les prédictions sont -1 pour les anomalies et 1 pour les points normaux
