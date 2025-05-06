from matplotlib.pylab import f
import pandas as pd
import requests
import json
import os    
from dotenv import load_dotenv  
from airflow.models import Variable
from datetime import datetime, timedelta

load_dotenv()


API_KEY = Variable.get("API_KEY")
CONTRACT_NAME = os.getenv("CONTRACT_NAME")
# Récupération de l'URL de l'API JCDecaux

API_URL = f" https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT_NAME}&apiKey={API_KEY}"

def fetch_data() : 
    
    response = requests.get(API_URL)

    if response.status_code != 200:
        print("Erreur lors de la récupération des données")
        return None
    
    # Conversion de la réponse en JSON
    data = response.json()
    df=pd.DataFrame(data)

    #ajout d'un timestamp à chaque ligne 
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists("data"):
        os.makedirs("data")
    
    filename = f"data/stations_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    df.to_csv(filename, index=False)
    print(f"Les données ont été enregistrées dans le fichier {filename}")


if __name__ == "__main__":
    fetch_data()
    

       



