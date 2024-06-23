import requests

if __name__ == '__main__':
    username = "jorge12345"
    password = "12345"
    data = {
        'username': username,
        'password': password,
    }
    url = 'http://127.0.0.1:8000/api/v1/auth'
    response = requests.post(url, data=data)
    response.raise_for_status()

    # Obtener el token de acceso del cuerpo de la respuesta
    access_token = response.json()['access_token']
    print(access_token)

    endpoint = 'http://127.0.0.1:8000/api/v1/users/reviews'
    headers = {'Authorization': 'Bearer ' + access_token}

    respuesta = requests.get(endpoint, headers=headers)
    respuesta.raise_for_status()

    # Procesar la respuesta
    data = respuesta.json()
    print(data)
