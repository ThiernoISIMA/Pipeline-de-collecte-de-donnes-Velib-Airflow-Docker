# mon pipeline DAG
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='velib_fetch_data',
    default_args=default_args,
    description='Pipeline pour collecter les données Vélib',
    schedule='*/15 * * * *',  # Toutes les 15 min
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    
     fetch_data = BashOperator(
        task_id='fetch_velib_data',bash_command='python /opt/airflow/dags/scripts/fetch_data.py'
        
       
    )

# fetch_data