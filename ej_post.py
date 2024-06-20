import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Jorge', 'curso': 'python', 'nivel':'intermedio'}

    response = requests.post(url, data = json.dump(payload))

    #json post se encarga de serializarlos
    #data, nosotros serializamos
    print(response.url)

    if response.status_code == 200:
        print(response.content)