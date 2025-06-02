import os
import pandas as pd

# Base du script
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "data")

input_file = os.path.join(data_dir, "stations_clean.csv")
output_file = os.path.join(data_dir, "stations_transformed.csv")

# Lecture du fichier
df = pd.read_csv(input_file)

# Transformation : colonne is_available
df["is_available"] = df["available_bikes"] > 0

# Conversion du timestamp si présent
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sauvegarde
df.to_csv(output_file, index=False)
print(f"Fichier transformé : {output_file}")
