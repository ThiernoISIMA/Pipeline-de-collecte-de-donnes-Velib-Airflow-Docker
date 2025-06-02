import os
import shutil

# Répertoire de base (où se trouve ce script)
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "data")

# Chemins complets des fichiers
src = os.path.join(data_dir, "stations_transformed.csv")
dst = os.path.join(data_dir, "velib_final.csv")

# Copier le fichier transformé vers le fichier final
shutil.copyfile(src, dst)
print(f"Fichier final enregistré sous : {dst}")
