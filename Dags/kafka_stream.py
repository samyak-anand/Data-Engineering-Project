from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'samyak',
    'start_date': datetime(2024, 4, 14, 10, 00)
}

def get_data():
    import requests
    import json

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    print(res)


get_data()