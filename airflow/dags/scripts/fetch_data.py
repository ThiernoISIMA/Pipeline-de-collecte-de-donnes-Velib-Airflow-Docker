# script qui va appeler l'API JCDecaux
# pour récupérer les stations de vélos
from matplotlib.pylab import f
import pandas as pd
import requests
import json
import os    
from dotenv import load_dotenv
from airflow.models import Variable
from datetime import datetime, timedelta

load_dotenv()

# Récupération de la clé API depuis le fichier .env
API_KEY = Variable.get("API_KEY")
CONTRACT_NAME = os.getenv("CONTRACT_NAME")
# Récupération de l'URL de l'API JCDecaux

API_URL = f" https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT_NAME}&apiKey={API_KEY}"
#definition de la fonction fetxh_data
def fetch_data() : 
    # Appel de l'API JCDecaux
    response = requests.get(API_URL)

    if response.status_code != 200:
        print("Erreur lors de la récupération des données")
        return None
    
    # Conversion de la réponse en JSON
    data = response.json()
    df=pd.DataFrame(data)

    #ajout d'un timestamp à chaque ligne 
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #creer le dossier data s'il n'existe pas
    if not os.path.exists("data"):
        os.makedirs("data")
    # nom du fichier de sortie
    filename = f"data/stations_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    # filename = f"/opt/airflow/dags/data/stations_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    df.to_csv(filename, index=False)
    print(f"Les données ont été enregistrées dans le fichier {filename}")


if __name__ == "__main__":
    fetch_data()
    

       



