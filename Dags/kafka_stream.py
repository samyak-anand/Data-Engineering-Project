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
    return res
    print(json.dumps(res,indent=3))

def format_data(res):
    data = {}
    location = res['location']
    #data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data
def stream_data():
    import json
    res= get_data()
    res= format_data(res)
    print(json.dumps(res,indent=3))

stream_data()