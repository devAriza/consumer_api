import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Jorge', 'curso': 'python', 'nivel':'intermedio'}

    #encabezados
    headers = {'Content-Type': 'application/json', 'access-token': '12345'}
    #enviando datos en formato json

    #datos enviados al atributo data & json
    #response = requests.post(url, json=payload)
    # json post se encarga de serializarlos
    # data, nosotros serializamos

    #data se envian valores en atributo form
    #en caso de no querer valores en atributo form
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #dict
        print(headers_response)
        server = headers_response['Server']
        #print(server)