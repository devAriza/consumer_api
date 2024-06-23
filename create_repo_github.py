import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
code = '#code_obtenido'
access_token = '#access_token'

if __name__=='__main__':
    url = 'https://api.github.com/user/repos'
    paylod = {'name': '#name_new_repo'}
    headers = {'Accept': 'application/json', 'Authorization': 'token ' + access_token}

    response = requests.post(url, headers=headers, json=paylod)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)
        print(response.text)

