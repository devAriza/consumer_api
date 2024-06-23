import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
code = '44a4cb967ecfceca3a8d'
access_token = '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'

if __name__=='__main__':
    url = 'https://api.github.com/user/repos'
    paylod = {'name': 'new_repo_withAPIGitHub'}
    headers = {'Accept': 'application/json', 'Authorization': 'token ' + access_token}

    response = requests.post(url, headers=headers, json=paylod)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)
        print(response.text)

