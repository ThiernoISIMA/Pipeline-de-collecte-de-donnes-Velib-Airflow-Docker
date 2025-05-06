🚴‍♂️ Pipeline de collecte de données Vélib – Airflow + Docker
Ce projet met en place un pipeline ETL simple pour collecter les données des stations Vélib via l'API JCDecaux, orchestré avec Apache Airflow et conteneurisé avec Docker.

⚙️ Fonctionnalités 

🔁 Exécution automatique toutes les 15 minutes (via cron)

📡 Récupération des données en temps réel depuis l’API JCDecaux

🧹 Suppression automatique de l’ancien fichier à chaque nouvelle extraction

📦 Stockage local des données au format CSV

🔒 Gestion sécurisée de la clé API avec les Airflow Variables


🧰 Stack utilisée

Apache Airflow 2.8+

Docker

Python 3.10

API JCDecaux


🚀 Lancer le projet
Cloner le repo

bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo/airflow
Démarrer Airflow avec Docker Compose


Définir la variable API_KEY dans l’interface Airflow
(Admin → Variables → Ajouter une clé API_KEY)

Le DAG velib_fetch_data s'exécutera automatiquement toutes les 15 min


