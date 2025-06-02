import pandas as pd
import requests
import os
from airflow.models import Variable
from datetime import datetime


#load_dotenv()


API_KEY = Variable.get("API_KEY")
CONTRACT_NAME = Variable.get("CONTRACT_NAME")
# Récupération de l'URL de l'API JCDecaux

API_URL = f" https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT_NAME}&apiKey={API_KEY}"

def fetch_data() : 
    
    response = requests.get(API_URL)
    print("URL utilisée :", API_URL)
    print("Code HTTP retourné :", response.status_code)


    if response.status_code != 200:
        print("Erreur lors de la récupération des données")
        return None
    
    # Conversion de la réponse en JSON
    data = response.json()
    df=pd.DataFrame(data)

    #ajout d'un timestamp à chaque ligne 
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_dir = os.path.join(os.path.dirname(__file__), "data")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    filename = os.path.join(data_dir, f"stations_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
    df.to_csv(filename, index=False)
    print(f"Les données ont été enregistrées dans le fichier {filename}")


if __name__ == "__main__":
    fetch_data()
    

       



