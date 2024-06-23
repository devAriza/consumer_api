import requests
import json
#Get como clientes, obtenemos recurso del servidor (json, xml, html)

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Jorge', 'curso': 'python', 'nivel': 'intermedio'}
    response = requests.get(url,params=args)
    print(response.json())
    if response.status_code == 200:

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
        print(f"URL completa: {response.url}")

        # response_json = response.json()
        # origin = response_json['origin']
        # print(origin)
        # content = response.content
        # print(content)

        # content = response.content #obtener el contenido de la pagina
        # file = open('kreston.html', 'wb') #abrir archivo html y escribir en binario
        # file.write(content) #escribir el contenido
        # file.close() #cerrar archivo