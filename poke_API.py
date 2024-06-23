import requests
import json

def get_pokemon(url='https://pokeapi.co/api/v2/pokemon-form/',offset = 0):

    args = {'offset': offset} if offset != 0 else {}

    response = requests.get(url, params = args)

    if response.status_code == 200:
        # obtener json de API
        payload = response.json()
        # obtener atributo results, caso contrario lista vacia
        result = payload.get('results', [])
        # result lleno?
        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)

        next = input("Continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemon(offset=offset+20)

def get_info_pokemon(name):
    if name == '':
        name = 'pikachu'

    url = 'https://pokeapi.co/api/v2/pokemon/'
    url_full = url + name

    response = requests.get(url_full)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        nombre = response_json['name']
        print(nombre)

if __name__ == '__main__':

    pokemon = input("Ingrese nombre de Pokemon: ").lower()
    get_info_pokemon(pokemon)

    #get_pokemon()
    '''
    url = 'https://pokeapi.co/api/v2/pokemon-form/' #lista de pokemons

    #poner limite de resultados a obtener
    args = {'offset': 0, 'limit': 1000}
    response = requests.get(url,params=args)

    if response.status_code == 200:
        #obtener json de API
        payload = response.json()
        #obtener atributo results, caso contrario lista vacia
        result = payload.get('results',[])
        #result lleno?
        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)
                
    '''