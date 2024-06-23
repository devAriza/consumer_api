import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
print(client_id, client_secret)

code = '91974405fd5bc03082a4'
#nos permite informacion del usuario logeado con GitHub
access_token = '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'
#obtener access token, que permite realizar peticiones
#https://github.com/login/oauth/authorize?client_id=client_id&scope=respo

if __name__ == '__main__':
    #endpoint para obtener repos
    url = 'https://api.github.com/user/repos'

    #access_token puede ir encabezados o url
    headers = {'Authorization': 'token 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'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)

    '''
    #obtener access_token para la informacion de usuario logeado
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        print(response_json)
        access_token = response_json['access_token']
        print(access_token)
    '''