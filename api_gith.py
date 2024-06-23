import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
print(client_id, client_secret)

code = '#code_obtenido'
#nos permite informacion del usuario logeado con GitHub
access_token = '#access_token'
#obtener access token, que permite realizar peticiones
#https://github.com/login/oauth/authorize?client_id=client_id&scope=repo

if __name__ == '__main__':
    #endpoint para obtener repos
    url = 'https://api.github.com/user/repos'

    #access_token puede ir encabezados o url
    headers = {'Authorization': 'token #access_token'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)


    #obtener access_token para la informacion de usuario logeado
    url1 = 'https://github.com/login/oauth/access_token'
    payload1 = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers1 = {'Accept': 'application/json'}
    response1 = requests.post(url1, json=payload1, headers=headers1)

    if response1.status_code == 200:
        response_json = response1.json()
        print(response_json)
        access_token = response_json['access_token']
        print(access_token)
