import os
import pandas as pd

# Répertoire absolu du script
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "data")

# Vérifie si le dossier existe
if not os.path.exists(data_dir):
    print(f"Le dossier '{data_dir}' n'existe pas. Le script est interrompu.")
    exit()

# Récupère les fichiers CSV
files = sorted(
    [f for f in os.listdir(data_dir) if f.startswith("stations_") and f.endswith(".csv")],
    reverse=True
)

if not files:
    print("Aucun fichier de données trouvé.")
    exit()

latest_file = os.path.join(data_dir, files[0])
df = pd.read_csv(latest_file)

#suppression de colonnes inutiles
columns_to_keep = ['name', 'address', 'position', 'available_bikes', 'timestamp']
df = df[columns_to_keep]
#verifie s'il existe des lignes vides
if df.isnull().values.any():
    df = df.dropna()  



# Sauvegarde dans un fichier clean
output_file = os.path.join(data_dir, "stations_clean.csv")
df.to_csv(output_file, index=False)

print(f"Données nettoyées enregistrées dans {output_file}")
