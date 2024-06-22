#put

import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Jorge', 'curso': 'python', 'nivel': 'intermedio'}
    headers = {'Content-Type': 'application/json', 'access-token': '12345'}

    response = requests.put(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:

        headers_response = response.headers  # dict
        print(headers_response)
        server = headers_response['Server']
